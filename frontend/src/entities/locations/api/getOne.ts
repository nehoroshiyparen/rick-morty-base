import type { ApiResponse } from "@/shared/api/types";
import { type LocationFull, LocationFullSchema } from "../types/LocationFull";
import { request } from "@/shared/api/request";

export const getOne = (id: number): Promise<ApiResponse<LocationFull>> => {
  return request(`/locations/${id}`, {
    method: "GET",
    schema: LocationFullSchema,
  });
};
