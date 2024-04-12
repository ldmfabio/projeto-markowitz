
import React, { useState } from 'react'
import { useForm } from 'react-hook-form'
import { GraphSection } from '../components/Tool/GraphSection'
import { FormSection } from '../components/Tool/FormSection'
import { InfoSection } from '../components/Tool/InfoSection'
import { LoadingComponent } from '../components/Misc/LoadingComponent'

/**


*/
const App = () => {
    const { _, handleSubmit } = useForm();
    const onSubmit = (data) => fetchData(data);
    const [data, setData] = useState({})
    const [lowRiskPortifolio, setlowRiskPortifolio ] = useState([])
    const [betterRiskReturnPortifolio, setbetterRiskReturnPortifolio ] = useState([])
    const [ definedRiskPortifolio, setDefinedRiskPortifolio ] = useState([])
    const [ riskFreeAsset, setRiskFreeAsset ] = useState([])
    const baseUrl = 'http://localhost:5000'
    const graphData = data['data']
    const graphLayout = data['layout']

    const [loading, setLoading] = useState(false);
    1
    const fetchData = async (data) => {
        console.log('fez a chamada com os dados:', data)
        const postResponse = await fetch(`${baseUrl}/graph`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: `{
                "start":"2022-01-01",
                "end":"2023-01-01"
            }`
        })
        const postData = await postResponse.json()
        setData(postData[0])
        setlowRiskPortifolio(postData[1])
        setbetterRiskReturnPortifolio(postData[2])
        setDefinedRiskPortifolio(postData[3])
        setRiskFreeAsset(postData[4])

        setLoading(false);
    }

    return (
        <>
            {
                (loading) ? <LoadingComponent /> : <section className='flex w-full gap-10 overflow-hidden'>
                <div>
                    <FormSection handleSubmit={handleSubmit} onSubmit={onSubmit} />
                </div>
                <div className='flex justify-between w-11/12'>
                    <InfoSection lowRiskPortifolio={lowRiskPortifolio} betterRiskReturnPortifolio={betterRiskReturnPortifolio} definedRiskPortifolio={definedRiskPortifolio} riskFreeAsset={riskFreeAsset} />
                    <GraphSection data={graphData} layout={graphLayout} />
                </div>
            </section>
            }
        </>
    )
}

export default App