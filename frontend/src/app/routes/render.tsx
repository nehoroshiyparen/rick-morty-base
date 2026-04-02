import type { AppRoute } from "./types/AppRoute";

export function renderRoute(route: AppRoute) {
  const Page = route.page;
  const Layout = route.layout ?? (({ children }) => <>{children}</>);

  const element = (
    <Layout>
      <Page />
    </Layout>
  );

  return {
    path: route.path,
    element,
  };
}
