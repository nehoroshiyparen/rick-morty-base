import type { Mapper } from "@/shared/interfaces/baseMapper";
import type { ApiResponse } from "../types";

// Перегрузка для массива
export function handleApiResponse<TDto, TDomain>(
  response: ApiResponse<TDto[]>,
  mapper: Mapper<TDto, TDomain>,
): ApiResponse<TDomain[]>;

// Перегрузка для одиночного элемента
export function handleApiResponse<TDto, TDomain>(
  response: ApiResponse<TDto>,
  mapper: Mapper<TDto, TDomain>,
): ApiResponse<TDomain>;

export function handleApiResponse<TDto, TDomain>(
  response: ApiResponse<TDto | TDto[]>,
  mapper: Mapper<TDto, TDomain>,
): ApiResponse<TDomain | TDomain[]> {
  if (!response.success) {
    return response as ApiResponse<TDomain | TDomain[]>;
  }

  if (Array.isArray(response.data)) {
    return {
      success: true,
      data: response.data.map(mapper.toDomain),
    };
  }

  return {
    success: true,
    data: mapper.toDomain(response.data),
  };
}
