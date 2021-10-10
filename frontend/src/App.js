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
  }, []);

  const onDrop = useCallback(acceptedFiles => {
    console.log(acceptedFiles);
    const data = new FormData();
    data.append('file', acceptedFiles[0]);
    axios.post("/upload", data, {})
      .then(res => {
        setPhotos(res.data);
      })
      .catch(error => console.log(error));
  }, [])

  const {getRootProps, getInputProps} = useDropzone({onDrop, noClick: true})

  /*
  const {acceptedFiles, getRootProps, getInputProps} = useDropzone({
    disabled: true
  });

  const files = acceptedFiles.map(file => (
    <li key={file.path}>
      {file.path} - {file.size} bytes
    </li>
  ));
  */

  return (
    <div className="App">
      <div {...getRootProps()}>
        {
          photos.length === 0 && <p>Drop the files here ... </p>
        }
        <input {...getInputProps()}/>
        <Gallery photos={photos} />
      </div>
    </div>
  );
}

export default App;
