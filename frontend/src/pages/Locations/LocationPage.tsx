import { CharacterMiniCard } from "@/entities/characters/ui/CharacterMiniCard";
import { useLocations } from "@/entities/locations/hooks/useLocations";
import { useEffect, useRef, useState } from "react";
import { useParams } from "react-router-dom";

export function LocationPage() {
  const params = useParams();
  const id = Number(params.id);

  const { location, loadOne, updateOne } = useLocations();

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
    if (location) {
      setNameValue(location.name);
    }
  }, [location]);

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
    setNameValue(location?.name ?? "");
    setSaveError(null);
    setIsEditing(false);
  };

  const handleSave = async () => {
    if (!location || nameValue.trim() === "") return;
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

  if (location === null) {
    return <div className="min-h-screen bg-zinc-950"></div>;
  }

  return (
    <div className="min-h-screen bg-zinc-950 pt-24">
      {/* Герой */}
      <div className="relative overflow-hidden border-b border-zinc-800">
        <div className="absolute inset-0 bg-linear-to-br from-(--rick-morty)/10 via-transparent to-transparent" />

        <div className="relative px-8 py-14">
          <div className="w-16 h-16 rounded-2xl bg-zinc-900 border border-zinc-800 flex items-center justify-center mb-6">
            <span className="text-3xl">🌍</span>
          </div>

          {/* Имя + кнопка редактирования */}
          <div className="flex items-start gap-3 mb-3">
            {isEditing ? (
              <input
                ref={inputRef}
                value={nameValue}
                onChange={(e) => setNameValue(e.target.value)}
                onKeyDown={handleKeyDown}
                className="font-display text-4xl font-bold text-white bg-transparent border-b-2 border-(--rick-morty) outline-none w-full"
                disabled={saving}
              />
            ) : (
              <h1 className="font-display text-5xl font-bold text-white">
                {location.name}
              </h1>
            )}

            {!isEditing && (
              <button
                onClick={handleEdit}
                className="mt-2 p-2 rounded-lg text-zinc-500 hover:text-white hover:bg-zinc-800 transition-colors shrink-0"
                title="Edit name"
              >
                <svg className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
                  <path strokeLinecap="round" strokeLinejoin="round" d="M15.232 5.232l3.536 3.536m-2.036-5.036a2.5 2.5 0 113.536 3.536L6.5 21.036H3v-3.572L16.732 3.732z" />
                </svg>
              </button>
            )}
          </div>

          {/* Кнопки сохранения / ошибка */}
          {isEditing && (
            <div className="flex items-center gap-2 mb-4">
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
                <span className="font-body text-sm text-red-400">{saveError}</span>
              )}
            </div>
          )}

          <div className="flex items-center gap-4 font-body text-zinc-500 text-sm">
            <span>{location.type}</span>
            <span className="text-zinc-700">·</span>
            <span>{location.dimension}</span>
            <span className="text-zinc-700">·</span>
            <span>
              Added{" "}
              {new Date(location.created_at).toLocaleDateString("en-US", {
                year: "numeric",
                month: "long",
                day: "numeric",
              })}
            </span>
          </div>
        </div>
      </div>

      {/* Детали */}
      <div className="px-8 py-8 space-y-8">
        <section>
          <h2 className="font-display text-white font-bold text-xl mb-4">
            Details
          </h2>
          <div className="grid grid-cols-2 gap-3">
            <div className="bg-zinc-900 rounded-xl p-4 border border-zinc-800">
              <p className="font-body text-zinc-500 text-xs uppercase tracking-widest mb-1">
                Type
              </p>
              <p className="font-display text-white font-bold">
                {location.type}
              </p>
            </div>
            <div className="bg-zinc-900 rounded-xl p-4 border border-zinc-800">
              <p className="font-body text-zinc-500 text-xs uppercase tracking-widest mb-1">
                Dimension
              </p>
              <p className="font-display text-white font-bold">
                {location.dimension}
              </p>
            </div>
          </div>
        </section>

        {/* Жители */}
        <section>
          <h2 className="font-display text-white font-bold text-xl mb-4">
            Residents
            <span className="font-body text-zinc-500 text-base font-normal ml-2">
              {location.characters_location.length}
            </span>
          </h2>

          {location.characters_location.length === 0 ? (
            <p className="font-body text-zinc-600 text-sm">
              No known residents
            </p>
          ) : (
            <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 xl:grid-cols-4 gap-3">
              {location.characters_location.map((character) => (
                <CharacterMiniCard key={character.id} character={character} />
              ))}
            </div>
          )}
        </section>
      </div>
    </div>
  );
}
