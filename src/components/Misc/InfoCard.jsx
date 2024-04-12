import React from 'react';
import '../../App.css';

/**
 * @component
 * @param {Object} props - The component props.
 * @param {string} props.stock - The stock information to display on the card.
 * @returns {React.Component} The InfoCard component.
 */
export const InfoCard = ({ title, data }) => {
    return (
        (Array.isArray(data) ? (
            <div className='mt-5 mtb-5 mr-5 p-8 w-full rounded-3xl bg-white shadow-local'>
                <h1 className='text-black text-lg pb-2 text-left'>{title}</h1>
                <ul>
                    {data.map((item) => (
                        <li className='text-md text-gray-800'>{item}</li>
                    ))}
                </ul>
            </div>
        ) : (
            <div className='mt-5 mtb-5 mr-5 p-8 w-full rounded-3xl bg-white shadow-local'>
                <h1 className='text-black text-lg pb-2 text-left'>{title}</h1>
                <ul>
                    <li className='text-md text-gray-800'>{data}</li>
                </ul>
            </div>
        ))
    );
}