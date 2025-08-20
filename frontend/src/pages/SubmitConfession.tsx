import ConfessionForm from "../components/ConfessionForm";

const SubmitConfession: React.FC = () => {
  return (
    <div className="min-h-screen bg-gradient-to-br from-red-50 to-red-100 flex items-center justify-center relative overflow-hidden">
      {/* Spotted red dots background */}
      <div className="absolute inset-0 opacity-80">
        {/* Test dot - should be very visible */}
        <div className="absolute top-10 left-10 w-32 h-32 bg-blue-600 rounded-full"></div>

        <div className="absolute top-32 left-32 w-20 h-20 bg-red-600 rounded-full bg-dot"></div>
        <div className="absolute top-64 right-48 w-24 h-24 bg-red-700 rounded-full bg-dot"></div>
        <div className="absolute top-96 left-64 w-16 h-16 bg-red-500 rounded-full bg-dot"></div>
        <div className="absolute top-48 right-80 w-20 h-20 bg-red-600 rounded-full bg-dot"></div>
        <div className="absolute top-32 left-1/2 w-20 h-20 bg-red-700 rounded-full bg-dot"></div>
        <div className="absolute top-80 right-1/3 w-24 h-24 bg-red-500 rounded-full bg-dot"></div>
        <div className="absolute top-1/2 left-1/4 w-16 h-16 bg-red-600 rounded-full bg-dot"></div>
        <div className="absolute top-1/3 right-1/4 w-20 h-20 bg-red-700 rounded-full bg-dot"></div>
        <div className="absolute top-2/3 left-3/4 w-20 h-20 bg-red-500 rounded-full bg-dot"></div>
        <div className="absolute top-1/6 right-1/2 w-24 h-24 bg-red-600 rounded-full bg-dot"></div>
        <div className="absolute top-5/6 left-1/6 w-16 h-16 bg-red-700 rounded-full bg-dot"></div>
        <div className="absolute top-1/8 right-1/6 w-20 h-20 bg-red-500 rounded-full bg-dot"></div>
        <div className="absolute top-7/8 left-2/3 w-20 h-20 bg-red-600 rounded-full bg-dot"></div>
      </div>

      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16 relative z-10 confession-form-enter">
        <div className="text-center mb-16">
          <h1 className="text-8xl font-bold text-red-800 mb-8 font-comic drop-shadow-2xl confession-form-title tracking-wider">
            Confessionsaurus
          </h1>
        </div>
        <div className="flex justify-center confession-form-form">
          <ConfessionForm />
        </div>
      </div>
    </div>
  );
};

export default SubmitConfession;
