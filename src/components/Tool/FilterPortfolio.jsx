import React from 'react';

/**
 * @component
 * @description This component represents a form with three checkboxes.
 * @param {Object} props - The component props.
 * @param {Function} props.onChange - Function to handle checkbox changes and update data.
 * @returns {React.Component} The FilterForm component.
 */
export const FilterPortfolio = ({ onChange }) => {
    const filterOptions = ['Carteira 1', 'Carteira 2', 'Carteira 3'];

    const handleCheckboxChange = (option) => {
        console.log(option)
        // Call the provided callback to handle data changes
        onChange(option);
    };

    return (
        <div className='min-w-48'>
            <h6 className='pb-4'>Carteira de Portifólio</h6>
            <select className="bg-transparent border-blue-600 w-full text-center py-2 text-gray-600 text-base placeholder-gray-600 border-b-2 focus:outline-none focus:ring-0 focus:border-black" name="filterPortfolio" onChange={(e) => handleCheckboxChange(e.target.value)}>
                <option>Selecionar</option>
                {filterOptions.map((option) => (
                    <option value={option}>{option}</option>
                ))}
            </select>
        </div>
    );
};
