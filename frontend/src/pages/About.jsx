import React from 'react';
import Navbar from "../components/Navbar";
import ProfileCard from "../components/ProfileCard";

const About = () => {
  const teamMembers = [
    {
      imageSrc: "https://media.licdn.com/dms/image/v2/D4E03AQEWJrnfzUscSw/profile-displayphoto-shrink_400_400/profile-displayphoto-shrink_400_400/0/1707773722489?e=1744243200&v=beta&t=yvZwr1RVwlZCLGSaSt2oKd_nAuDXKdkXvU-c3zGACDg",
      name: "Akif Dirican",
      role: "Computer Science & Mathematics"
    },
    {
      imageSrc: "https://media.licdn.com/dms/image/v2/D4D03AQGJyhUL3xhJ-A/profile-displayphoto-shrink_400_400/profile-displayphoto-shrink_400_400/0/1693621090014?e=1744243200&v=beta&t=wwVjFRl-IzAkPPgOt-XqXiBQ8MqcX7mJOrKKJpMp7as",
      name: "Alp Niksarli",
      role: "Computer Science & Data Science"
    },
    {
      imageSrc: "https://media.licdn.com/dms/image/v2/D4D03AQE0fsBbhNx1pw/profile-displayphoto-shrink_400_400/profile-displayphoto-shrink_400_400/0/1727795420400?e=1744243200&v=beta&t=W5voMAUNSbFs5tu7u80gX4RBETw-o8QwYuRKEj5BxZ8",
      name: "Utkan Uygur",
      role: "Computer Science & Machine Learning"
    }
  ];

  return (
    <div className="min-h-screen bg-dark">
      <Navbar />
      
      <div className="container mx-auto px-4 py-12">
        <div className="flex flex-wrap justify-center gap-8 mb-16">
          {teamMembers.map((member, index) => (
            <ProfileCard
              key={index}
              imageSrc={member.imageSrc}
              name={member.name}
              role={member.role}
            />
          ))}
        </div>

        <div className="max-w-3xl mx-auto text-center">
          <h2 className="text-3xl font-bold mb-6 text-primary">About Our Platform</h2>
          <p className="text-lg text-white leading-relaxed">
            We are revolutionizing Mathematics tutoring through cutting-edge AI visual creator agent. 
            Our platform specializes in digitalizing Mathematics tutoring by leveraging advanced AI agents 
            that provide comprehensive visual descriptions and explanations. This innovative approach 
            makes complex Mathematicak concepts more accessible and easier to understand for students 
            of all levels. Through interactive visualizations and personalized guidance, we're 
            transforming how students learn and engage with Mathematics.
          </p>
        </div>
      </div>
    </div>
  );
};

export default About;