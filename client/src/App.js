import { ChakraProvider } from '@chakra-ui/react';
import './App.css';
import { createBrowserRouter, RouterProvider } from "react-router-dom"
import Home from './pages/Home';
import Receitas from './pages/Receitas';

const router = createBrowserRouter([
  {
    path: "/",
    element: <Home />
  },
  {
    path: "/receitas",
    element: <Receitas />
  }
])


function App() {
  return (
    <ChakraProvider>
      <RouterProvider router={router} />
    </ChakraProvider>
  );
}

export default App;
