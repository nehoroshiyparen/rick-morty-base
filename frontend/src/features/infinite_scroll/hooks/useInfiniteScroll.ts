import { useCallback, useState } from "react";

type UseInfiniteScrollProps<T> = {
  fetchFn: (limit: number, offset: number) => Promise<T[]>;
  limit: number;
};

export function useInfiniteScroll<T>({
  fetchFn,
  limit,
}: UseInfiniteScrollProps<T>) {
  const [data, setData] = useState<T[]>([]);
  const [offset, setOffset] = useState(0);
  const [isLoading, setIsLoading] = useState(false);
  const [hasMore, setHasMore] = useState(true);

  const loadMore = useCallback(async () => {
    if (isLoading || !hasMore) return;

    setIsLoading(true);

    try {
      const newData = await fetchFn(limit, offset);

      setData((prev) => [...prev, ...newData]);
      setOffset((prev) => prev + limit);

      if (newData.length < limit) {
        setHasMore(false);
      }
    } finally {
      setIsLoading(false);
    }
  }, [fetchFn, offset, limit, isLoading, hasMore]);

  return {
    data,
    loadMore,
    isLoading,
    hasMore,
  };
}
