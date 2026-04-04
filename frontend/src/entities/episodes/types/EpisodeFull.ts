import { CharacterPreviewSchema } from "@/entities/characters/types/CharacterPreview";
import z from "zod";

export const EpisodeFullSchema = z.object({
  id: z.number(),
  external_id: z.number(),
  name: z.string(),
  air_date: z.string().transform((val) => new Date(val)),
  episode: z.string(),
  url: z.url(),
  created_at: z.string().transform((val) => new Date(val)),
  characters: z.array(CharacterPreviewSchema),
});
export type EpisodeFull = z.infer<typeof EpisodeFullSchema>;
