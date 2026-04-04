import type { ApiResponse } from "@/shared/api/types";
import { type EpisodeFull, EpisodeFullSchema } from "../types/EpisodeFull";
import { request } from "@/shared/api/request";

export const getOne = (id: number): Promise<ApiResponse<EpisodeFull>> => {
  return request(`/episodes/${id}`, {
    method: "GET",
    schema: EpisodeFullSchema,
  });
};
