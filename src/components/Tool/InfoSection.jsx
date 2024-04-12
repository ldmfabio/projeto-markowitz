import React from 'react';
import { InfoCard } from '../Misc/InfoCard';

/**
 * @component
 * @description React functional component representing an information section for different portfolios.
 * @param {Object} props - The component props.
 * @param {string[]} props.lowRiskPortifolio - Array of stocks in the low-risk portfolio.
 * @param {string[]} props.betterRiskReturnPortifolio - Array of stocks in the portfolio with better risk/return ratio.
 * @param {string[]} props.definedRiskPortifolio - Array of stocks in the portfolio with defined risk.
 * @param {string} props.riskFreeAsset - The risk-free asset information.
 * @returns {React.Component} The InfoSection component.
 */
export const InfoSection = ({ lowRiskPortifolio, betterRiskReturnPortifolio, definedRiskPortifolio, riskFreeAsset }) => {
    
    const datas = [
        {
            title: 'Portfólio de Menor Risco:',
            data: lowRiskPortifolio
        },
        {
            title: 'Portfólio de Melhor Relação Risco/Retorno:',
            data: betterRiskReturnPortifolio
        },
        {
            title: 'Portifólio com Risco Definido:',
            data: definedRiskPortifolio
        },
        {
            title: 'Portifólio com Risco Definido:',
            data: definedRiskPortifolio
        },
        {
            title: 'Ativo Livre de Risco:',
            data: riskFreeAsset
        }
    ]
    
    return (
        <>
            <div className="lg:max-w-xs xl:max-w-11/12">
                <div className='text-justify'>
                    {datas.map((data) => (
                        <InfoCard title={data.title} data={data.data} />
                    ))}
                </div>
            </div>
        </>
    );
}