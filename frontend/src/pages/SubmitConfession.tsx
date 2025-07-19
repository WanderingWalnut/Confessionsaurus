import ConfessionForm from "../components/ConfessionForm";

const SubmitConfession: React.FC = () => {
  return (
    <div className="min-h-screen bg-gradient-to-br from-red-50 to-red-100 flex items-center justify-center">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
        <div className="text-center mb-12">
          <h1 className="text-6xl font-bold text-red-800 mb-4 font-comic">
            <span className="dino-emoji"></span> Confessionsaurus{" "}
            <span className="dino-emoji"></span>
          </h1>
          <p className="text-xl text-red-700 max-w-2xl mx-auto font-medium">
            Share your prehistoric thoughts anonymously with the UCalgary
            community
          </p>
          <div className="mt-4 text-red-600 text-lg">
            <span className="dino-emoji"></span> Rawr! Your secrets are safe
            with us! <span className="dino-emoji">🦖</span>
          </div>
        </div>
        <div className="flex justify-center">
          <ConfessionForm />
        </div>
      </div>
    </div>
  );
};

export default SubmitConfession;
