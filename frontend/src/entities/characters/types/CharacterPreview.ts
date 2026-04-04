import z from "zod";

export const CharacterPreviewSchema = z.object({
  id: z.number(),
  external_id: z.number(),
  name: z.string(),
  status: z.string(),
  image: z.url(),
});
export type CharacterPreview = z.infer<typeof CharacterPreviewSchema>;
