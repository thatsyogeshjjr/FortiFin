import "./App.css";
import Logo from "./assets/logo.png";
import HeroImg from "./assets/heroimg.jpg";
import scrs1 from "./assets/scrs1.jpg";
import scrs2 from "./assets/scrs2.png";
import scrs3 from "./assets/scrs3.png";
import scrs4 from "./assets/scrs4.png";
import githubLogo from "./assets/github.png";

function App() {
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
            <li>Home</li>
            <li>Downloads</li>
            <li>Developers</li>
            <li>About</li>
          </ul>
        </div>
      </div>
      <div
        id="hero"
        className="bg-neutral-300 flex flex-row h-[90vh] justify-around items-center"
      >
        <img
          src={HeroImg}
          className="h-60  rounded-full justify-center self-center"
        />
        <div id="content" className="flex flex-col w-80 gap-5">
          <h2 className="text-4xl">
            A minimal approach to your <b>Finances.</b>
          </h2>
          <p className="text-l">
            Help your banking needs relying on FortiFin. With an easy sign up
            and profile setup.
          </p>
          <br />
          <button className="bg-zinc-800 w-60 text-slate-200 rounded-md px-5 py-2 text-md">
            Download FortiFin
          </button>
        </div>
      </div>
      <div id="screenshots" className="">
        <h2 className="text-2xl p-5 font-bold underline-offset-1">
          Screenshots
        </h2>
        <div
          id="images"
          className="flex flex-row gap-20 p-5 overflow-scroll no-scrollbar h-80"
        >
          <img src={scrs1} alt="" />
          <img src={scrs2} alt="" />
          <img src={scrs3} alt="" />
          <img src={scrs4} alt="" />
        </div>
      </div>
      <div id="footer" className="bg-zinc-800 p-10 bottom-0">
        <a href="https://github.com/thatsyogeshjjr/FortiFin" target="_blank">
          <img src={githubLogo} alt="" className="h-10" />
        </a>
      </div>
    </>
  );
}

export default App;
