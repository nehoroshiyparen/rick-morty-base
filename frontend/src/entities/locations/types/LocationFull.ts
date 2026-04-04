import { CharacterPreviewSchema } from "@/entities/characters/types/CharacterPreview";
import z from "zod";

export const LocationFullSchema = z.object({
  id: z.number(),
  external_id: z.number(),
  name: z.string(),
  type: z.string(),
  dimension: z.string(),
  url: z.url(),
  created_at: z.string().transform((val) => new Date(val)),
  characters_location: z.array(CharacterPreviewSchema),
});
export type LocationFull = z.infer<typeof LocationFullSchema>;
