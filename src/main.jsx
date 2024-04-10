import React from 'react'
import ReactDOM from 'react-dom/client'
import Layout from './routes/Layout.jsx'
import App from './routes/App.jsx'
import Portifolios from './routes/Portifolios.jsx'
import History from './routes/History.jsx'
import './App.css'
import './index.css'
import { createBrowserRouter, RouterProvider } from 'react-router-dom'
import ErrorPage from './routes/ErrorPage.jsx'

const router = createBrowserRouter([
  { 
    path: '/', 
    element: <Layout />, 
    errorElement: <ErrorPage />,
    children: [
      { path: '/', element: <App />},
      { path: '/portifolios', element: <Portifolios /> },
      { path: '/history', element: <History /> }
    ]
  },
])

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>
)
