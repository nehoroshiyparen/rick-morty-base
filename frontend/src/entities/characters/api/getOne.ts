import type { ApiResponse } from "@/shared/api/types";
import {
  CharacterFullSchema,
  type CharacterFull,
} from "../types/CharacterFull";
import { request } from "@/shared/api/request";

export const getOne = (id: number): Promise<ApiResponse<CharacterFull>> => {
  return request(`/characters/${id}`, {
    method: "GET",
    schema: CharacterFullSchema,
  });
};
