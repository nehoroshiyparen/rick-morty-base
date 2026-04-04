import type { AxiosRequestConfig } from "axios";
import z from "zod";

export type ApiSuccess<T> = { success: true; data: T };
export type ApiFail = { success: false; error: string; status?: number };

export type ApiResponse<T> = ApiSuccess<T> | ApiFail;

export interface RequestOptions<T> extends AxiosRequestConfig {
  schema?: z.ZodType<T>;
  query?: Record<string, string | number>;
}
