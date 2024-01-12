import { useState, useEffect } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import Plot from 'react-plotly.js'
import './App.css'

function App() {
  const [data, setData] = useState({})

  // fetch data from http://127.0.0.1:5000/
  const getData = async () => {
    const response = await fetch('http://localhost:5000/').then(res => res.json())
    setData(response)
  }

  useEffect(() => {
    getData()
  });

  console.log(data)

  return (
    <>
      <div>
        <Plot
          data={[
            {
              x: [1, 2, 3],
              y: [2, 6, 3],
              type: 'scatter',
              mode: 'lines+markers',
              marker: { color: 'red' },
            },
            { type: 'bar', x: [1, 2, 3], y: [2, 5, 3] },
          ]}
          layout={{ width: 920, height: 540, title: 'A Fancy Plot' }} />
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
    </>
  )
}

export default App
