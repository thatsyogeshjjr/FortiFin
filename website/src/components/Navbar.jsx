import { Link } from "react-router-dom";
import Logo from "../assets/logo.png";
import { useState } from "react";
import hambergerIcon from "../assets/hambergerIcon.png";

export var Navbar = () => {
  var [showNav, setShowNav] = useState("hidden");

  function toggleNav() {
    setShowNav(showNav === "hidden" ? "" : "hidden");
  }

  return (
    <>
      <div
        id="header"
        className="top-0 w-screen flex flex-row justify-between px-10 py-5 bg-zinc-800 text-slate-200 sticky"
      >
        <div id="menu">
          <img
            src={hambergerIcon}
            alt=""
            className={
              "bg-slate-200 active:bg-slate-500 rounded-full p-2 h-10 sm:hidden"
            }
            onClick={() => toggleNav()}
          />
        </div>
        <div id="logo" className="">
          <img src={Logo} className="h-10" />
        </div>

        <div className="flex">
          <div
            id="nav"
            className={
              "sm:hidden absolute bg-slate-100 text-slate-950 p-10 rounded-md left-10 top-20 w-[80vw] " +
              showNav
            }
          >
            <ul className="flex flex-col gap-10 *:p-4 *:text-lg *:border-2 *:border-solid *:border-black *:rounded-md">
              <Link to="/">
                <li>Home</li>
              </Link>
              <Link to="/dev">
                <li>Developers</li>
              </Link>
              <a
                href="https://github.com/thatsyogeshjjr/FortiFin"
                target="_blank"
              >
                <li>View Code</li>
              </a>
              <Link to="/thanks">
                <li>My Thanks</li>
              </Link>
            </ul>
          </div>
        </div>
        <div
          id="nav"
          className="hidden sm:flex sm:justify-center sm:items-center"
        >
          <ul className="flex flex-row gap-10 justify-center items-center">
            <li>
              <Link to="/">Home</Link>
            </li>
            <li>
              <Link to="/dev">Developers</Link>
            </li>
            <li>
              <a
                href="https://github.com/thatsyogeshjjr/FortiFin"
                target="_blank"
              >
                View Code
              </a>
            </li>
            <li>
              <Link to="/thanks">My Thanks</Link>
            </li>
          </ul>
        </div>
      </div>
    </>
  );
};
