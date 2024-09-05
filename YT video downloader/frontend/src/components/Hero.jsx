import React, { useState } from 'react'
import axios from 'axios'

const Hero = () => {
  const [videoUrl, setUrl] = useState('')
  const [message, setMessage] = useState('')
  const [downloadLink, setDownloadLink] = useState('')

  const reloadwindow = () => {
    window.location.reload()
  }

  const handleDownload = async () => {
    if (!videoUrl ) {
      setMessage('Please enter a URL')
      return
    }
    console.log(videoUrl)
    try {
      const response = await axios.post('http://127.0.0.1:8000/api/download', null, {
        params: { url: videoUrl },
      });
      setDownloadLink(response.data.download_url);
    } catch (error) {
      console.error('Error fetching download link:', error);
    }

  }


  return (
    <div className=' bg-black h-[80vh] text-white flex flex-col items-center p-24 '>

      <input type="url" placeholder='Link goes here...' className=' px-2 py-4 w-96 rounded-lg text-red-500'
        value={videoUrl}
        onChange={(e) => setUrl(e.target.value)} />
      <button className=' px-3 py-2 bg-red-500 rounded-md text-white mt-7 hover:bg-red-700 focus:bg-red-800 text-xl'
        onClick={handleDownload}>Download</button>

      <p className=' pt-4'>{message}</p>
      {downloadLink && (
        <a href={downloadLink} className='text-blue-500 text-lg'>Click here to download</a>
      )}

      {downloadLink && (
        <p onClick={reloadwindow} className='text-green-500 text-lg cursor-pointer'>Download another video?</p>
      )}

    </div>
  )
}

export default Hero
