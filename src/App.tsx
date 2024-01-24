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
        <h1 className="text-3xl font-bold m-4">
          Projeto-Markowitz
        </h1>
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
      <div className="bg-white rounded px-10 pt-10 pb-8 mb-4">
        <form action="http://localhost:5000/graph" method="POST">
          <div className='flex flex-col items-start'>
            <div className='m-2'>
              <label className='text-black' htmlFor="start">Data inicial:</label>
              <input className='rounded bg-gray-600' type="date" id="start" name="start" />
            </div>
            <div className='m-2'>
              <label className='text-black' htmlFor="start">Data final:</label>
              <input className='rounded bg-gray-600' type="date" id="end" name="end" />
            </div>
          </div>
          <input className='rounded bg-gray-600 p-3' type="submit" value="Submit" />
        </form>
      </div>
    </>
  )
}

export default App
