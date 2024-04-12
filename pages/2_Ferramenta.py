import streamlit as st
from streamlit_authenticator.authenticate.authentication import AuthenticationHandler
import yaml
from yaml.loader import SafeLoader

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.collections import PatchCollection

def main(): 
    st.set_page_config(
        page_title="Home", 
        page_icon="📉", 
        layout="wide", 
        initial_sidebar_state="expanded", 
    )

    # init result
    st.session_state.showResult = False
    # verify user
    if st.session_state.get('authentication_status') != True:
        st.switch_page("0_Usuário.py")
    
    st.title("ModernMKZ")
    st.caption("""<p style='font-size: 1.4em; max-width: 900px'>
        Você pode se perguntar por que um designer optaria por usar o texto lorem ipsum em vez de alguns parágrafos em seu idioma nativo. 
    </p>""", unsafe_allow_html=True)

    col1, col2 = st.columns((1,3))

    with col1:
        # form 
        wallets = [
            {
                'title': 'Wallet 1'
            },
            {
                'title': 'Wallet 2'
            },
        ]

        wallet_titles = [wallet['title'] for wallet in wallets]

        st.write("Carteiras Cadastradas")
        wallet = st.selectbox(
            label="Selecione uma Carteira",
            options=wallet_titles,
            placeholder='Selecione uma Carteira',
            label_visibility='collapsed',
        )

        st.write("Selecione o período de tempo:")
        # Radio buttons para 3 e 5 anos
        time_period = st.radio(
            "Selecione o período de tempo:",
            ('3 anos', '5 anos'),
            label_visibility='collapsed',
        )
        
        if st.button('Fazer Busca', type='primary', use_container_width=True):
            st.session_state.showResult = True

    with col2:
        col1_2, col2_2 = st.columns((1,1))

        with col1_2:
            # Create some sample data
            data = {
                'x': [1, 2, 3, 4, 5],
                'y': [4, 6, 5, 8, 2]
            }

            # Convert the data to a Pandas DataFrame
            df = pd.DataFrame(data)

            # Configure the graph
            fig, ax = plt.subplots()
            ax.plot(df['x'], df['y'])
            ax.set_xlabel('X-Axis')
            ax.set_ylabel('Y-Axis')
            ax.set_title('Exemplo de Gráfico de Linha')

            # Display the graph in Streamlit
            st.pyplot(fig)
        
        with col2_2:
            # Define color codes (you can adjust these to your preference)
            colors = ['red', 'green', 'blue', 'purple', 'orange', 'cyan']


            def generate_color_chart():
                """Generates a color chart figure."""

                # Create a figure and an axis
                fig, ax = plt.subplots()

                # Create rectangular patches for each color
                patches = []
                for i, color in enumerate(colors):
                    rect = plt.Rectangle((i, 0), 1, 1, color=color)
                    patches.append(rect)

                # Add the patches to the axis
                ax.add_collection(PatchCollection(patches))

                # Set labels and limits for the axes
                ax.set_xlabel('Color Index')
                ax.set_ylabel('Color')
                ax.set_xlim(-0.5, len(colors) - 0.5)  # Adjust x-axis limits based on color count
                ax.set_ylim(0, 1)  # Set y-axis limits (0 to 1 for color scale)

                # Set a title for the chart
                ax.set_title('Sample Color Chart')

                # Remove unnecessary elements for a clean chart
                ax.set_xticks([])  # Hide x-axis ticks
                ax.set_yticks([])  # Hide y-axis ticks
                ax.spines['top'].set_visible(False)  # Hide top spine
                ax.spines['right'].set_visible(False)  # Hide right spine

                return fig


            # Display the color chart
            fig = generate_color_chart()
            st.pyplot(fig)

            # Add a text box to potentially allow users to modify color names (optional)
            # color_names = st.text_input("Enter color names (separated by commas)", ", ".join(colors))
            # if color_names:
            #     new_colors = color_names.split(",")
            #     # Update color chart with new names (implementation left as an exercise)



if __name__ == "__main__":
    main()
