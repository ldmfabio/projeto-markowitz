import { useState, useEffect } from 'react'
import Plot from 'react-plotly.js'
import { useForm } from 'react-hook-form'
import './App.css'

function App() {
  const { register, handleSubmit, formState: { errors } } = useForm();
  const onSubmit = (data:any) => console.log(data);
  const [data, setData]:any = useState({})
  const baseUrl = 'http://localhost:5000'

  const fetchData = async () => {
    const response = await fetch(`${baseUrl}/graph`)
    const data = await response.json()
    setData(data)
  }

  useEffect(() => {
    fetchData()
  }, [])

  return (
    <>
      <h1 className="text-3xl font-bold m-4">
        Projeto-Markowitz
      </h1>
      <div className='flex justify-evenly'>
        <div className='m-4'>
          <Plot
            data={data['data']}
            layout={{ 
                title: "Fronteira Eficiente",
                // title position
                titlefont: {
                  size: 20,
                },

                width: 940, 
                height: 580, 
                plot_bgcolor: '#E5ECF6',
                yaxis: {
                  title: "Retorno",
                },
                xaxis: {
                  title: "Risco",
                }
              }}
            
          />
        </div>
        <div className="bg-white rounded p-3">
          <form onSubmit={handleSubmit(onSubmit)}>
            <div className='flex items-start mb-3'>
              <div className='m-1'>
                <label className='text-black' htmlFor="start">Data inicial:</label>
                <input className='rounded bg-gray-600' type="date" {...register("start")}/>
              </div>
              <div className='m-1'>
                <label className='text-black' htmlFor="start">Data final:</label>
                <input className='rounded bg-gray-600' type="date" {...register("end")} />
              </div>
            </div>
            <input className='rounded bg-gray-600 p-3' type="submit" value="Submit" />
          </form>
        </div>
      </div>
    </>
  )
}

export default App
