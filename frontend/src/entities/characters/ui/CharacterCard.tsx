import { ImageWithRetry } from "@/features/image_with_retry/ImageWithRetry";
import type { CharacterPreview } from "../types/CharacterPreview";
import { Link } from "react-router-dom";

const STATUS_CONFIG = {
  Alive: { dot: "bg-green-400", label: "Alive" },
  Dead: { dot: "bg-red-500", label: "Dead" },
  Unknown: { dot: "bg-zinc-400", label: "Unknown" },
} as const;

type Props = {
  character: CharacterPreview;
};

export function CharacterCard({ character }: Props) {
  const status =
    STATUS_CONFIG[character.status as keyof typeof STATUS_CONFIG] ??
    STATUS_CONFIG.Unknown;

  return (
    <Link
      to={`./${character.id}`}
      className="group relative top-0 flex flex-col overflow-hidden rounded-2xl bg-zinc-900 cursor-pointer
             transition-all duration-300 hover:-top-1 hover:shadow-xl hover:shadow-black/60"
    >
      {/* Картинка */}
      <div className="relative aspect-square overflow-hidden">
        <ImageWithRetry
          src={character.image}
          alt={character.name}
          className="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105"
        />
        <div className="absolute inset-0 bg-linear-to-t from-zinc-900 via-zinc-900/10 to-transparent" />
      </div>

      {/* Инфо */}
      <div className="px-4 py-3">
        <h3 className="font-display text-white font-bold text-base truncate">
          {character.name}
        </h3>

        <div className="flex items-center gap-2 mt-1.5">
          <span className={`w-2 h-2 rounded-full shrink-0 ${status.dot}`} />
          <span className="font-body text-zinc-400 text-xs">
            {status.label}
          </span>
        </div>
      </div>

      {/* Акцент при ховере */}
      <div className="absolute inset-x-0 bottom-0 h-0.5 bg-(--rick-morty) scale-x-0 group-hover:scale-x-100 transition-transform duration-300" />
    </Link>
  );
}
