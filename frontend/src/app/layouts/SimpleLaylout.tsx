import React from "react";
import { Header } from "@/widgets";

type Props = {
  children: React.ReactNode;
};

export function SimpleLayout({ children }: Props) {
  return (
    <>
      <Header />
      {children}
    </>
  );
}
