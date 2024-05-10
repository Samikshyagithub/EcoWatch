import React, { PureComponent } from 'react';
import { PieChart, Pie, Sector, Cell, ResponsiveContainer } from 'recharts';
import Sidebar from '../components/Sidebar'
import FileWindow from '../components/fileup'
import { VscColorMode, VscOrganization } from 'react-icons/vsc'
import { IoNotifications } from 'react-icons/io5'
import { FaUserCircle, FaInfoCircle } from 'react-icons/fa'
import { RiCloudFill } from 'react-icons/ri'
import HeroImg from '../assets/Hero1.png'
import HeroImg2 from '../assets/Hero2.png'
import fohor from '../assets/fohor.jpg'
import Dadelu from '../assets/Dadelu.jpg'
import River from '../assets/River.png'
import House from '../assets/House.jpg'
import Firefighter from '../assets/Firefighter.png'
import ambulance from '../assets/ambulance.jpg'
import Garbage from '../assets/Garbage.png'

const Home = () => {
  const overviewArr = [
    {
      id: 1,
      name: 'Cities covered',
      number: '3',
      color: '#fc7303',
    },
    {
      id: 2,
      name: 'Partners',
      number: '16',
      color: '#18cf00',
    },
    {
      id: 3,
      name: 'Footages',
      number: '8',
      color: '#0015d5',
    },
    {
      id: 4,
      name: 'Suspects found',
      number: '104',
      color: '#b60000',
    },
  ]
  const data01 = [
    { name: 'Group A', value: 400 },
    { name: 'Group B', value: 300 },
    { name: 'Group C', value: 300 },
    { name: 'Group D', value: 200 },
  ];
  const data02 = [
    { name: 'A1', value: 100 },
    { name: 'A2', value: 300 },
    { name: 'B1', value: 100 },
    { name: 'B2', value: 80 },
    { name: 'B3', value: 40 },
    { name: 'B4', value: 30 },
    { name: 'B5', value: 50 },
    { name: 'C1', value: 100 },
    { name: 'C2', value: 200 },
    { name: 'D1', value: 150 },
    { name: 'D2', value: 50 },
  ];
  return (
    <>
      <div className="flex w-full h-screen">
        <div className="w-[18%]">
          <Sidebar />
        </div>
        <div className="flex flex-col w-[82%]">
          <div className="flex items-center justify-between py-2 px-7">
            
            

          <div className="ml-auto">
        <div className="flex items-center justify-center">
          <button className="p-2 m-2 bg-gray-100 rounded-full dark:bg-black">
            <IoNotifications size={22} />
          </button>
          <button className="p-2 m-2 bg-gray-100 rounded-full dark:bg-black">
            <VscColorMode size={22} />
          </button>
          <button className="p-2 m-2 bg-gray-100 rounded-full dark:bg-black">
            <FaUserCircle size={22} />
          </button>
        </div>
      </div>
    </div>  
          
              <h1 className="px-4 mt-9 ml-6 py-0 text-2xl font-semibold ">
                What are the problems?
              </h1>
              
              < div className="flex flex-col p-4 mt-5 ml-4  shadow-xl rounded-3xl h-[42vh] w-[75vw]">
                <div className="flex">
                <div className="flex items-center flex-col rounded-xl p-5 w-2/3 m-2" style={{ backgroundImage: `url(${Dadelu})`, backgroundSize: 'cover', backgroundPosition: 'center', height: '80%', paddingBottom: '20%' }}>
                 <div className="flex items-start">
                </div>
                  </div>
                  <div className="flex items-center flex-col rounded-xl p-5 w-2/3 m-2" style={{ backgroundImage: `url(${River})`, backgroundSize: 'cover', backgroundPosition: 'center',height: '80%' }}>
                    
                 </div>
                  <div className="flex items-center flex-col rounded-xl p-5 w-2/3 m-2" style={{ backgroundImage: `url(${fohor})`, backgroundSize: 'cover', backgroundPosition: 'center' , height: '80%'}}>
                    
                 </div>
                  <div className="flex items-center flex-col rounded-xl p-5 w-2/3 m-2" style={{ backgroundImage: `url(${House})`, backgroundSize: 'cover', backgroundPosition: 'center', height: '80%' }}>
                    
                 </div>
                </div>
                <div class=" p-4 rounded-3xl h-[70vh] w-[75vw] mr-2 mt-3">
    <div class="grid grid-cols-4 gap-4  text-black">
    <div class = "w-[200px] h-[100px] pl-5">
      <div className="border border-gray-500 border-opacity-50 bg-gray-200 bg-opacity-50 rounded-lg p-4 text-center">
                    <h1 className='text-2x0.5 font-bold text-white'>Fire Detection</h1>
                 </div>
  
    </div>
    <div class = "w-[200px] h-[50px] pl-5 ">
    <div className="border border-gray-500 border-opacity-50 bg-gray-200 bg-opacity-50 rounded-lg p-4 text-center">
                    <h1 className='text-2x0.5 font-bold text-white'>Fire Detection</h1>
                 </div>
    </div>
    <div class = "w-[200px] h-[100px] pl-5">
    <div className="border border-gray-500 border-opacity-50 bg-gray-200 bg-opacity-50 rounded-lg p-4 text-center">
                    <h1 className='text-2x0.5 font-bold text-white'>Fire Detection</h1>
                 </div>
    </div>
    <div class = "w-[200px] h-[100px] pl-5">
      <div className="border border-gray-500 border-opacity-50 bg-gray-200 bg-opacity-50 rounded-lg p-4 text-center">
                    <h1 className='text-2x0.5 font-bold text-white'>Fire Detection</h1>
                 </div>
  
    </div>
  </div>
</div>

             <h1 className="px-4 mt-3 py-0 text-2xl font-semibold">
                What Eco Watch does?
              </h1>
              
              < div className="flex flex-col p-1 mt-4 ml- shadow-xl rounded-3xl h-[40vh] w-[75vw]">
                <div className="flex">
                <div className="flex items-center flex-col rounded-xl p-5 w-2/3 m-2" style={{ backgroundImage: `url(${Firefighter})`, backgroundSize: 'cover', backgroundPosition: 'center', height: '80%', paddingBottom: '20%' }}>
                  </div>
                  <div className="flex items-center flex-col rounded-xl p-5 w-2/3 m-2" style={{ backgroundImage: `url(${ambulance})`, backgroundSize: 'cover', backgroundPosition: 'center',height: '80%',paddingBottom: '20%' }}>
                   
                 </div>
                  < div className="flex items-center flex-col rounded-xl p-5 w-2/3 m-2" style={{ backgroundImage: `url(${Garbage})`, backgroundSize: 'cover', backgroundPosition: 'center' , height: '80%', paddingBottom: '20%' }}>
                   
                 </div>
                  
                </div>
              </div>
              <div class=" p-4 rounded-3xl h-[70vh] w-[75vw] mr-2 mt-3">
  <div class="grid grid-cols-3 gap-4  text-black">
    <div class = "w-[370px] h-[200px]">
    <p class="text-base font-semibold leading-relaxed ml-7 mb-4  text-white text-center">
      <div className="border border-gray-500 border-opacity-50 bg-gray-200 bg-opacity-50 rounded-lg p-4 text-center">
                    <h1 className='text-2x0.5 font-bold text-white'>Fire Detection</h1>
                 </div>
  The machine learning model for fire detection can be run on CCTV footage by providing the video feed as input. The model will analyze the footage and generate alerts when it detects a fire.
</p>
    </div>
    <div class = "w-[370px] h-[200px]">
    <p class="text-base font-semibold leading-relaxed ml-7 mb-4  text-white text-center">
      <div className="border border-gray-500 border-opacity-50 bg-gray-200 bg-opacity-50 rounded-lg p-4 text-center">
                    <h1 className='text-2x0.5 font-bold text-white'>Accident Reporting</h1>
                 </div>
 Users can upload photos of accidents via the Agni Alert web or mobile application. The system processes these images and forwards the reports to the relevant emergency services and local authorities.
</p>
    </div>
    <div class = "w-[350px] h-[200px]">
    <p class="text-base font-semibold leading-relaxed ml-7 mb-4  text-white text-center" >
      <div className="border border-gray-500 border-opacity-50 bg-gray-200 bg-opacity-50 rounded-lg p-4 text-center">
                    <h1 className='text-2x0.5 font-bold text-white'>Trash Detection</h1>
                 </div>
 The trash detection feature operates by analyzing video feeds from CCTV cameras. It identifies instances of unauthorized trash disposal and sends alerts to the appropriate authorities.
</p>
    </div>
  </div>
</div>
               </div>
            </div>
         </div>
        
    </>
  )
}

export default Home
