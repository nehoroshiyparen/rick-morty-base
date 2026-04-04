import type { ApiResponse } from "@/shared/api/types";
import { CharacterFullSchema, type CharacterFull } from "../types/CharacterFull";
import { request } from "@/shared/api/request";

export const update = (
  id: number,
  data: { name: string },
): Promise<ApiResponse<CharacterFull>> => {
  return request(`/characters/${id}`, {
    method: "PATCH",
    data,
    schema: CharacterFullSchema,
  });
};
