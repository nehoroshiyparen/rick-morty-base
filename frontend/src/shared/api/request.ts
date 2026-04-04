import { api } from "./api";
import type { ApiResponse, RequestOptions } from "./types";
import { handleApiError } from "./handlers/handleApiError";
import { ZodError } from "zod";

export async function request<T>(
  url: string,
  options: RequestOptions<T> = {},
): Promise<ApiResponse<T>> {
  const { query, schema, ...axiosOptions } = options;

  try {
    let fullUrl = url;

    if (query && Object.keys(query).length) {
      const params = new URLSearchParams();
      Object.entries(query).forEach(([key, value]) => {
        params.append(key, String(value));
      });
      fullUrl += `?${params.toString()}`;
    }

    const response = await api(fullUrl, axiosOptions);

    let data: unknown = response.data?.data ?? response.data;

    if (schema) {
      try {
        data = schema.parse(data);
      } catch (e) {
        if (e instanceof ZodError) {
          console.error("❌ ZOD VALIDATION ERROR:", e.message.toString());
          return {
            success: false,
            error: "Schema validation failed",
          } as ApiResponse<T>;
        }
        throw e;
      }
    }

    return { success: true, data: data as T };
  } catch (e: unknown) {
    return handleApiError(e);
  }
}
