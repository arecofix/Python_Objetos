import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse, HttpHeaders } from '@angular/common/http';
import { environment } from 'src/environments/environment';
import { Observable, throwError, firstValueFrom } from 'rxjs';
import { catchError } from 'rxjs/operators';

export interface HealthResponse {
  status: string;
  message: string;
  os_path_example: string;
  server: string;
  version: string;
  mode: string;
}

/**
 * Servicio para interactuar con el motor local (Back-end Python).
 * Utilizado para la arquitectura Offline-First.
 */
@Injectable({
  providedIn: 'root'
})
export class LocalApiService {
  private readonly baseUrl = environment.localEngineUrl;
  private readonly TOKEN_KEY = 'local_offline_token';

  constructor(private http: HttpClient) {}

  /**
   * Genera las cabeceras HTTP incluyendo el Token JWT local si existe.
   */
  private getHeaders(): { headers: HttpHeaders } {
    let headers = new HttpHeaders();
    const token = localStorage.getItem(this.TOKEN_KEY);
    if (token) {
      headers = headers.set('Authorization', `Bearer ${token}`);
    }
    return { headers };
  }

  /**
   * Inicia sesión en el motor local (Offline).
   */
  async loginOffline(username: string, password: string):Promise<any> {
    try {
      const response: any = await firstValueFrom(
        this.http.post(`${this.baseUrl}/login`, { username, password })
      );
      if (response && response.token) {
        localStorage.setItem(this.TOKEN_KEY, response.token);
      }
      return response;
    } catch (error) {
      this.handleError(error as HttpErrorResponse);
      throw error;
    }
  }

  /**
   * Cierra la sesión local.
   */
  logoutOffline(): void {
    localStorage.removeItem(this.TOKEN_KEY);
  }

  /**
   * Verifica la conexión y salud del motor de datos local.
   */
  checkHealth(): Observable<HealthResponse> {
    return this.http.get<HealthResponse>(`${this.baseUrl}/health`)
      .pipe(catchError(this.handleError));
  }

  /**
   * Verifica si el motor de datos local está activo (legacy status).
   * @deprecated Use checkHealth() instead
   */
  getStatus(): Observable<any> {
    return this.http.get(`${this.baseUrl}/health`)
      .pipe(catchError(this.handleError));
  }

  /**
   * Obtiene los productos del inventario local (SQLite).
   */
  getProductos(): Observable<any[]> {
    return this.http.get<any[]>(`${this.baseUrl}/productos`, this.getHeaders())
      .pipe(catchError(this.handleError));
  }

  /**
   * Registra un producto en la base de datos local.
   */
  addProducto(producto: any): Observable<any> {
    return this.http.post<any>(`${this.baseUrl}/productos`, producto, this.getHeaders())
      .pipe(catchError(this.handleError));
  }

  /**
   * Obtiene los clientes registrados localmente.
   */
  getClientes(): Observable<any[]> {
    return this.http.get<any[]>(`${this.baseUrl}/clientes`, this.getHeaders())
      .pipe(catchError(this.handleError));
  }

  // --- Manejo de Errores Global ---
  private handleError(error: HttpErrorResponse) {
    let errorMessage = 'Ha ocurrido un error desconocido con el servidor local';
    if (error.error instanceof ErrorEvent) {
      // Error del lado del cliente o de red
      errorMessage = `Error de cliente: ${error.error.message}`;
    } else {
      // El backend retornó un código de error
      errorMessage = `El servidor local retornó el código ${error.status}: ${error.message}`;
    }
    console.error('LocalApiService Error:', errorMessage);
    return throwError(() => new Error(errorMessage));
  }
}
