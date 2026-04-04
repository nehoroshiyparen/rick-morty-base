import type { ApiResponse } from "@/shared/api/types";
import { EpisodeFullSchema, type EpisodeFull } from "../types/EpisodeFull";
import { request } from "@/shared/api/request";

export const update = (
  id: number,
  data: { name: string },
): Promise<ApiResponse<EpisodeFull>> => {
  return request(`/episodes/${id}`, {
    method: "PATCH",
    data,
    schema: EpisodeFullSchema,
  });
};
