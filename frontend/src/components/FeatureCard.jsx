// src/components/FeatureCard.jsx
import { motion } from "framer-motion";

const FeatureCard = ({ title, description, index }) => {
  return (
    <motion.div
      className="bg-white/10 border border-white/20 backdrop-blur-md shadow-lg rounded-xl p-6 w-full sm:w-[45%] lg:w-[30%] hover:scale-105 transition-transform duration-300"
      initial={{ opacity: 0, y: 50 }}
      whileInView={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.5, delay: index * 0.1 }}
      viewport={{ once: true }}
    >
      <h3 className="text-xl font-semibold text-green-300 mb-2">{title}</h3>
      <p className="text-gray-300 text-sm">{description}</p>
    </motion.div>
  );
};

export default FeatureCard;
