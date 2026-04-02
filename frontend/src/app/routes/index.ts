import { createBrowserRouter } from "react-router-dom";
import { routes } from "./routes";
import { renderRoute } from "./render";

export const router = createBrowserRouter(routes.map(renderRoute));
