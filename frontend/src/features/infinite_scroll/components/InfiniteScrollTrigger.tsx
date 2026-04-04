import { useEffect, useRef } from "react";

type Props = {
  onLoadMore: () => void;
  hasMore: boolean;
};

export function InfiniteScrollTrigger({ onLoadMore, hasMore }: Props) {
  const ref = useRef<HTMLDivElement | null>(null);

  useEffect(() => {
    if (!ref.current || !hasMore) return;

    const observer = new IntersectionObserver((entries) => {
      if (entries[0].isIntersecting) {
        onLoadMore();
      }
    });

    observer.observe(ref.current);

    return () => observer.disconnect();
  }, [hasMore, onLoadMore]);

  return <div ref={ref} className="h-10" />;
}
