import { Injectable, inject, PLATFORM_ID, signal } from '@angular/core';
import { isPlatformBrowser } from '@angular/common';
import {
  User,
  Session,
  AuthChangeEvent,
  AuthResponse,
} from '@supabase/supabase-js';
import { environment } from '../../../environments/environment';
import { SUPABASE_CLIENT } from '../di/supabase-token';
import { BehaviorSubject, Observable } from 'rxjs';
import { LoggerService } from './logger.service';
import { ProfileService } from './profile.service';
import { TenantService } from './tenant.service';
import { LocalApiService } from './local-api.service';
import { UserProfile } from '@app/shared/interfaces/user.interface';
import { App } from '@capacitor/app';
import { Browser } from '@capacitor/browser';
import { NgZone } from '@angular/core';
import { Capacitor } from '@capacitor/core';
import { TENANT_CONSTANTS } from '../constants/tenant.constants';

@Injectable({
  providedIn: 'root',
})
export class AuthService {
  private supabase = inject(SUPABASE_CLIENT);
  private logger = inject(LoggerService);
  private platformId = inject(PLATFORM_ID);
  private profileService = inject(ProfileService);
  private tenantService = inject(TenantService);
  private localApiService = inject(LocalApiService);
  private ngZone = inject(NgZone);
  
  // Súper Administrador Global
  public isSuperAdmin = signal<boolean>(false);

  private authState = new BehaviorSubject<{
    session: Session | null;
    user: User | null;
    profile: UserProfile | null;
  }>({
    session: null,
    user: null,
    profile: null,
  });

  public authState$ = this.authState.asObservable();

  // Método para obtener el perfil actual
  getCurrentProfile(): UserProfile | null {
    return this.authState.value.profile;
  }

  constructor() {
    if (isPlatformBrowser(this.platformId)) {
      this.initAuth();
      this.setupDeepLinks();
    }
  }

  private setupDeepLinks() {
    App.addListener('appUrlOpen', (data: any) => {
      this.ngZone.run(async () => {
        const url = new URL(data.url);
        // Clean URL if it has fragments like #access_token
        if (url.hash) {
            const params = new URLSearchParams(url.hash.substring(1));
            const accessToken = params.get('access_token');
            const refreshToken = params.get('refresh_token');
            if (accessToken && refreshToken) {
                await this.supabase.auth.setSession({
                    access_token: accessToken,
                    refresh_token: refreshToken
                });
                // Close browser if open
                await Browser.close();
            }
        }
      });
    });
  }

  private async initAuth() {
    // Check offline token first
    const offlineToken = localStorage.getItem('local_offline_token');
    if (offlineToken) {
       const mockUser: User = { id: 'offline-admin-id', app_metadata: {}, user_metadata: {}, aud: 'authenticated', created_at: new Date().toISOString(), email: 'admin' } as any;
       const mockSession: Session = { access_token: offlineToken, refresh_token: '', expires_in: 86400, token_type: 'bearer', user: mockUser };
       const mockProfile: UserProfile = { id: 'offline-admin-id', email: 'admin', role: 'super_admin' } as any;
       
       this.authState.next({ session: mockSession, user: mockUser, profile: mockProfile });
       this.isSuperAdmin.set(true);
    }

    try {
      const { data: { session }, error } = await this.supabase.auth.getSession();
      
      if (error) {
        this.logger.error('Session retrieval error', error);
        // If technical error like refresh token invalid, clear local session to allow clean state
        if (error.message.includes('Refresh Token')) {
           await this.supabase.auth.signOut();
        }
      }

      if (session) {
        const profile = await this.ensureProfile(session);
        this.authState.next({ session, user: session.user, profile });
        if (profile && (TENANT_CONSTANTS.SUPER_ADMIN_EMAILS.includes(profile.email || '') || profile.role === 'super_admin')) {
          this.isSuperAdmin.set(true);
        }
      }
    } catch (e) {
      this.logger.error('Critical auth init failure', e);
    }

    this.supabase.auth.onAuthStateChange(
      async (event: AuthChangeEvent, session: Session | null) => {
        this.logger.info(`Auth Event: ${event}`);
        
        const isOffline = !!localStorage.getItem('local_offline_token');

        if (event === 'SIGNED_OUT') {
           if (!isOffline) {
               this.authState.next({ session: null, user: null, profile: null });
               this.isSuperAdmin.set(false);
           }
           return;
        }

        if (session) {
          const profile = await this.ensureProfile(session);
          this.authState.next({ session, user: session.user, profile });
          if (profile && (TENANT_CONSTANTS.SUPER_ADMIN_EMAILS.includes(profile.email || '') || profile.role === 'super_admin')) {
            this.isSuperAdmin.set(true);
          }
        } else if (!isOffline) {
          this.authState.next({ session: null, user: null, profile: null });
          this.isSuperAdmin.set(false);
        }
      },
    );
  }

