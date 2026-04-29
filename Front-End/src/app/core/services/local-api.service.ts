import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { environment } from 'src/environments/environment';
import { Observable, throwError } from 'rxjs';
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

  constructor(private http: HttpClient) {}

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
    return this.http.get<any[]>(`${this.baseUrl}/productos`)
      .pipe(catchError(this.handleError));
  }

  /**
   * Registra un producto en la base de datos local.
   */
  addProducto(producto: any): Observable<any> {
    return this.http.post<any>(`${this.baseUrl}/productos`, producto)
      .pipe(catchError(this.handleError));
  }

  /**
   * Obtiene los clientes registrados localmente.
   */
  getClientes(): Observable<any[]> {
    return this.http.get<any[]>(`${this.baseUrl}/clientes`)
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
