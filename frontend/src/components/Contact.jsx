import contactBg from '../assets/forest.jpg';
const Contact = () => {
  return (
    <section
      id="contact"
      className="w-full py-18 px-4 sm:px-6 md:px-12 lg:px-20"
      style={{
        backgroundImage: `url(${contactBg})`,
        backgroundSize: 'cover',
        backgroundPosition: 'center',
        backgroundRepeat: 'no-repeat',
      }}
    >
      <div className="max-w-6xl mx-auto flex flex-col md:flex-row gap-12 text-white">
        
        {/* Left Column - Contact Details */}
        <div className="md:w-1/2 space-y-6 md:my-auto text-center md:text-left">
          <h2 className="text-3xl sm:text-4xl font-bold drop-shadow-lg">Get in Touch</h2>
          <p className="text-base sm:text-lg leading-relaxed drop-shadow-md max-w-md mx-auto md:mx-0">
            We'd love to hear from you! Whether you have questions, feedback, or want to request a campaign, reach out anytime.
          </p>
          <div className="space-y-4 text-sm sm:text-base drop-shadow-md max-w-md mx-auto md:mx-0">
            <div>
              <h3 className="font-semibold text-lg">Address</h3>
              <p>123 Civic Street, Awareness City, Country</p>
            </div>
            <div>
              <h3 className="font-semibold text-lg">Email</h3>
              <p>contact@civicsense.org</p>
            </div>
            <div>
              <h3 className="font-semibold text-lg">Phone</h3>
              <p>+1 (555) 123-4567</p>
            </div>
          </div>
        </div>

        {/* Right Column - Contact Form */}
        <div className="md:w-1/2 bg-white bg-opacity-90 rounded-xl p-6 sm:p-8 md:p-10 text-gray-900 shadow-lg">
          <form className="flex flex-col gap-5 sm:gap-6">
            <div>
              <label htmlFor="name" className="block mb-1 font-semibold">
                Name
              </label>
              <input
                id="name"
                name="name"
                type="text"
                required
                className="w-full border border-gray-300 rounded-md px-3 py-2 text-sm sm:text-base focus:outline-none focus:ring-2 focus:ring-green-400"
              />
            </div>

            <div>
              <label htmlFor="email" className="block mb-1 font-semibold">
                Email
              </label>
              <input
                id="email"
                name="email"
                type="email"
                required
                className="w-full border border-gray-300 rounded-md px-3 py-2 text-sm sm:text-base focus:outline-none focus:ring-2 focus:ring-green-400"
              />
            </div>

            <div>
              <label htmlFor="message" className="block mb-1 font-semibold">
                Message
              </label>
              <textarea
                id="message"
                name="message"
                rows="4"
                required
                className="w-full border border-gray-300 rounded-md px-3 py-2 text-sm sm:text-base focus:outline-none focus:ring-2 focus:ring-green-400 resize-none"
              />
            </div>

            <button
              type="submit"
              className="bg-green-500 hover:bg-green-600 text-white font-semibold py-3 rounded-md transition duration-300 text-sm sm:text-base"
            >
              Send Message
            </button>
          </form>
        </div>
      </div>
    </section>
  );
};

export default Contact;
