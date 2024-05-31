import "./App.css";
import HeroImg from "./assets/heroimg.jpg";
import scrs1 from "./assets/scrs1.jpg";
import scrs2 from "./assets/scrs2.png";
import scrs3 from "./assets/scrs3.png";
import scrs4 from "./assets/scrs4.png";
import githubLogo from "./assets/github.png";
import { Navbar } from "./components/Navbar.jsx";
import { Link } from "react-router-dom";

function App() {
  return (
    <>
      <Navbar />

      <div
        id="hero"
        className="bg-neutral-300 flex flex-row h-[90vh] justify-around items-center"
      >
        <img
          src={HeroImg}
          className="h-60  rounded-full justify-center self-center"
        />
        <div id="content" className="flex flex-col w-100 gap-5">
          <h2 className="text-4xl w-80">
            A minimal approach to your <b>Finances.</b>
          </h2>

          <p className="text-l">
            Help your banking needs relying on FortiFin. With an easy sign up
            and profile setup.
          </p>
          <br />
          <div className="flex flex-row gap-2">
            <Link
              className="bg-zinc-800 w-60 text-slate-200 rounded-md px-[3px] py-2 text-md text-center justify-center"
              to="downloads"
            >
              Download FortiFin
            </Link>
            <a
              className="bg-zinc-800 w-60 text-slate-200 rounded-md px-5 py-2 text-md text-center justify-center"
              href="https://www.slideshare.net/slideshow/fortifin/265076823"
              target="_blank"
            >
              Visit Project File
            </a>
          </div>
          <a
            className="bg-zinc-800 w-80 text-slate-200 rounded-md px-5 py-2 text-md text-center justify-center"
            href="https://youtu.be/JGPFPI0vSEU?si=MvyME8P3RGutDKgN"
            target="_blank"
          >
            View Documentary
          </a>
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
      <br />
      <div id="deal">
        <h2 className="text-2xl p-5 font-bold underline-offset-1">
          What's the actual deal?
        </h2>
        <div id="deal-content" className="w-screen">
          <p className="px-10 py-5 text-md w-[60vw] items-r">
            The project was made as submission to the annual CBSE IP Practical
            Final. Made in <b>Python</b> with heavy focus on <i>Tkinter(Tk)</i>{" "}
            module and with specific efforts to UI, design, file structuring,
            project planning and collaboration. The database for the application
            is <b>MySQL</b>. In the setup program at the github repository,
            FortiFin allows students / teachers who want to work with the
            application to set it up with little to no complications.
          </p>
          <p className="px-10 py-5 text-md w-[60vw]">
            The design for the program was done in Figma. A free to use design
            software, used for both wireframing and UI design. Available both as
            a web application and a desktop app.
          </p>
          <p className="px-10 py-5 text-md w-[60vw]">
            The home directory is divided into 3 sections - assets, views, lib
            and a python file <code>Login.py</code>. Assets folder contains
            images relating to the project, where they're classified by screens
            they're on. The library folder containers functions to help with
            banking aspect of the project. The final folder views, delivers on
            the GUI for the program.
          </p>
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
