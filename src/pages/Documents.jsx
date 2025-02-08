import React, { useState } from 'react';
import Navbar from "../components/Navbar";
import UploadButton from "../components/UploadButton";
import { File } from 'lucide-react';

const Documents = () => {
  const [documents, setDocuments] = useState([]);

  const handleFileSelect = (file) => {
    // Create a URL for the file preview
    const fileURL = URL.createObjectURL(file);
    setDocuments([...documents, {
      name: file.name,
      type: file.type,
      url: fileURL
    }]);
  };

  return (
    <div className="min-h-screen">
      <Navbar />
      
      <div className="container mx-auto px-4 py-12">
        <div className="flex flex-wrap gap-6 items-start justify-center">
          {documents.map((doc, index) => (
            <div 
              key={index}
              className="w-48 h-64 border border-gray-300 rounded-lg p-4 flex flex-col items-center justify-center"
            >
              {doc.type.includes('image') ? (
                <img 
                  src={doc.url} 
                  alt={doc.name}
                  className="w-full h-40 object-cover rounded"
                />
              ) : (
                <File className="w-20 h-20 text-gray-400" />
              )}
              <p className="mt-4 text-sm text-gray-600 truncate w-full text-center">
                {doc.name}
              </p>
            </div>
          ))}
          
          <UploadButton onFileSelect={handleFileSelect} />
        </div>
      </div>
    </div>
  );
};

export default Documents;