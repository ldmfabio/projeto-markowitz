import React, { useState } from 'react';
import { FilterForm } from './FilterForm';
import { BtnPrimary } from '../Misc/BtnPrimary';
import { FilterPortfolio } from './FilterPortfolio';

/**
 * @component
 * @description This component represents a section with form-related elements including checkboxes.
 * @param {Object} props - The component props.
 * @param {Function} props.onSubmit - Function to handle form submission.
 * @returns {React.Component} The FormSection component.
 */
export const FormSection = ({ onSubmit }) => {
    const [data, setData] = useState({});

    const func = (data) => onSubmit(data)

    const handleDateChange = (filterDate) => {
        // Update the data variable when checkbox values change
        setData(filterDate);
    };

    const handlePortfolioChange = (filterPortfolio) => {
        // Update the data variable when checkbox values change
        setData(filterPortfolio);
    };

    return (
        <div className="m-1 flex flex-col gap-4">
            <FilterForm onChange={handleDateChange} />
            <FilterPortfolio onChange={handlePortfolioChange} />
            <BtnPrimary content={'Buscar'} funct={func(data)} />
        </div>
    );
};