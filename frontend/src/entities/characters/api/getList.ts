import type { ApiResponse } from "@/shared/api/types";

import { request } from "@/shared/api/request";
import {
  CharacterPreviewSchema,
  type CharacterPreview,
} from "../types/CharacterPreview";

export const getList = (
  limit: number,
  offset: number,
): Promise<ApiResponse<CharacterPreview[]>> => {
  return request(`/characters/`, {
    method: "GET",
    query: {
      limit,
      offset,
    },
    schema: CharacterPreviewSchema.array(),
  });
};
