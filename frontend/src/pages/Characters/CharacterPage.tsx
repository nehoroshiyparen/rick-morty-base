import { useCharacters } from "@/entities/characters/hooks/useCharacters";
import type { EpisodePreview } from "@/entities/episodes/types/EpisodePreview";
import { useEffect, useRef, useState } from "react";
import { Link, useParams } from "react-router-dom";

const STATUS_CONFIG = {
  Alive: { dot: "bg-green-400", label: "Alive" },
  Dead: { dot: "bg-red-500", label: "Dead" },
  Unknown: { dot: "bg-zinc-400", label: "Unknown" },
} as const;

type InfoCardProps = { label: string; value: string | null };

function InfoCard({ label, value }: InfoCardProps) {
  return (
    <div className="bg-zinc-900 rounded-xl p-4 border border-zinc-800">
      <p className="font-body text-zinc-500 text-xs uppercase tracking-widest mb-1">
        {label}
      </p>
      <p className="font-display text-white font-bold text-sm truncate">
        {value && value !== "" ? value : "Unknown"}
      </p>
    </div>
  );
}

type EpisodeChipProps = { episode: EpisodePreview };

function EpisodeChip({ episode }: EpisodeChipProps) {
  const id = episode.id;
  return (
    <Link
      to={`/episodes/${episode.id}`}
      className="font-body text-xs text-(--rick-morty) bg-(--rick-morty)/10 border border-(--rick-morty)/20 rounded-lg px-3 py-1.5 hover:bg-(--rick-morty)/20 transition-colors cursor-pointer"
    >
      EP {id}
    </Link>
  );
}

