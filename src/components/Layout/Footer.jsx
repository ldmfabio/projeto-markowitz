import React from "react"

/**
 * @component
 * @description React functional component representing a fixed footer with branding information.
 * @returns {React.Component} The Footer component.
 */
export const Footer = () => {
    return (
        <>
            <footer className="w-full text-center py-8 mt-5">
                <p className="text-black font-bold text-base">ModernMKZ</p>
                <p className="text-gray-600 text-sm font-thin pt-2">Desenvolvido por: <a className="text-blue-500" href="https:www.github.com/mateus-lopes" target="_blank" rel="noreferrer">mateus-lopes</a></p>
            </footer>
        </>
    )
}