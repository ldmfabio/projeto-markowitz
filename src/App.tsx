import { useState, useEffect } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import Plot from 'react-plotly.js'
import './App.css'

function App() {
  const [data, setData]:any = useState({})

  const fetchData = async () => {
    const response = await fetch('http://localhost:5000/')
    const data = await response.json()
    setData(data)
  }

  useEffect(() => {
    fetchData()
  }, [])

  console.log(data)
  return (
    <>
      <div>
        <Plot
          data={data['data']}
          layout={data['layout']} />
          
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
    </>
  )
}

export default App