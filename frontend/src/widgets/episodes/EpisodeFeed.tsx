import type { EpisodePreview } from "@/entities/episodes/types/EpisodePreview";
import { EpisodeCard } from "@/entities/episodes/ui/EpisodeCard";

type Props = {
  episodes: EpisodePreview[];
};

export function EpisodeFeed({ episodes }: Props) {
  if (episodes.length === 0) {
    return (
      <div className="flex flex-col items-center justify-center py-40 text-zinc-600">
        <span className="text-6xl mb-4">📺</span>
        <p className="font-body text-lg">No episodes found</p>
      </div>
    );
  }

  return (
    <div className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 xl:grid-cols-5 gap-4">
      {episodes.map((episode) => (
        <EpisodeCard key={episode.id} episode={episode} />
      ))}
    </div>
  );
}
