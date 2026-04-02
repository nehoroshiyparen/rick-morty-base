import { APP_ROUTES } from "./config";
import type { AppRoute } from "./types/AppRoute";
import { Home, Characters, Locations, Episodes } from "../../pages";
import { SimpleLayout } from "../layouts";

export const routes: AppRoute[] = [
  {
    path: APP_ROUTES.home,
    page: Home,
    layout: SimpleLayout,
  },
  {
    path: APP_ROUTES.characters,
    page: Characters,
    layout: SimpleLayout,
  },
  {
    path: APP_ROUTES.locations,
    page: Locations,
    layout: SimpleLayout,
  },
  {
    path: APP_ROUTES.episodes,
    page: Episodes,
    layout: SimpleLayout,
  },
];
