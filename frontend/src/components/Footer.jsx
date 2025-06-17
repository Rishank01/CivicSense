import { FaFacebookF, FaTwitter, FaInstagram, FaLinkedinIn } from 'react-icons/fa';

const Footer = () => {
  return (
    <footer className="w-full bg-black/70 text-white px-4 sm:px-8 md:px-16 pt-14 pb-8 backdrop-blur-md border-t border-white/20">
      <div className="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-4 gap-10 text-sm">
        
        {/* Column 1: Brand */}
        <div className="space-y-4">
          <h2 className="text-3xl font-bold text-green-400">CivicSense</h2>
          <p className="leading-relaxed text-gray-300">
            Simplifying government schemes, policies, and laws into digestible, engaging campaigns for all citizens.
          </p>
          <div className="flex space-x-4 mt-4">
            <a href="#" className="text-lg hover:text-green-400 transition-transform transform hover:scale-130 duration-300"><FaFacebookF /></a>
            <a href="#" className="text-lg hover:text-green-400 transition-transform transform hover:scale-130 duration-300"><FaTwitter /></a>
            <a href="#" className="text-lg hover:text-green-400 transition-transform transform hover:scale-130 duration-300"><FaInstagram /></a>
            <a href="#" className="text-lg hover:text-green-400 transition-transform transform hover:scale-130 duration-300"><FaLinkedinIn /></a>
          </div>
        </div>

        {/* Column 2: Navigation */}
        <div>
          <h3 className="font-semibold text-lg mb-3 text-green-400">Navigation</h3>
          <ul className="space-y-2">
            <li><a href="#home" className="hover:text-green-300">Home</a></li>
            <li><a href="#about" className="hover:text-green-300">About</a></li>
            <li><a href="#faqs" className="hover:text-green-300">FAQs</a></li>
            <li><a href="#contact" className="hover:text-green-300">Contact</a></li>
          </ul>
        </div>

        {/* Column 3: Contact Info */}
        <div>
          <h3 className="font-semibold text-lg mb-3 text-green-400">Contact</h3>
          <ul className="space-y-2 text-gray-300">
            <li><strong>Phone:</strong> +1 (555) 123-4567</li>
            <li><strong>Email:</strong> contact@civicsense.org</li>
            <li><strong>Location:</strong> 123 Civic Street, Awareness City</li>
          </ul>
        </div>

        {/* Column 4: Newsletter */}
        <div>
          <h3 className="font-semibold text-lg mb-3 text-green-400">Stay Updated</h3>
          <p className="text-gray-300 mb-4">Subscribe to our newsletter to stay informed about new campaigns and features.</p>
          <form className="flex flex-col sm:flex-row gap-2">
            <input
              type="email"
              placeholder="Your email"
              className="w-full px-3 py-2 rounded-md text-black focus:outline-none ring-2 ring-white focus:ring-green-400 text-white"
            />
            <button
              type="submit"
              className="bg-green-500 hover:bg-green-600 text-white px-4 py-2 rounded-md font-semibold transition-colors"
            >
              Subscribe
            </button>
          </form>
        </div>
      </div>

      {/* Bottom line */}
      <div className="text-center text-gray-400 text-sm mt-12 border-t border-white/20 pt-4">
        © {new Date().getFullYear()} CivicSense. All rights reserved. | Built with ❤️ by CivicSense Team
      </div>
    </footer>
  );
};

export default Footer;
