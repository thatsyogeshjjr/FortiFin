export var DevCard = (props) => {
  return (
    <div className="flex flex-col md:flex-row py-10 px-20 w-screen justify-around">
      <img
        src={props.img}
        className="rounded-full w-max h-max sm:w-60 sm:h-60"
        alt=""
      />
      <div className="sm:hidden h-10" />
      <h1 className="w-[80vw] px-0 sm:px-20 text-2xl sm:text-4xl flex flex-col justify-center items-left">
        <p>
          <b>{props.title}</b> ({props.role})
        </p>
        <br />
        <p className="text-lg sm:text-2xl">{props.name}</p>
      </h1>
    </div>
  );
};
