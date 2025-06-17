import forestImage from '../assets/forest.jpg';
import { RiArrowDownWideFill } from "react-icons/ri";
import AboutSection from '../components/About';
import FaqSection from '../components/FaqSection';
import Contact from '../components/Contact';
import Footer from '../components/Footer';

const Home = () => {
    console.log(forestImage); // Check the import

    return (
        <>
            {/* Anchor for Home */}
            <div id="home"></div>
            {/* Home */}
            <div className="h-screen w-full overflow-hidden">
                {/* Background Image */}
                <div
                    className="inset-0 bg-cover bg-center z-0 h-full"
                    style={{ backgroundImage: `url(${forestImage})` }}
                >

                    {/* 1st Section */}
                    <div className='flex gap-2 inset-0'>
                        {/* Left-Half -> Site Logo */}
                        <div className='flex'>
                            <h1 className='text-white text-2xl p-6 mx-10'><span className='text-pink-700'>C</span>ivicSense</h1>
                        </div>
                        {/* Right Half -> Nav Section */}
                        {/* Right Half -> Nav Section */}
                        <nav className="flex z-20 flex justify-center items-center p-4 w-full text-white">
                            <ul className="flex text-lg font-semibold w-1/2 justify-around rounded-3xl py-2 bg-white/10 backdrop-blur-md border border-white/30 shadow-md">
                                {['Home', 'About', 'FAQs', 'Contact'].map((text) => {
                                    // Use text.toLowerCase() for section ids
                                    const sectionId = text.toLowerCase();

                                    return (
                                        <li
                                            key={text}
                                            className="relative cursor-pointer px-2 overflow-hidden
                                                before:content-[''] before:absolute before:bottom-0 before:left-0
                                                before:h-[2px] before:w-0 before:bg-green-400
                                                before:transition-all before:duration-500 hover:before:w-full"
                                        >
                                            <a href={`#${sectionId}`} className="block py-2">
                                                {text}
                                            </a>
                                        </li>
                                    );
                                })}
                            </ul>
                        </nav>


                        <div className='flex'>
                            <h1 className='text-white text-2xl p-6 mx-10'>CivicSense</h1>
                        </div>

                    </div>


                    {/* Second Section -> Overlay content */}
                    <div className="z-10 flex flex-col items-center h-full text-white text-center px-4 justify-around p-8">
                        <div className=''>
                            <h1 className="text-4xl md:text-6xl font-bold mb-4">Welcome to the Forest</h1>
                            <p className="text-lg md:text-2xl">Experience the wild like never before</p>
                        </div>

                        {/* Button */}
                        <div className=''>
                            <a href="#about">
                                <button className="p-4 rounded-full mx-4 text-white text-5xl animate-bounce cursor-pointer">
                                    <RiArrowDownWideFill />
                                </button>
                            </a>

                        </div>
                    </div>
                </div>
            </div>

            {/* About */}
            <AboutSection/>
            {/* FAQs */}
            <FaqSection/>
            {/* Contact */}
            <Contact/>
            {/* Footer */}
            <Footer/>
        </>
    );
};

export default Home;

