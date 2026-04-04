import type { ApiResponse } from "@/shared/api/types";
import { LocationFullSchema, type LocationFull } from "../types/LocationFull";
import { request } from "@/shared/api/request";

export const update = (
  id: number,
  data: { name: string },
): Promise<ApiResponse<LocationFull>> => {
  return request(`/locations/${id}`, {
    method: "PATCH",
    data,
    schema: LocationFullSchema,
  });
};
