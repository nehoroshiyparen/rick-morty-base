import { Link } from "react-router-dom";
import type { LocationPreview } from "../types/LocationPreview";

type Props = {
  location: LocationPreview;
};

export function LocationCard({ location }: Props) {
  return (
    <Link
      to={`./${location.id}`}
      className="group relative bg-zinc-900 rounded-2xl p-5 cursor-pointer
                 transition-all duration-300 hover:-translate-y-1 hover:shadow-xl hover:shadow-black/60
                 border border-zinc-800 hover:border-zinc-700 overflow-hidden"
    >
      {/* Декоративный фон */}
      <div className="absolute inset-0 bg-linear-to-br from-(--rick-morty)/5 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300" />

      {/* Иконка */}
      <div className="relative w-10 h-10 rounded-full bg-zinc-800 group-hover:bg-(--rick-morty)/10 transition-colors duration-300 flex items-center justify-center mb-4">
        <span className="text-lg">🌍</span>
      </div>

      {/* Название */}
      <h3 className="relative font-display text-white font-bold text-base truncate mb-2">
        {location.name}
      </h3>

      {/* Измерение */}
      <p className="relative font-body text-zinc-500 text-xs truncate">
        {location.dimension}
      </p>

      {/* Нижний акцент */}
      <div className="absolute inset-x-0 bottom-0 h-0.5 bg-(--rick-morty) scale-x-0 group-hover:scale-x-100 transition-transform duration-300" />
    </Link>
  );
}
