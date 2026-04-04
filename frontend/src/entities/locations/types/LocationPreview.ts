import z from "zod";

export const LocationPreviewSchema = z.object({
  id: z.number(),
  external_id: z.number(),
  name: z.string(),
  dimension: z.string(),
});
export type LocationPreview = z.infer<typeof LocationPreviewSchema>;
