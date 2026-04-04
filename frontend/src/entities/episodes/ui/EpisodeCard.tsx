import { Link } from "react-router-dom";
import type { EpisodePreview } from "../types/EpisodePreview";

type Props = {
  episode: EpisodePreview;
};

export function EpisodeCard({ episode }: Props) {
  const [season, ep] = episode.episode.split("E");

  return (
    <Link
      to={`./${episode.id}`}
      className="group relative bg-zinc-900 rounded-2xl p-5 cursor-pointer
                 transition-all duration-300 hover:-translate-y-1 hover:shadow-xl hover:shadow-black/60
                 border border-zinc-800 hover:border-zinc-700 overflow-hidden"
    >
      {/* Декоративный фон */}
      <div className="absolute inset-0 bg-linear-to-br from-(--rick-morty)/5 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300" />

      {/* Код эпизода */}
      <div className="relative flex items-end gap-1 mb-4">
        <span className="font-display text-4xl font-bold text-(--rick-morty) leading-none">
          {season}
        </span>
        <span className="font-display text-xl font-bold text-zinc-500 leading-none mb-0.5">
          E{ep}
        </span>
      </div>

      {/* Название */}
      <h3 className="relative font-display text-white font-bold text-base truncate mb-2">
        {episode.name}
      </h3>

      {/* Дата */}
      <p className="relative font-body text-zinc-500 text-xs">
        {String(episode.air_date)}
      </p>

      {/* Нижний акцент */}
      <div className="absolute inset-x-0 bottom-0 h-0.5 bg-(--rick-morty) scale-x-0 group-hover:scale-x-100 transition-transform duration-300" />
    </Link>
  );
}
