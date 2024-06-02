import { Navbar } from "../components/Navbar.jsx";
import LeadImg from "../assets/YJ.png";
import CreativeImg from "../assets/DD.png";
import ThinkerImg from "../assets/AB.jpeg";
import { DevCard } from "../components/Dev.jsx";

export var DevelopersPage = () => {
  return (
    <>
      <Navbar />
      <h2 h1 className="p-10 text-4xl">
        Meet the Dev Team
      </h2>

      <DevCard
        img={LeadImg}
        title="Obsessive Geek"
        role="lead"
        name="Yogesh Jajoria"
      />
      <DevCard
        img={CreativeImg}
        title="Budgeted Nolan"
        role="director"
        name="Deekshant Dhiman"
      />
      <DevCard
        img={ThinkerImg}
        title="The Thinker"
        role="database design"
        name="Aryan Bhatt"
      />
    </>
  );
};
