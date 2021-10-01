import Gallery from 'react-photo-gallery'
import './App.css';
import { photos } from './photos'

function App() {
  
  return (
    <div className="App">
      <Gallery photos={photos} />
    </div>
  );
}

export default App;
