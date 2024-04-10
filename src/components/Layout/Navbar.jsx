import React from 'react';
import { NavList } from './NavList';

/**
 * @component
 * @description React functional component representing the navigation bar of the application.
 * @param {Object} props - The component props.
 * @param {string} props.page_select - The selected page identifier.
 * @returns {React.Component} The Navbar component.
 */
export const Navbar = ({page_select}) => {
    return (
        <div className='w-full flex justify-between bg-transparent items-center'>
            <div className='flex justify-start items-center bg-transparent'>
                <div className='bg-black py-6 px-12 mr-8 text-white rounded-b-xl'>
                    <img src="./logo_test.png" />
                </div>
                <NavList page_select={page_select} />
            </div>
            <div>
                <p className='nav-link' onClick={console.log('Saiu poha')}>
                    Sair
                </p>
            </div>
        </div>
    );
}