import { CharacterFeed } from "@/widgets/characters/CharacterFeed";
import { useCharacters } from "@/entities/characters/hooks/useCharacters";
import { InfiniteScrollTrigger } from "@/features/infinite_scroll/components/InfiniteScrollTrigger";

export function CharactersPage() {
  const { characters, loading, hasMore, loadMore } = useCharacters(10);
  return (
    <div className="min-h-screen bg-zinc-950 pt-32">
      {/* Подзаголовок */}
      <div className="px-8 pb-8 border-b border-zinc-800">
        <p className="font-body text-(--rick-morty) text-sm font-semibold tracking-widest uppercase mb-2">
          Universe
        </p>
        <div className="flex flex-col justify-between">
          <h2 className="font-display text-4xl font-bold text-white">
            Characters
          </h2>
          <span className="font-body text-zinc-500 text-sm">
            {characters.length} found
          </span>
        </div>
      </div>

      {/* Лента */}
      <div className="px-8 py-8">
        <CharacterFeed characters={characters} />

        <InfiniteScrollTrigger onLoadMore={loadMore} hasMore={hasMore} />

        {loading && <p className="text-white text-center">Loading...</p>}
      </div>
    </div>
  );
}
