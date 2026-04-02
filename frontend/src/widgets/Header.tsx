import { Link } from "react-router-dom";

export function Header() {
  return (
    <div className="w-screen flex justify-center fixed z-10">
      <Link to={"/"}>
        <span className="font-[rick-morty] text-8xl text-(--rick-morty) rick-morty-outline">
          Rick and Morty
        </span>
      </Link>
    </div>
  );
}
