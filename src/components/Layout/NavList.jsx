import React from 'react';

/**
 * @component
 * @description React functional component representing a navigation list for the application.
 * @param {Object} props - The component props.
 * @param {string} props.page_getStyles - The selected page identifier.
 * @returns {React.Component} The NavList component.
 */
export const NavList = ({page_select}) => {
    const getStyles = (page) => {
        return page === page_select ? { color: '#0182FC', borderBottom: '1px solid #0182FC' } : {};
    };

    return (
        <nav>
            <ul className='flex gap-8'>
                <li 
                    style={getStyles('page_app')} className='nav-link'
                >
                    <a href="/">
                        Ferramenta
                    </a>
                </li>
                <li 
                    style={getStyles('page_portfolios')} className='nav-link'
                >
                    <a href="portifolios">
                        Portifólios
                    </a>
                </li>
                <li 
                style={getStyles('page_historico')} className='nav-link'
                >
                    <a href="history">
                        Histórico   
                    </a>
                </li>
            </ul>
        </nav>
    );
}