import React, { useState } from 'react';
import Navbar from "../components/Navbar";
import UploadButton from "../components/UploadButton";
import Loading from "../components/Loading";
import { File, Trash2, Download } from 'lucide-react';

const Documents = () => {
  console.log("Local storage: " + localStorage.getItem('pastDocuments'))
  const [documents, setDocuments] = useState(localStorage.getItem('pastDocuments') ? JSON.parse(localStorage.getItem('pastDocuments')) : []);
  const handleFileSelect = (file) => {
    const fileURL = URL.createObjectURL(file);
    const newDocuments = [...documents, {
      name: file.name,
      type: file.type,
      url: fileURL
    }];
    localStorage.setItem('pastDocuments', JSON.stringify(newDocuments));
    setDocuments(newDocuments);
  };

  const handleDelete = (index) => {
    const newDocuments = documents.filter((_, i) => i !== index);
    localStorage.setItem('pastDocuments', JSON.stringify(newDocuments));
    setDocuments(newDocuments);
  };

  const handleDownload = (doc) => {
    const link = document.createElement('a');
    link.href = doc.url;
    link.download = doc.name;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  };

  return (
    <div className="min-h-screen">
      <Navbar />

      < Loading />
      
      <div className="container mx-auto px-4 py-12">
        <div className="flex flex-wrap gap-6 items-start justify-center">
          {documents.map((doc, index) => (
            <div key={index} className="flex flex-col items-center">
              <div className="w-48 h-48 border border-gray-300 rounded-lg overflow-hidden">
                <div className="h-full flex flex-col">
                  <div className="flex-1 p-4 flex items-center justify-center">
                    {doc.type.includes('image') ? (
                      <img 
                        src={doc.url} 
                        alt={doc.name}
                        className="w-full h-full object-cover rounded"
                      />
                    ) : (
                      <File className="w-20 h-20 text-gray-400" />
                    )}
                  </div>
                  <div className="bg-gray-50 p-2 border-t border-gray-300">
                    <p className="text-sm text-gray-600 truncate w-full text-center">
                      {doc.name}
                    </p>
                  </div>
                </div>
              </div>
              <div className="flex gap-2 mt-2">
                <button
                  onClick={() => handleDelete(index)}
                  className="flex items-center gap-1 px-3 py-1 bg-red-500 hover:bg-red-600 text-white rounded-md"
                >
                  <Trash2 className="w-4 h-4" />
                </button>
                <button
                  onClick={() => handleDownload(doc)}
                  className="flex items-center gap-1 px-3 py-1 bg-green-500 hover:bg-green-600 text-white rounded-md"
                >
                  <Download className="w-4 h-4" />
                </button>
              </div>
            </div>
          ))}
          
          <UploadButton onFileSelect={handleFileSelect} />
        </div>
      </div>
    </div>
  );
};

export default Documents;