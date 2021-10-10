import Gallery from 'react-photo-gallery';
import './App.css';
import {useDropzone} from 'react-dropzone';
import { useCallback, React, useState, useEffect } from 'react';
import axios from 'axios';

function App() {

  const [photos, setPhotos] = useState([])

  // Get  photos on first render
  useEffect(() => { 
    axios.get("/photos", {})
    .then( res => {
      setPhotos(res.data);
    })
    .catch(error => console.log(error));
  }, []);

  const onDrop = useCallback(acceptedFiles => {
    const data = new FormData();

    // Add each file to form data
    acceptedFiles.forEach((file) => data.append('file', file));
    
    // Post all files
    axios.post("/upload", data, {})
      .then(res => {
        setPhotos(res.data);
      })
      .catch(error => console.log(error));
  }, [])

  const {getRootProps, getInputProps} = useDropzone({onDrop, noClick: true})

  return (
    <div className="App">
      <div {...getRootProps()}>
        {
          photos.length === 0 && <p>No photos in this gallery yet! Drop them here... </p>
        }
        <input {...getInputProps()}/>
        <Gallery photos={photos} />
      </div>
    </div>
  );
}

export default App;
