import z from "zod";

export const EpisodePreviewSchema = z.object({
  id: z.number(),
  external_id: z.number(),
  name: z.string(),
  air_date: z.string().transform((val) => new Date(val)),
  episode: z.string(),
});
export type EpisodePreview = z.infer<typeof EpisodePreviewSchema>;
