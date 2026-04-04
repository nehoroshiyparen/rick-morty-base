import type { LocationPreview } from "@/entities/locations/types/LocationPreview";
import { LocationCard } from "@/entities/locations/ui/LocationCard";

type Props = {
  locations: LocationPreview[];
};

export function LocationFeed({ locations }: Props) {
  if (locations.length === 0) {
    return (
      <div className="flex flex-col items-center justify-center py-40 text-zinc-600">
        <span className="text-6xl mb-4">🪐</span>
        <p className="font-body text-lg">No locations found</p>
      </div>
    );
  }

  return (
    <div className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 xl:grid-cols-5 gap-4">
      {locations.map((location) => (
        <LocationCard key={location.id} location={location} />
      ))}
    </div>
  );
}
