import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

df_reviews = pd.read_csv("datasets/customer reviews.csv")
df_top_100_books = pd.read_csv("datasets/Top-100 Trending Books.csv")

preco_max = df_top_100_books["book price"].max()
preco_min = df_top_100_books["book price"].min()

preco_ate = st.sidebar.slider(
    "Faixa de preço", preco_min, preco_max, preco_max)

df_books = df_top_100_books[df_top_100_books["book price"] <= preco_ate]
st.write(df_books)

# Gráficos
col1, col2 = st.columns(2)
fig = px.bar(df_books["year of publication"].value_counts())
fig2 = px.histogram(df_books["book price"])
col1.plotly_chart(fig)
col2.plotly_chart(fig2)

