import { Link } from "react-router-dom";
import Logo from "../assets/logo.png";

export var Navbar = () => {
  return (
    <>
      <div
        id="header"
        className="top-0 w-screen flex flex-row justify-between px-10 py-5 bg-zinc-800 text-slate-200 sticky"
      >
        <div id="logo" className="flex flex-row">
          <img src={Logo} className="h-10" />
        </div>
        <div id="nav" className="flex justify-center items-center">
          <ul className="flex flex-row gap-10 justify-center items-center">
            <li>
              <Link to="/">Home</Link>
            </li>
            <li>
              <a
                href="https://github.com/thatsyogeshjjr/FortiFin"
                target="_blank"
              >
                Downloads
              </a>
            </li>
            <li>
              <Link to="/dev">Developers</Link>
            </li>
            <li>
              <Link to="/about">About</Link>
            </li>
          </ul>
        </div>
      </div>
    </>
  );
};
