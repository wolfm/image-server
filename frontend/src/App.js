import Gallery from 'react-photo-gallery'
import './App.css';
import { photos } from './photos'
import {useDropzone} from 'react-dropzone'

function App() {

  const {acceptedFiles, getRootProps, getInputProps} = useDropzone({
    disabled: true
  });

  const files = acceptedFiles.map(file => (
    <li key={file.path}>
      {file.path} - {file.size} bytes
    </li>
  ));
  
  return (
    <div className="App">
      <div className="container">
        <div {...getRootProps({className: 'dropzone'})}>
          <input {...getInputProps()}/>
          <p>Drag and drop files here</p>
        </div>
        <aside>
          <h4>Files</h4>
          <ul>{files}</ul>
        </aside>
      </div>
      <Gallery photos={photos} />
    </div>
  );
}

export default App;
