import React from 'react';

/**
 * @component
 * @description This component represents a form with three checkboxes.
 * @param {Object} props - The component props.
 * @param {Function} props.onChange - Function to handle checkbox changes and update data.
 * @returns {React.Component} The FilterForm component.
 */
export const FilterForm = ({ onChange }) => {
    const filterOptions = ['Só no ano passado', 'Ultimos 3 anos', 'Ultimos 5 anos'];

    const handleCheckboxChange = (option) => {
        console.log(option)
        // Call the provided callback to handle data changes
        onChange(option);
    };

    return (
        <div className='min-w-48 mt-16'>
            <h6 className='pb-1.5'>Data Inicial</h6>
           {filterOptions.map((option, index) => (
                <li className='list-none' key={index}>
                    <label className='flex text-gray-500 text-sm'>
                        <input
                        type="radio"
                        name="answer"
                        value={option}
                        className='w-5'
                        onChange={() => handleCheckboxChange(option)}
                        />
                        <p className='p-2'>{option}</p>
                    </label>
                </li>
            ))}
        </div>
    );
};
