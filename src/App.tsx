import { useState, useEffect } from 'react'
import Plot from 'react-plotly.js'
import './App.css'

function App() {
  const [data, setData]:any = useState({})

  const fetchData = async () => {
    const response = await fetch('http://localhost:5000/graph')
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
          layout={{ 
            title: "Fronteira Eficiente", 
            width: 1200, 
            height: 700, 
            plot_bgcolor: '#E5ECF6',
            yaxis: {
              title: "Retorno",
            },
            xaxis: {
              title: "Risco",
            }
            
            }} />
          
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
    </>
  )
}

export default App
