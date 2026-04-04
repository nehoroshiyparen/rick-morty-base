import { useState } from "react";

type Props = {
  src: string;
  alt: string;
  className?: string;
  maxRetries?: number;
};

export function ImageWithRetry({
  src,
  alt,
  className,
  maxRetries = 10,
}: Props) {
  const [retryCount, setRetryCount] = useState(0);
  const [imgKey, setImgKey] = useState(0);
  const [failed, setFailed] = useState(false);

  const handleError = () => {
    if (retryCount < maxRetries) {
      const delay = 1500 * (retryCount + 1); // 1.5s, 3s, 4.5s

      setTimeout(() => {
        setRetryCount((c) => c + 1);
        setImgKey((k) => k + 1);
      }, delay);
    } else {
      setFailed(true);
    }
  };

  if (failed) {
    return (
      <div
        className={`${className} bg-zinc-800 flex items-center justify-center`}
      >
        <span className="text-zinc-600 text-xs">No image</span>
      </div>
    );
  }

  return (
    <img
      key={imgKey}
      src={src}
      alt={alt}
      className={className}
      onError={handleError}
    />
  );
}
