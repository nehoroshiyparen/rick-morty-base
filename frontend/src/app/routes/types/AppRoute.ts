export type AppRoute = {
  path: string;
  page: React.ComponentType;
  layout?: React.ComponentType<{ children: React.ReactNode }>;
};