  /**
   * Ensures a profile row exists for the given session user.
   * If no profile exists yet, creates one from auth user metadata.
   * This permanently fixes the PGRST116 issue for new/OAuth users.
   */
  private async ensureProfile(session: Session): Promise<UserProfile | null> {
    try {
      const existingProfile = await this.profileService.getProfile(session.user.id);
      if (existingProfile) return existingProfile;

      // Profile row doesn't exist yet — auto-create it from auth metadata
      const meta = session.user.user_metadata || {};
      const tenantId = this.tenantService.getTenantId();
      const isFallback = tenantId === TENANT_CONSTANTS.FALLBACK_ID;

      const payload: any = {
        id: session.user.id,
        email: session.user.email || meta['email'] || '',
        first_name: meta['first_name'] || meta['given_name'] || null,
        last_name: meta['last_name'] || meta['family_name'] || null,
        full_name: meta['full_name'] || meta['name'] || null,
        avatar_url: meta['avatar_url'] || meta['picture'] || null,
        role: meta['role'] || session.user.app_metadata?.['role'] || 'user',
        is_active: true,
        created_at: new Date().toISOString(),
        updated_at: new Date().toISOString(),
      };

      // 🚨 Configuración de Súper Admin Central (ezequielenrico15@gmail.com)
      if (payload.email && TENANT_CONSTANTS.SUPER_ADMIN_EMAILS.includes(payload.email)) {
        payload.role = 'super_admin';
        this.isSuperAdmin.set(true);
      }

      // Only include tenant_id if it is not the fallback placeholder
      if (!isFallback) {
        payload['tenant_id'] = tenantId;
      }

      const { data, error } = await this.supabase
        .from('profiles')
        .upsert(payload, { onConflict: 'id' })
        .select()
        .maybeSingle();

      if (error) {
        this.logger.error('Failed to auto-create profile row', error);
        return null;
      }

      this.logger.info(`Profile auto-created for user ${session.user.id}`);
      
      const createdProfile = data as UserProfile | null;
      if (createdProfile && (TENANT_CONSTANTS.SUPER_ADMIN_EMAILS.includes(createdProfile.email || '') || createdProfile.role === 'super_admin')) {
        this.isSuperAdmin.set(true);
      }
      
      return createdProfile;
    } catch (err) {
      this.logger.error('ensureProfile error', err);
      return null;
    }
  }

  async signOut(): Promise<string | null> {
    this.localApiService.logoutOffline();
    const { error } = await this.supabase.auth.signOut();
    this.authState.next({ session: null, user: null, profile: null });
    this.isSuperAdmin.set(false);
    return error ? error.message : null;
  }

  getCurrentUser(): User | null {
    return this.authState.value.user;
  }

  async getUser(): Promise<User | null> {
    const {
      data: { user },
    } = await this.supabase.auth.getUser();
    return user;
  }

  getCurrentSession(): Session | null {
    return this.authState.value.session;
  }

  async getSession(): Promise<Session | null> {
    const { data } = await this.supabase.auth.getSession();
    return data.session;
  }

  async getUserProfile(userId: string): Promise<UserProfile | null> {
    return this.profileService.getProfile(userId);
  }

