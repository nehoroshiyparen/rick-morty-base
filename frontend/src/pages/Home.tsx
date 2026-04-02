import { Link } from "react-router-dom";

const panels = [
  {
    title: "Characters",
    subtitle: "Explore the universe",
    image: "/characters.jpg",
    url: "/characters",
  },
  {
    title: "Locations",
    subtitle: "Discover places",
    image: "/locations.jpg",
    url: "/locations",
  },
  {
    title: "Episodes",
    subtitle: "Watch the story",
    image: "/episodes.jpg",
    url: "/episodes",
  },
];

export function Home() {
  return (
    <div className="w-screen h-screen flex bg-black gap-0.5">
      {panels.map((panel) => (
        <Link
          to={panel.url}
          key={panel.title}
          className="group relative h-full flex-1 overflow-hidden cursor-pointer"
        >
          {/* Картинка */}
          <div
            className="absolute inset-0 bg-center bg-cover transition-transform duration-700 ease-out group-hover:scale-110"
            style={{ backgroundImage: `url(${panel.image})` }}
          />

          {/* Постоянный градиент снизу */}
          <div className="absolute inset-0 bg-linear-to-t from-black/80 via-black/10 to-transparent" />

          {/* Затемнение на ховер */}
          <div className="absolute inset-0 bg-black/0 group-hover:bg-black/40 transition-colors duration-500" />

          {/* Контент */}
          <div className="relative z-10 h-full flex flex-col justify-end p-8">
            <h1 className="text-5xl font-bold text-white mb-2 translate-y-1 group-hover:translate-y-0 transition-transform duration-300">
              {panel.title}
            </h1>

            <p className="text-white/60 text-sm opacity-0 group-hover:opacity-100 translate-y-3 group-hover:translate-y-0 transition-all duration-300 delay-75">
              {panel.subtitle}
            </p>

            <div className="mt-3 opacity-0 group-hover:opacity-100 translate-y-3 group-hover:translate-y-0 transition-all duration-300 delay-100">
              <span className="text-(--rick-morty) text-sm font-semibold tracking-widest uppercase">
                Explore →
              </span>
            </div>
          </div>
        </Link>
      ))}
    </div>
  );
}
