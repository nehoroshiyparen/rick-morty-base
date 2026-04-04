import { isAxiosError } from "axios";
import type { ApiFail } from "../types";
import z from "zod";

export function handleApiError(err: unknown): ApiFail {
  // AxiosError
  if (isAxiosError(err)) {
    const status = err.response?.status;
    const message =
      err.response?.data?.error ||
      (err.response?.statusText
        ? `Status code: ${err.response?.status}`
        : "Ошибка соединения с сервером");

    return { success: false, error: message, status };
  }

  // ZodError
  if (err instanceof z.ZodError) {
    return { success: false, error: "Неверный формат данных от сервера" };
  }

  // Любая другая ошибка
  return { success: false, error: "Неизвестная ошибка" };
}
