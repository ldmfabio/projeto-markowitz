import React from 'react';
import Plot from 'react-plotly.js'

/**
 * @component
 * @description React functional component representing a section for displaying a Plotly graph.
 * @param {Object} props - The component props.
 * @param {Object[]} props.data - Array of data objects for the Plotly graph.
 * @param {Object} props.layout - Layout configuration for the Plotly graph.
 * @returns {React.Component} The GraphSection component.
 */
export const GraphSection = ({data, layout}) => {
    return (
        <div className='max-h-96 overflow-hidden ml-auto mr-0 rounded-3xl mt-5 shadow-local'>
          <Plot
            data={data}
            layout={{
              ...layout,
              width: 800,
              height: 400,
              margin: {
                l: 80,
                r: 40,
                b: 80,
                t: 40,
                pad: 0
              }              
            }}
          />
        </div>
    );
}