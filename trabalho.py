import streamlit as st
import requests

st.title('Consulte um DDD')

ddd = st.text_input('Digite o DDD desejado: ')

if ddd:
    url = f'https://brasilapi.com.br/api/ddd/v1/{ddd}'
    resposta = requests.get(url)

    if resposta.status_code == 200:
        json_resposta = resposta.json()
        estado = json_resposta['state']
        cidades = json_resposta['cities']

        st.write(f'**Estado:** {estado}')
        st.write('**Cidades:**')
        for cidade in cidades:
            st.write(f'- {cidade}')
    else:
        st.error('DDD não encontrado. Verifique se o número está correto.')
