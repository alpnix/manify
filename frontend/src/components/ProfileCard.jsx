import React from 'react';

const ProfileCard = ({ imageSrc, name, role, uni }) => {
  return (
    <div className="flex flex-col items-center mx-4">
      <div className="w-48 h-48 rounded-full overflow-hidden mb-4 border-4 border-secondary">
        <img
          src={imageSrc || "/api/placeholder/200/200"} 
          alt={name} 
          className="w-full h-full object-cover"
        />
      </div>
      <h3 className="text-xl font-semibold text-primary">{name}</h3>
      <p className="text-white">{role}</p>
      <i className='text-white'>{uni}</i>
    </div>
  );
};

export default ProfileCard;