export function CharacterPage() {
  const params = useParams();
  const id = Number(params.id);

  const { character, loadOne, updateOne } = useCharacters();

  const [isEditing, setIsEditing] = useState(false);
  const [nameValue, setNameValue] = useState("");
  const [saving, setSaving] = useState(false);
  const [saveError, setSaveError] = useState<string | null>(null);
  const inputRef = useRef<HTMLInputElement>(null);

  useEffect(() => {
    if (id) {
      loadOne(id);
    }
  }, [id, loadOne]);

  useEffect(() => {
    if (character) {
      setNameValue(character.name);
    }
  }, [character]);

  useEffect(() => {
    if (isEditing && inputRef.current) {
      inputRef.current.focus();
      inputRef.current.select();
    }
  }, [isEditing]);

  const handleEdit = () => {
    setSaveError(null);
    setIsEditing(true);
  };

  const handleCancel = () => {
    setNameValue(character?.name ?? "");
    setSaveError(null);
    setIsEditing(false);
  };

  const handleSave = async () => {
    if (!character || nameValue.trim() === "") return;
    setSaving(true);
    setSaveError(null);

    const result = await updateOne(id, { name: nameValue.trim() });

    setSaving(false);
    if (result.success) {
      setIsEditing(false);
    } else {
      setSaveError(result.error ?? "Failed to save");
    }
  };

  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === "Enter") handleSave();
    if (e.key === "Escape") handleCancel();
  };

  if (character === null) {
    return <div className="min-h-screen bg-zinc-950"></div>;
  }

  const status =
    STATUS_CONFIG[character.status as keyof typeof STATUS_CONFIG] ??
    STATUS_CONFIG.Unknown;

  return (
    <div className="min-h-screen bg-zinc-950 pt-24">
      {/* Герой */}
      <div className="relative overflow-hidden">
        {/* Размытый фон */}
        <div
          className="absolute inset-0 bg-center bg-cover scale-110 blur-2xl opacity-20"
          style={{ backgroundImage: `url(${character.image})` }}
        />
        <div className="absolute inset-0 bg-linear-to-b from-transparent via-zinc-950/60 to-zinc-950" />

        {/* Контент героя */}
        <div className="relative px-8 py-12 flex gap-8 items-end">
          <img
            src={character.image}
            alt={character.name}
            className="w-48 h-48 rounded-2xl object-cover shadow-2xl shrink-0 border border-zinc-800"
          />

          <div className="pb-2 flex-1 min-w-0">
            <div className="flex items-center gap-2 mb-3">
              <span className={`w-2.5 h-2.5 rounded-full ${status.dot}`} />
              <span className="font-body text-zinc-400 text-sm">
                {status.label}
              </span>
              <span className="text-zinc-700">·</span>
              <span className="font-body text-zinc-400 text-sm">
                {character.species}
              </span>
            </div>

            {/* Имя + кнопка редактирования */}
            <div className="flex items-start gap-3 mb-4">
              {isEditing ? (
                <input
                  ref={inputRef}
                  value={nameValue}
                  onChange={(e) => setNameValue(e.target.value)}
                  onKeyDown={handleKeyDown}
                  className="font-display text-5xl font-bold text-white leading-tight bg-transparent border-b-2 border-(--rick-morty) outline-none w-full"
                  disabled={saving}
                />
              ) : (
                <h1 className="font-display text-6xl font-bold text-white leading-tight">
                  {character.name}
                </h1>
              )}

              {!isEditing && (
                <button
                  onClick={handleEdit}
                  className="mt-3 p-2 rounded-lg text-zinc-500 hover:text-white hover:bg-zinc-800 transition-colors shrink-0"
                  title="Edit name"
                >
                  <svg
                    className="w-5 h-5"
                    fill="none"
                    viewBox="0 0 24 24"
                    stroke="currentColor"
                    strokeWidth={2}
                  >
                    <path
                      strokeLinecap="round"
                      strokeLinejoin="round"
                      d="M15.232 5.232l3.536 3.536m-2.036-5.036a2.5 2.5 0 113.536 3.536L6.5 21.036H3v-3.572L16.732 3.732z"
                    />
                  </svg>
                </button>
              )}
            </div>

            {/* Кнопки сохранения / ошибка */}
            {isEditing && (
              <div className="flex items-center gap-2 mb-3">
                <button
                  onClick={handleSave}
                  disabled={saving || nameValue.trim() === ""}
                  className="font-body text-sm px-4 py-1.5 rounded-lg bg-(--rick-morty) text-zinc-950 font-semibold hover:opacity-90 disabled:opacity-50 transition-opacity"
                >
                  {saving ? "Saving…" : "Save"}
                </button>
                <button
                  onClick={handleCancel}
                  disabled={saving}
                  className="font-body text-sm px-4 py-1.5 rounded-lg bg-zinc-800 text-zinc-300 hover:bg-zinc-700 disabled:opacity-50 transition-colors"
                >
                  Cancel
                </button>
                {saveError && (
                  <span className="font-body text-sm text-red-400">
                    {saveError}
                  </span>
                )}
              </div>
            )}

            <p className="font-body text-zinc-500 text-sm">
              Added{" "}
              {new Date(character.created_at).toLocaleDateString("en-US", {
                year: "numeric",
                month: "long",
                day: "numeric",
              })}
            </p>
          </div>
        </div>
      </div>

      {/* Детали */}
      <div className="px-8 py-8 space-y-8">
        {/* Инфо сетка */}
        <section>
          <h2 className="font-display text-white font-bold text-xl mb-4">
            Details
          </h2>
          <div className="grid grid-cols-2 sm:grid-cols-4 gap-3">
            <InfoCard label="Gender" value={character.gender} />
            <InfoCard label="Species" value={character.species} />
            <InfoCard label="Type" value={character.type} />
            <InfoCard label="Origin" value={character.origin?.name ?? null} />
          </div>
        </section>

        {/* Локация */}
        <section>
          <h2 className="font-display text-white font-bold text-xl mb-4">
            Last known location
          </h2>
          <Link
            to={`/locations/${character.location.id}`}
            className="bg-zinc-900 rounded-xl p-5 border border-zinc-800 flex items-center gap-4"
          >
            <div className="w-12 h-12 rounded-full bg-zinc-800 flex items-center justify-center shrink-0">
              <span className="text-xl">🌍</span>
            </div>
            <div>
              <p className="font-display text-white font-bold">
                {character.location.name}
              </p>
              <p className="font-body text-zinc-500 text-sm">Planet</p>
            </div>
          </Link>
        </section>

        {/* Эпизоды */}
        <section>
          <h2 className="font-display text-white font-bold text-xl mb-4">
            Episodes
            <span className="font-body text-zinc-500 text-base font-normal ml-2">
              {character.episodes.length}
            </span>
          </h2>
          <div className="flex flex-wrap gap-2">
            {character.episodes.map((episode) => (
              <EpisodeChip key={episode.id} episode={episode} />
            ))}
          </div>
        </section>
      </div>
    </div>
  );
}
