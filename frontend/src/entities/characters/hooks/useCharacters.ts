import { useCallback, useEffect, useRef, useState } from "react";
import type { CharacterPreview } from "../types/CharacterPreview";
import { getList } from "../api/getList";
import { getOne } from "../api/getOne";
import { update } from "../api/update";
import type { CharacterFull } from "../types/CharacterFull";

export const useCharacters = (limit = 10) => {
  const [characters, setCharacters] = useState<CharacterPreview[]>([]);
  const [character, setCharacter] = useState<CharacterFull | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [hasMore, setHasMore] = useState(true);

  const offsetRef = useRef(0);
  const loadingRef = useRef(false);
  const hasMoreRef = useRef(true);

  const loadOne = async (id: number) => {
    setLoading(true);
    setError(null);

    const response = await getOne(id);

    if (response.success) {
      setCharacter(response.data);
    } else {
      setError(response.error);
    }

    setLoading(false);
  };

  const updateOne = async (id: number, data: { name: string }) => {
    const response = await update(id, data);

    if (response.success) {
      setCharacter(response.data);
      return { success: true as const };
    } else {
      return { success: false as const, error: response.error };
    }
  };

  const loadMore = useCallback(async () => {
    if (loadingRef.current || !hasMoreRef.current) return;

    loadingRef.current = true;
    setLoading(true);
    setError(null);

    const response = await getList(limit, offsetRef.current);

    if (response.success) {
      setCharacters((prev) => [...prev, ...response.data]);
      offsetRef.current += limit;

      if (response.data.length < limit) {
        hasMoreRef.current = false;
        setHasMore(false);
      }
    } else {
      setError(response.error);
    }

    loadingRef.current = false;
    setLoading(false);
  }, [limit]);

  useEffect(() => {
    loadMore();
  }, [loadMore]);

  return { character, characters, loading, error, hasMore, loadMore, loadOne, updateOne };
};
