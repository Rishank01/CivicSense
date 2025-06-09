import { useState } from 'react';
import { FaChevronDown, FaChevronUp } from 'react-icons/fa';

const faqs = [
  {
    question: 'What is CivicSense?',
    answer:
      'CivicSense is a platform that transforms complex government laws, acts, and schemes into simplified, visually appealing campaigns for public awareness.',
  },
  {
    question: 'Who can use CivicSense?',
    answer:
      'Anyone! Whether you’re a student, working professional, policymaker, or concerned citizen — CivicSense helps you stay informed in a meaningful way.',
  },
  {
    question: 'How does it generate content?',
    answer:
      'Our platform uses AI-powered tools and curated research to convert government updates into concise campaigns and narratives.',
  },
  {
    question: 'Is the content verified?',
    answer:
      'Yes, our content goes through review loops and fact-checking to ensure accuracy and reliability.',
  },
  {
    question: 'Can I request a campaign on a specific topic?',
    answer:
      'Absolutely. Users will soon be able to submit requests for campaign topics through our platform.',
  },
//   {
//     question: 'Is CivicSense free to use?',
//     answer:
//       'Yes, the core content will remain free for public access. We may introduce premium features in the future.',
//   },
];

const FaqSection = () => {
  const [openIndex, setOpenIndex] = useState(null);

  const toggleFAQ = (index) => {
    setOpenIndex(openIndex === index ? null : index);
  };

  return (
    <section
      id="faqs"
      className="w-full bg-[#f9fafb] py-16 px-4 sm:px-8 md:px-16"
    >
      <div className="max-w-5xl mx-auto">
        <h2 className="text-4xl font-bold text-center text-gray-800 mb-8">
          Frequently Asked Questions
        </h2>

        <div className="space-y-6">
          {faqs.map((faq, index) => {
            const isOpen = openIndex === index;

            return (
              <div key={index} className="rounded-xl bg-white transition-all duration-300">
                {/* Question Row */}
                <div
                  onClick={() => toggleFAQ(index)}
                  className="flex justify-between items-center p-5 cursor-pointer hover:bg-gray-100 rounded-xl"
                >
                  <h3 className="text-lg md:text-xl font-semibold text-gray-900">
                    {faq.question}
                  </h3>
                  {isOpen ? (
                    <FaChevronUp className="text-blue-600" />
                  ) : (
                    <FaChevronDown className="text-gray-500" />
                  )}
                </div>

                {/* Animated Answer Section */}
                <div
                  className={`overflow-hidden transition-all duration-500 ease-in-out ${
                    isOpen ? 'max-h-[500px] opacity-100' : 'max-h-0 opacity-0'
                  }`}
                >
                  <div className="relative pb-6">
                    {/* Answer Bubble */}
                    <div className="bg-[#2563eb] text-white rounded-2xl p-5 shadow-md mt-3">
                      <p className="text-sm md:text-base leading-relaxed">
                        {faq.answer}
                      </p>
                    </div>
                  </div>
                </div>
              </div>
            );
          })}
        </div>
      </div>
    </section>
  );
};

export default FaqSection;
