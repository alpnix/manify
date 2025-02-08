import React, { useState } from 'react';
import { Plus, Upload, Camera, HardDrive } from 'lucide-react';

const UploadButton = ({ onFileSelect }) => {
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [selectedOption, setSelectedOption] = useState(null);

  const handleOptionSelect = (option) => {
    setSelectedOption(option);
    if (option === 'computer') {
      document.getElementById('fileInput').click();
    }
    setIsModalOpen(false);
  };

  const handleFileChange = (e) => {
    const file = e.target.files[0];
    if (file) {
      onFileSelect(file);
    }
  };

  return (
    <div className="relative">
      {/* Plus Button */}
      <div 
        onClick={() => setIsModalOpen(true)}
        className="w-48 h-48 border-2 border-gray-300 rounded-lg flex items-center justify-center cursor-pointer hover:bg-gray-50"
      >
        <Plus className="w-16 h-16 text-gray-400" />
      </div>

      {/* Modal */}
      {isModalOpen && (
        <>
          {/* Backdrop */}
          <div 
            className="fixed inset-0 bg-black bg-opacity-50 z-40"
            onClick={() => setIsModalOpen(false)}
          />
          
          {/* Modal Content */}
          <div className="fixed transform -translate-x-1/2 -translate-y-1/2 top-1/2 left-1/2 bg-white p-4 rounded-lg shadow-lg z-50 min-w-[200px]">
            <div className="flex flex-col gap-4">
              <button
                onClick={() => handleOptionSelect('computer')}
                className="flex items-center gap-2 p-3 rounded-lg hover:bg-gray-100 w-full"
              >
                <Upload className="w-5 h-5" />
                <span>Upload from Computer</span>
              </button>
              <button
                onClick={() => handleOptionSelect('drive')}
                className="flex items-center gap-2 p-3 rounded-lg hover:bg-gray-100 w-full"
              >
                <HardDrive className="w-5 h-5" />
                <span>Upload from Drive</span>
              </button>
              <button
                onClick={() => handleOptionSelect('camera')}
                className="flex items-center gap-2 p-3 rounded-lg hover:bg-gray-100 w-full"
              >
                <Camera className="w-5 h-5" />
                <span>Take Photo</span>
              </button>
            </div>
          </div>
        </>
      )}
      
      <input
        type="file"
        id="fileInput"
        className="hidden"
        onChange={handleFileChange}
        accept="image/*,.pdf,.doc,.docx"
      />
    </div>
  );
};

export default UploadButton;