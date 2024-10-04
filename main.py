import streamlit as st 

st.set_page_config('Download do projeto',layout='centered')

st.title('Download do material')

# Caminho para o arquivo ZIP
zip_file_path = 'Apresentacao_de_Ia-main.zip'

# Criação do botão de download
with open(zip_file_path, 'rb') as f:
    st.download_button(
        label="Baixar arquivo ZIP",
        data=f,
        file_name='Projeto Atual.zip',
        mime='application/zip'
    )