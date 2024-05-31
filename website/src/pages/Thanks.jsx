import { Navbar } from "../components/Navbar";

export var ThanksPage = () => {
  return (
    <>
      <Navbar />
      <h1 className="text-4xl p-10">A sincere thanks from the lead to</h1>
      <div id="content" className="flex flex-col gap-5 p-10">
        <div className="person">
          <h2 className="text-2xl">Madam Mamta Panwar</h2>
          <p className="text-lg px-5">
            for empowering us to work on this project.{" "}
          </p>
        </div>
        <div className="person">
          <h2 className="text-2xl">Principal Madam Kamna Beri</h2>
          <p className="text-lg px-5">
            for not only allowing us work on this project but also to shoot a
            short film for the same
          </p>
        </div>
        <div className="person">
          <h2 className="text-2xl">Master Dhiman and Master Bhatt</h2>
          <p className="text-lg px-5">
            for working with me and trusting me to lead this amazing team
            forward.
          </p>
        </div>
        <div className="person">
          <h2 className="text-2xl">Master Mandhotra</h2>
          <p className="text-lg px-5">
            for supplying all critical hardware supplies we needed during the
            tenure of the project and aiding in filming.
          </p>
        </div>

        <div className="person">
          <p className="text-4xl text-center p-8 font-bold">
            Thanks for the awesome time.
          </p>
        </div>
      </div>
    </>
  );
};
