import React from 'react';

/**
 
 */
export const BtnPrimary = ({ content, func }) => {
    return (
        <button 
            type='button' 
            className='bg-blue-600 rounded-3xl w-full py-2 text-white' 
            onClick={() => func()}
        >
            {content}
        </button>
    );
}