import { EpisodePreviewSchema } from "@/entities/episodes/types/EpisodePreview";
import { LocationPreviewSchema } from "@/entities/locations/types/LocationPreview";
import z from "zod";

export const CharacterFullSchema = z.object({
  id: z.number(),
  external_id: z.number(),
  name: z.string(),
  status: z.string(),
  species: z.string(),
  type: z.string().nullable(),
  gender: z.string(),
  origin: LocationPreviewSchema.nullable(),
  location: LocationPreviewSchema,
  image: z.url(),
  url: z.url(),
  created_at: z.string().transform((val) => new Date(val)),
  episodes: z.array(EpisodePreviewSchema),
});
export type CharacterFull = z.infer<typeof CharacterFullSchema>;
