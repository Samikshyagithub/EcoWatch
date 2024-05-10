import React from 'react'
import { TbTools } from 'react-icons/tb'
import { BiHomeSmile, BiUserVoice, BiMessageSquareError } from 'react-icons/bi'
// import {GiSuspicious} from 'react-icons/gi'
import { GiCctvCamera } from 'react-icons/gi'
import { Outlet, Link } from 'react-router-dom'
import Logo from '../assets/logo3.png'
import ecowatch from '../assets/ecowatch.png'

const Sidebar = () => {
  const pathname = window.location.pathname

  const arr = [
    {
      id: 1,
      name: 'Home',
      link: '/',
      icon: <BiHomeSmile size={27} />,
    },
    {
      id: 2,
      name: 'Garbage Detection',
      link: '/tool',
      icon: <TbTools size={26} />,
    },
{
      id: 2,
      name: 'Fire Detection',
      link: '/Firedetection',
      icon: <TbTools size={26} />,
    },

    {
      id: 3,
      name: 'Suspects',
      link: '/suspects',
      icon: <BiUserVoice size={28} />,
    },
  ]
  return (
    <>
      <div className="flex flex-col justify-between w-full h-full border-gray-300">
        <div>
          <div className='flex items-center'>
            {
              <div><img src={ecowatch} alt="Logo" className='w-15 h-20 mt-5 mb-5 ml-4 border-2 border-black rounded-xl' /></div> 
              }
            <div className='mx-3'><ecowatch size={35} /></div>
            
          
          </div>
          <ul>
            {arr.map(({ id, name, link, icon }) => (
              <Link to={link} key={id}>
                <li className="flex justify-center w-full text-gray-600 cursor-pointer dark:text-gray-300">
                  <div
                    className={`${pathname === link ? 'bg-primary shadow-xl dark:bg-primary-dark text-white hover:text-white dark:hover:text-white' : ''
                      } flex items-center hover:text-primary dark:hover:text-primary-dark my-1 h-12 rounded-full w-56`}
                  >
                    <span className="px-4">{icon}</span>{' '}
                    <span className="mx-4 text-base font-medium">{name}</span>
                  </div>
                </li>
              </Link>
            ))}
          </ul>
        </div>
        <div>
          <div className="flex justify-center w-full px-4 text-gray-600 cursor-pointer">
            
          </div>
        </div>
      </div>
    </>
  )
}

export default Sidebar
