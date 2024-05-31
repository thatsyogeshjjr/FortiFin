import { Link } from "react-router-dom";

export var NoPage = () => {
  return (
    <>
      <div
        id="content"
        className="h-screen w-screen flex flex-row justify-center items-center"
      >
        <div id="left" className="">
          <h2 className="text-4xl">404 Error</h2>
          <p>Looks like you lost your way here.</p>
          <br />
          <Link
            to="/"
            className="bg-zinc-800 text-slate-200 px-10 p-[10px] rounded-md"
          >
            Take me home
          </Link>
        </div>
      </div>
    </>
  );
};
