import React from "react";
import ConfessionForm from "../components/ConfessionForm";

const SubmitConfession: React.FC = () => {
  return (
    <div className="min-h-screen bg-gray-50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
        <div className="text-center mb-12">
          <h1 className="text-4xl font-bold text-gray-900 mb-4">
            UCalgary Confessions
          </h1>
          <p className="text-xl text-gray-600 max-w-2xl mx-auto">
            Share your thoughts anonymously with the UCalgary community
          </p>
        </div>
        <div className="flex justify-center">
          <ConfessionForm />
        </div>
      </div>
    </div>
  );
};

export default SubmitConfession;
