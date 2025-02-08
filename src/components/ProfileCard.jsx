import React from 'react';

const ProfileCard = ({ imageSrc, name, role }) => {
  return (
    <div className="flex flex-col items-center mx-4">
      <div className="w-48 h-48 rounded-full overflow-hidden mb-4 border-4 border-black">
        <img 
          src={imageSrc || "/api/placeholder/200/200"} 
          alt={name} 
          className="w-full h-full object-cover"
        />
      </div>
      <h3 className="text-xl font-semibold text-gray-800">{name}</h3>
      <p className="text-gray-600">{role}</p>
    </div>
  );
};

export default ProfileCard;