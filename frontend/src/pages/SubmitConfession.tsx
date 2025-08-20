import ConfessionForm from "../components/ConfessionForm";

const SubmitConfession: React.FC = () => {
  return (
    <div className="min-h-screen w-screen bg-gradient-to-br from-red-50 to-red-100 flex items-center justify-center relative overflow-hidden">
      {/* Spotted red dots background */}
      <div className="absolute inset-0 opacity-80">
        {/* Test dot - should be very visible */}
        <div className="absolute top-10 left-10 w-16 h-16 sm:w-32 sm:h-32 bg-blue-600 rounded-full"></div>

        <div className="absolute top-20 left-20 w-12 h-12 sm:w-20 sm:h-20 bg-red-600 rounded-full bg-dot"></div>
        <div className="absolute top-40 right-24 sm:top-64 sm:right-48 w-16 h-16 sm:w-24 sm:h-24 bg-red-700 rounded-full bg-dot"></div>
        <div className="absolute top-60 left-32 sm:top-96 sm:left-64 w-10 h-10 sm:w-16 sm:h-16 bg-red-500 rounded-full bg-dot"></div>
        <div className="absolute top-32 right-40 sm:top-48 sm:right-80 w-12 h-12 sm:w-20 sm:h-20 bg-red-600 rounded-full bg-dot"></div>
        <div className="absolute top-24 left-1/2 sm:top-32 sm:left-1/2 w-12 h-12 sm:w-20 sm:h-20 bg-red-700 rounded-full bg-dot"></div>
        <div className="absolute top-60 right-1/3 sm:top-80 sm:right-1/3 w-16 h-16 sm:w-24 sm:h-24 bg-red-500 rounded-full bg-dot"></div>
        <div className="absolute top-1/2 left-1/4 w-10 h-10 sm:w-16 sm:h-16 bg-red-600 rounded-full bg-dot"></div>
        <div className="absolute top-1/3 right-1/4 w-12 h-12 sm:w-20 sm:h-20 bg-red-700 rounded-full bg-dot"></div>
        <div className="absolute top-2/3 left-3/4 w-12 h-12 sm:w-20 sm:h-20 bg-red-500 rounded-full bg-dot"></div>
        <div className="absolute top-1/6 right-1/2 w-16 h-16 sm:w-24 sm:h-24 bg-red-600 rounded-full bg-dot"></div>
        <div className="absolute top-5/6 left-1/6 w-10 h-10 sm:w-16 sm:h-16 bg-red-700 rounded-full bg-dot"></div>
        <div className="absolute top-1/8 right-1/6 w-12 h-12 sm:w-20 sm:h-20 bg-red-500 rounded-full bg-dot"></div>
        <div className="absolute top-7/8 left-2/3 w-12 h-12 sm:w-20 sm:h-20 bg-red-600 rounded-full bg-dot"></div>
      </div>

      <div className="w-full max-w-7xl mx-auto py-8 sm:py-12 lg:py-16 relative z-10 confession-form-enter px-4">
        <div className="text-center mb-8 sm:mb-12 lg:mb-16">
          <h1 className="text-4xl sm:text-6xl lg:text-8xl font-bold text-red-800 font-comic drop-shadow-2xl confession-form-title tracking-wider leading-tight">
            Confessionsaurus
          </h1>
        </div>
        <div className="flex justify-center confession-form-form w-full">
          <ConfessionForm />
        </div>
      </div>
    </div>
  );
};

export default SubmitConfession;
