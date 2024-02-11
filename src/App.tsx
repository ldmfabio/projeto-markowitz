import { useState } from 'react'
import Plot from 'react-plotly.js'
import { useForm } from 'react-hook-form'
import './App.css'

function App() {
  const { register, handleSubmit } = useForm();
  const onSubmit = (data:any) => fetchData(data);
  const [data, setData]:any = useState({})
  const [lowRiskPortifolio, setlowRiskPortifolio ] = useState([])
  const [betterRiskReturnPortifolio, setbetterRiskReturnPortifolio ] = useState([])
  const [ definedRiskPortifolio, setDefinedRiskPortifolio ] = useState([])
  const [ riskFreeAsset, setRiskFreeAsset ] = useState([])
  const baseUrl = 'http://localhost:5000'
  const graphData = data['data']
  const graphLayout = data['layout']

  const fetchData = async (data: any) => {
    const postResponse: any = await fetch(`${baseUrl}/graph`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    })
    const postData = await postResponse.json()
    setData(postData[0])
    setlowRiskPortifolio(postData[1])
    setbetterRiskReturnPortifolio(postData[2])
    setDefinedRiskPortifolio(postData[3])
    setRiskFreeAsset(postData[4])
  }

  return (
    <>
      <h1 className="text-3xl font-bold mt-4">
        MKZ Frontier
      </h1>
      <div className='flex justify-center'>
        <div>
          <div className='m-6'>
            <Plot
              data={graphData}
              layout={{
                ...graphLayout,
                width: 1000,
                height: 600,
              
              }}
            />
          </div>

          <div className="bg-white m-6 py-2">
            <form onSubmit={handleSubmit(onSubmit)}>
              <div className='flex justify-start m-5'>
                <div className='m-1'>
                  <label className='text-black'>Data inicial:</label>
                  <input defaultValue={'2022-01-01'} className='rounded bg-gray-600' type="date" {...register("start")} />
                </div>
                
                <div className='m-1'>
                  <label className='text-black'>Data final:</label>
                  <input defaultValue={'2023-01-01'} className='rounded bg-gray-600' type="date" {...register("end")} />
                </div>
              </div>
              <input className='rounded bg-gray-600 p-3' type="submit" value="Submit" />
            </form>
          </div>
        </div>

        <div className="bg-white">
          <div className='text-justify'>
            <div className='m-5'>
              <h1 className='text-black font-bold'>Portfólio de Menor Risco:</h1>
              <ul>
                {lowRiskPortifolio.map((stock: any) => (
                  <li className='text-black' key={stock}>
                    {stock}
                  </li>
                ))}
              </ul>
            </div>
            <div className='m-5'>
              <h1 className='text-black font-bold'>Portfólio de Melhor Relação Risco/Retorno:</h1>
              <ul>
                {betterRiskReturnPortifolio.map((stock: any) => (
                  <li className='text-black' key={stock}>
                    {stock}
                  </li>
                ))}
              </ul>
            </div>
            <div className='m-5'>
              <h1 className='text-black font-bold'>Portifólio com Risco Definido:</h1>
              <ul>
                {definedRiskPortifolio.map((stock: any) => (
                  <li className='text-black' key={stock}>
                    {stock}
                  </li>
                ))}
                <li className='text-black'>
                  {riskFreeAsset}
                </li>
              </ul>
            </div>
          </div>
          
          
        </div>

      </div>
    </>
  )
}

export default App
