import type { ApiResponse } from "@/shared/api/types";

import { request } from "@/shared/api/request";
import {
  type LocationPreview,
  LocationPreviewSchema,
} from "../types/LocationPreview";

export const getList = (
  limit: number,
  offset: number,
): Promise<ApiResponse<LocationPreview[]>> => {
  return request(`/locations/`, {
    method: "GET",
    query: {
      limit,
      offset,
    },
    schema: LocationPreviewSchema.array(),
  });
};
