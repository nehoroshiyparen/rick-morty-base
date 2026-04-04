import type { CharacterPreview } from "@/entities/characters/types/CharacterPreview";
import { CharacterCard } from "@/entities/characters/ui/CharacterCard";

type Props = {
  characters: CharacterPreview[];
};

export function CharacterFeed({ characters }: Props) {
  if (characters.length === 0) {
    return (
      <div className="flex flex-col items-center justify-center py-40 text-zinc-600">
        <span className="text-6xl mb-4">👽</span>
        <p className="font-body text-lg">No characters found</p>
      </div>
    );
  }

  return (
    <div className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 xl:grid-cols-5 gap-4">
      {characters.map((character) => (
        <CharacterCard key={character.id} character={character} />
      ))}
    </div>
  );
}
