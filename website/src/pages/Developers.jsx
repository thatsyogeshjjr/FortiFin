import { Navbar } from "../components/Navbar.jsx";
import LeadImg from "../assets/YJ.png";
import CreativeImg from "../assets/DD.png";
import ThinkerImg from "../assets/AB.jpeg";

export var DevelopersPage = () => {
  return (
    <>
      <Navbar />
      <h2 h1 className="p-10 text-4xl">
        Meet the Dev Team
      </h2>

      <div className="lead flex flex-row py-10 px-20 w-screen justify-around">
        <img src={LeadImg} className="rounded-full w-60 h-60" alt="" />
        <h1 className="px-20 text-4xl flex flex-col justify-center items-left ">
          <p>
            <b>Obsessive Geek</b> (lead)
          </p>
          <br />
          <p className="text-2xl">Yogesh Jajoria</p>
        </h1>
      </div>
      <div className="lead flex flex-row py-10 px-20 justify-around">
        <h1 className="px-20 text-4xl flex flex-col justify-center items-left">
          <p>
            <b>Creature of Creativity</b> (director)
          </p>
          <br />
          <p className="text-xl">Deekshant Dhiman</p>
        </h1>
        <img src={CreativeImg} className="rounded-full w-60 h-60" alt="" />
      </div>
      <div className="lead flex flex-row py-10 px-20 justify-around">
        <img src={ThinkerImg} className="rounded-full w-60 h-60" alt="" />
        <h1 className="px-20 text-4xl flex flex-col justify-center items-left">
          <p className="flex justify-center items-center gap-4">
            <b>The Thinker</b>{" "}
            <p className="text-xl">(wanna blow up a joint? Thats your guy)</p>
          </p>
          <br />
          <p className="text-xl">Aryan Bhatt</p>
        </h1>
      </div>
    </>
  );
};
