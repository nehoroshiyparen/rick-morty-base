import type { CharacterPreview } from "@/entities/characters/types/CharacterPreview";
import { ImageWithRetry } from "@/features/image_with_retry/ImageWithRetry";
import { Link } from "react-router-dom";

const STATUS_CONFIG = {
  Alive: { dot: "bg-green-400" },
  Dead: { dot: "bg-red-500" },
  Unknown: { dot: "bg-zinc-400" },
} as const;

type Props = {
  character: CharacterPreview;
  onClick?: (character: CharacterPreview) => void;
};

export function CharacterMiniCard({ character, onClick }: Props) {
  const status =
    STATUS_CONFIG[character.status as keyof typeof STATUS_CONFIG] ??
    STATUS_CONFIG.Unknown;

  return (
    <Link
      to={`/characters/${character.id}`}
      onClick={() => onClick?.(character)}
      className="group flex items-center gap-3 bg-zinc-900 border border-zinc-800 hover:border-zinc-700
                 rounded-xl p-2.5 cursor-pointer transition-all duration-200 hover:bg-zinc-800"
    >
      <div className="relative w-10 h-10 rounded-lg overflow-hidden shrink-0">
        <ImageWithRetry
          src={character.image}
          alt={character.name}
          className="w-full h-full object-cover"
        />
      </div>

      <div className="min-w-0">
        <p className="font-display text-white text-sm font-bold truncate">
          {character.name}
        </p>
        <div className="flex items-center gap-1.5 mt-0.5">
          <span className={`w-1.5 h-1.5 rounded-full shrink-0 ${status.dot}`} />
          <span className="font-body text-zinc-500 text-xs">
            {character.status}
          </span>
        </div>
      </div>
    </Link>
  );
}
