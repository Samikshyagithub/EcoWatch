import "./components/fileup";
import Home from "./pages/Home";
import Tool from "./pages/Tool";
import Suspects from "./pages/Suspects";
import FireDetection from "./pages/Firedetection";
import { createBrowserRouter, RouterProvider } from "react-router-dom";

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
    path: "/suspects",
    element: <Suspects />,
  },
  {
    path: "/Firedetection",
    element: <FireDetection />,
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
