import { APP_ROUTES } from "./config";
import type { AppRoute } from "./types/AppRoute";
import {
  Home,
  CharactersPage,
  LocationsPage,
  EpisodesPage,
  CharacterPage,
  LocationPage,
  EpisodePage,
} from "@/pages";
import { SimpleLayout } from "../layouts";

export const routes: AppRoute[] = [
  {
    path: APP_ROUTES.home,
    page: Home,
    layout: SimpleLayout,
  },
  {
    path: APP_ROUTES.characters,
    page: CharactersPage,
    layout: SimpleLayout,
  },
  {
    path: APP_ROUTES.locations,
    page: LocationsPage,
    layout: SimpleLayout,
  },
  {
    path: APP_ROUTES.episodes,
    page: EpisodesPage,
    layout: SimpleLayout,
  },
  {
    path: APP_ROUTES.character,
    page: CharacterPage,
    layout: SimpleLayout,
  },
  {
    path: APP_ROUTES.location,
    page: LocationPage,
    layout: SimpleLayout,
  },
  {
    path: APP_ROUTES.episode,
    page: EpisodePage,
    layout: SimpleLayout,
  },
];
