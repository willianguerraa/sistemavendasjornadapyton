# Passo a passo do projeto
# Passo 1: Criar a tela do sistema
# Passo 2: Criar o formulário de cadastro
    #campo de data
    #cadastrar vendedor
    #campo produto
    #campo quantidade
    #valor
    # botao cadastrar venda
# Passo 3: Salvar a venda na base de dados
# Passo 4: Mostrar a base de dados na tela
# Passo 5: Criar o dashboard com os gráficos
    #card/metrica ->faturamento total
    #grafico de barra/coluna -> venda por vendedor
    #grafico de pizza-> venda por produto

# pip install streamlit pandas plotly
import streamlit as st
import pandas as pd
import plotly.express as px

#carregar a base de vendas
tabela_vendas = pd.read_csv("vendas.csv") 


# Passo 1: Criar a tela do sistema
st.write("# Sistema de Vendas")

#cadastro de vendas

st.sidebar.write("## Cadastrar Vendas")
data = st.sidebar.date_input("Data")
vendedor = st.sidebar.selectbox("Vendedor",["Ana", "Bruno", "Cala" ])
produto = st.sidebar.selectbox("Produto",["Notebook", "Celular", "Fone" ])
quantidade = st.sidebar.number_input("Quantidade", step=1)
valor = st.sidebar.number_input("Valor")
botao_cadastrar = st.sidebar.button("Cadastrar Venda")

#logica de cadastro
if botao_cadastrar:
    nova_venda = [str(data), vendedor, produto, quantidade, valor]
    ultima_linha = len(tabela_vendas) # 124 linhas 
    tabela_vendas.loc[ultima_linha] = nova_venda
    tabela_vendas.to_csv("vendas.csv", index=False)
    st.success("venda cadastrada!")

#visualizar as vendas
st.write("## Vendas Cadastradas")
st.dataframe(tabela_vendas)

#seção de dashboards
st.write("## Dashboard")

faturamento = tabela_vendas["valor"].sum()
st.metric("Faturamento total", f"R$ {faturamento}")

grafico1 = px.bar(tabela_vendas,x="vendedor", y="valor", color="produto")
st.plotly_chart(grafico1)

grafico2 = px.pie(tabela_vendas, names="produto", values="valor", hole=0.5)
st.plotly_chart(grafico2)