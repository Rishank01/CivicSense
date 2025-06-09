// src/components/AboutSection.jsx
import { motion } from "framer-motion";
import FeatureCard from "./FeatureCard";

const features = [
  {
    title: "Simplified Laws",
    description: "We break down complex acts and government policies into easy-to-understand narratives.",
  },
  {
    title: "Visual Campaigns",
    description: "Creative visuals help citizens grasp civic updates quickly and effectively.",
  },
  {
    title: "Real-Time Updates",
    description: "Stay instantly informed about newly passed laws, schemes, and reforms.",
  },
  {
    title: "Awareness for All",
    description: "Content designed for people of all literacy levels and age groups.",
  },
  {
    title: "Reliable Sources",
    description: "All campaigns are based on verified government data and expert interpretation.",
  },
  {
    title: "Civic Engagement",
    description: "Empowering citizens to engage with laws and policies that affect their lives.",
  },
];

const AboutSection = () => {
  return (
    <motion.section
      id="about"
      className="min-h-screen w-full bg-[#0e1a1f] text-white flex flex-col items-center px-4 sm:px-6 md:px-12 py-16"
      initial={{ opacity: 0, y: 100 }}
      whileInView={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.8, ease: "easeOut" }}
      viewport={{ once: true }}
    >
      {/* Headline & Intro */}
      <div className="text-center max-w-4xl mb-12 px-4">
        <h2 className="text-4xl md:text-5xl font-bold text-green-400 mb-4 leading-tight">
          Turning Policies into People’s Stories
        </h2>
        <p className="text-lg md:text-xl text-gray-300">
          CivicSense translates complex government updates into relatable campaigns —
          helping everyone understand what’s new and why it matters.
        </p>
      </div>

      {/* Feature Cards */}
      <div className="flex flex-wrap justify-center gap-6 w-full max-w-7xl">
        {features.map((feature, index) => (
          <FeatureCard
            key={index}
            title={feature.title}
            description={feature.description}
            index={index}
          />
        ))}
      </div>
    </motion.section>
  );
};

export default AboutSection;
