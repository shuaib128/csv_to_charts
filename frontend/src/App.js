import './App.css';
import { BrowserRouter, Route, Routes } from "react-router-dom";

import Home from './page/Home';
import MultipleHome from './page/MultipleHome';

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/multiple" element={<MultipleHome />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
