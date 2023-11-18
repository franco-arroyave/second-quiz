import { useRouter } from "next/router";

export default function Post() {
  const router = useRouter();
  const { user } = router.query;
  return (
    <div>
      <p>Post: { user }</p>
    </div>
  );
}