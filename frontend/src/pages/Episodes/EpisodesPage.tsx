import { EpisodeFeed } from "@/widgets/episodes/EpisodeFeed";
import { InfiniteScrollTrigger } from "@/features/infinite_scroll/components/InfiniteScrollTrigger";
import { useEpisodes } from "@/entities/episodes/hooks/useEpisodes";

export function EpisodesPage() {
  const { episodes, loading, hasMore, loadMore } = useEpisodes(40);

  return (
    <div className="min-h-screen bg-zinc-950 pt-32">
      <div className="px-8 pb-8 border-b border-zinc-800">
        <p className="font-body text-(--rick-morty) text-sm font-semibold tracking-widest uppercase mb-2">
          Story
        </p>
        <div className="flex flex-col justify-between">
          <h2 className="font-display text-4xl font-bold text-white">
            Episodes
          </h2>
          <span className="font-body text-zinc-500 text-sm">
            {episodes.length} found
          </span>
        </div>
      </div>

      <div className="px-8 py-8">
        <EpisodeFeed episodes={episodes} />
        <InfiniteScrollTrigger onLoadMore={loadMore} hasMore={hasMore} />
        {loading && <p className="text-white text-center mt-4">Loading...</p>}
      </div>
    </div>
  );
}
