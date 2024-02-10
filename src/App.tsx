import { useState, useEffect } from 'react'
import Plot from 'react-plotly.js'
import { useForm } from 'react-hook-form'
import './App.css'

function App() {
  const { register, handleSubmit } = useForm();
  const onSubmit = (data:any) => fetchData(data);
  const [data, setData]:any = useState({})
  const baseUrl = 'http://localhost:5000'

  const fetchData = async (data: any) => {
    const postResponse = await fetch(`${baseUrl}/graph`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    })
    const postData = await postResponse.json()
    setData(postData)
  }

  return (
    <>
      <h1 className="text-3xl font-bold mt-4">
        Projeto-Markowitz
      </h1>
      <div className='flex'>
        <div className="bg-white m-6 py-2">
          <form onSubmit={handleSubmit(onSubmit)}>
            <div className='flex items-start m-3'>
              <div className='m-1'>
                <label className='text-black' htmlFor="start">Data inicial:</label>
                <input defaultValue={'2022-01-01'} className='rounded bg-gray-600' type="date" {...register("start")} />
              </div>
              <div className='m-1'>
                <label className='text-black' htmlFor="start">Data final:</label>
                <input defaultValue={'2023-01-01'} className='rounded bg-gray-600' type="date" {...register("end")} />
              </div>
            </div>
            <input className='rounded bg-gray-600 p-3' type="submit" value="Submit" />
          </form>
        </div>
        <div className='m-6'>
          <Plot
            data={data['data']}
            layout={{ 
                title: "Fronteira Eficiente",
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
      </div>
    </>
  )
}

export default App
