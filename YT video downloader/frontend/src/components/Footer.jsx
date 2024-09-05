import React from 'react'

const Footer = () => {
  return (
    <div className='  bg-red-500 flex justify-around p-6 text-white font-semibold'>
      <p  className=' cursor-pointer hover:text-gray-300 transition-all duration-300'>Copyright 2024</p>
      <p className=' cursor-pointer hover:text-gray-300 transition-all duration-300'>Made by Sujit Rao</p>
      <p className=' cursor-pointer' onClick={() => window.location.href = 'mailto:your-sujitrao.it.aec@gmail.com'}>Contact</p>
    </div>
  )
}

export default Footer