  async updateUserProfile(
    userId: string,
    profile: Partial<UserProfile>,
  ): Promise<UserProfile | null> {
    return this.profileService.updateProfile(userId, profile);
  }

  getSupabaseClient() {
    return this.supabase;
  }

  // Social Logins
  private async signInWithProvider(provider: 'google' | 'facebook' | 'github'): Promise<any> {
    const isNative = Capacitor.isNativePlatform();

    const { data, error } = await this.supabase.auth.signInWithOAuth({
      provider,
      options: { 
        redirectTo: environment.authRedirectUrl,
        skipBrowserRedirect: isNative
      },
    });

    if (isNative && data?.url) {
      await Browser.open({ url: data.url });
    }

    return { data, error };
  }

  async signInWithGoogle(): Promise<any> {
    return this.signInWithProvider('google');
  }

  async signInWithFacebook(): Promise<any> {
    return this.signInWithProvider('facebook');
  }

  async signInWithGithub(): Promise<any> {
    return this.signInWithProvider('github');
  }

  async signIn(email: string, password: string): Promise<any> {
    try {
      // First check if it looks like an offline admin account or local fallback
      if (email === 'admin' || !email.includes('@')) {
         return this.attemptOfflineLogin(email, password);
      }

      const res = await this.supabase.auth.signInWithPassword({ email, password });
      if (res.error) {
        // Fallback for network errors
        if (res.error.message.includes('fetch') || res.error.message.includes('Network') || res.error.message.includes('Failed to fetch')) {
            return this.attemptOfflineLogin(email, password);
        }
        return res;
      }
      return res;
    } catch (error: any) {
      return this.attemptOfflineLogin(email, password);
    }
  }

  private async attemptOfflineLogin(email: string, password: string): Promise<any> {
    this.logger.info('Attempting offline login fallback');
    try {
       const localRes = await this.localApiService.loginOffline(email, password);
       if (localRes && localRes.token) {
           const mockUser: User = {
               id: localRes.admin.id || 'offline-admin-id',
               app_metadata: {},
               user_metadata: {},
               aud: 'authenticated',
               created_at: new Date().toISOString(),
               email: email
           } as any;
           const mockSession: Session = {
               access_token: localRes.token,
               refresh_token: '',
               expires_in: 86400,
               token_type: 'bearer',
               user: mockUser
           };
           const mockProfile: UserProfile = {
               id: localRes.admin.id || 'offline-admin-id',
               email: email,
               role: 'super_admin'
           } as any;
           
           this.authState.next({ session: mockSession, user: mockUser, profile: mockProfile });
           this.isSuperAdmin.set(true);
           return { data: { session: mockSession, user: mockUser }, error: null };
       }
       return { data: null, error: { message: 'Invalid offline credentials' } };
    } catch (e) {
       return { data: null, error: { message: 'Network error and offline login failed.' } };
    }
  }

  async signUp(
    email: string,
    password: string,
    profileData: Partial<UserProfile>,
  ): Promise<any> {
    const tenantId = this.tenantService.getTenantId();
    this.logger.info(`Attempting signUp for ${email} with tenant: ${tenantId}`);
    
    try {
      const response = await this.supabase.auth.signUp({
        email,
        password,
        options: { 
          data: { 
            ...profileData,
            tenant_id: tenantId
          } 
        },
      });
      
      this.logger.info(`SignUp response for ${email}`, response);
      return response;
    } catch (error) {
      this.logger.error(`Catch error in signUp for ${email}`, error);
      throw error;
    }
  }

  // Auth specific utilities
  async resetPassword(email: string): Promise<string | null> {
    const { error } = await this.supabase.auth.resetPasswordForEmail(email, {
      redirectTo: environment.authRedirectUrl,
    });
    return error ? error.message : null;
  }

  async updatePassword(newPassword: string): Promise<string | null> {
    const { error } = await this.supabase.auth.updateUser({
      password: newPassword,
    });
    return error ? error.message : null;
  }
}
