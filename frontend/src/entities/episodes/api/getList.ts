import type { ApiResponse } from "@/shared/api/types";

import { request } from "@/shared/api/request";
import {
  type EpisodePreview,
  EpisodePreviewSchema,
} from "../types/EpisodePreview";

export const getList = (
  limit: number,
  offset: number,
): Promise<ApiResponse<EpisodePreview[]>> => {
  return request(`/episodes/`, {
    method: "GET",
    query: {
      limit,
      offset,
    },
    schema: EpisodePreviewSchema.array(),
  });
};
