import "./components/fileup";
import Home from "./pages/Home";
import Tool from "./pages/Tool";
import Suspects from "./pages/suspects";
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import FireDetection from "./pages/Firedetection";
import Firesuspect from "./pages/Firesuspect";


const router = createBrowserRouter([
  {
    path: "/",
    element: <Home />,
  },
  {
    path: "/tool",
    element: <Tool />,
  },
  {
    path: "/Firedetection",
    element: <FireDetection />,
  },
  {
    path: "/suspects",
    element: <Suspects />,
  },
  {
    path: "/Firesuspect",
    element: <Firesuspect />,
  },
]);

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <RouterProvider router={router} />
      </header>
    </div>
  );
}

export default App;
