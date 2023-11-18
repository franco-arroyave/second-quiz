import Link from "next/link";

export default function Dashboard() {
  return (
    <ul>
      <li>
        <Link href="/">
          Home
        </Link>
      </li>
      <li>
        <Link href="/querties">
          Querties
        </Link>
      </li>
      <li>
        <Link href="/user/123">
          User
        </Link>
      </li>
    </ul>
  );
}