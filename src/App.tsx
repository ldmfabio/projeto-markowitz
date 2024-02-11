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
      <h1 className="text-3xl font-bold m-4">
        MKZ Frontier
      </h1>
      <div className='flex justify-center'>
        <div>
          <div className='m-1'>
            <Plot
              data={graphData}
              layout={{
                ...graphLayout,
                width: 1000,
                height: 600,
              
              }}
            />
          </div>

          <div className="bg-white m-1">
            <form onSubmit={handleSubmit(onSubmit)}>
              <div className='flex flex-col p-7'>

                <div className='flex'>
                  <div className='m-4'>
                    <label className='text-black font-bold'>Data inicial: </label>
                    <input defaultValue={'2022-01-01'} className='p-2 rounded bg-black' type="date" {...register("start")} />
                  </div>

                  <div className='m-4'>
                    <label className='text-black font-bold'>Data final: </label>
                    <input defaultValue={'2023-01-01'} className='p-2 rounded bg-black' type="date" {...register("end")} />
                  </div>
                  
                  <div className='m-4'>
                    <label className='text-black font-bold'>Portifólios: </label>
                    <select className='p-2 rounded bg-black' name="select">
                      <option value="port1">Portifólio 1</option>
                      <option value="port2" selected>Portifólio 2</option>
                      <option value="port3">Portifólio 3</option>
                    </select>
                  </div>
                </div>
                <input className='p-3 m-1 rounded bg-black' type="submit" value="Submit" />
              </div>
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
