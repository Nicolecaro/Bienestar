import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import geopandas as gpd

dw = pd.read_csv('dataframe1.csv')
dw1 = gpd.read_file('countries.geo.json')
dw2 = gpd.read_file('dataframe2.geojson')

st.set_page_config(layout='wide')
st.title("Bienestar en América")

st.subheader('Países analizados')

for year in dw2['año'].unique():
    fig, ax = plt.subplots(1, 1)
    subset = dw2[dw2['año'] == year]
    subset.plot(ax=ax, label=str(year))
    plt.axis('off')
    plt.show()
st.pyplot(fig)

st.text("Para llevar a cabo el estudio sobre el Bienestar de la población en América, se tomaron")
st.text("quince países los cuales fueron: Colombia, Argentina, Bolivia, Brasil, Canada, Chile,") 
st.text("Costa Rica, Ecuador, Mexico, Paraguay, Uruguay, Peru y Estados Unidos.")


st.subheader('Descripción de datos')

st.dataframe(dw.head())

st.text("Para llevar a cabo el estudio se tomaron cinco variables que pueden influir en el")
st.text("bienestar de la población, las cuales fueron el crecimiento de la población, el")
st.text("PIB per cápita, tasa de desempleo, la expectativa de vida y el acceso a la electricidad.")
st.text("Estas variables serán analizadas desde el año 2002 hasta el 2019.")

tab1, tab2, tab3, tab4, tab5 = st.tabs(['Análisis estadístico', 'Análisis gráfico', 'Análisis de hipótesis', 'Evolución de las variables', 'Creado por:'])

with tab1:

    st.dataframe(dw.describe())

    t= """
    La media de cada una de las variables teniendo en cuenta los datos que se van a analizar,
    reflejan el desempeño de cada variable escogida para el estudio en la región a lo 
    largo del tiempo. La tasa  promedio de crecimiento de la población fue de 1.106%, 
    la tasa promedio de desempleo es de 6.87%, el ingreso per cápita promedio fue
    de $13,292 dólares, pasando a la expectativa promedio de vida que fue de 75 años, mientras 
    que el acceso promedio a la electricidad por porcentaje de la población fue de 96.77%.   
    """
    st.text(t)


    resumen = {}

    resumen['Medias crecimiento de la población'] = dw.groupby(['pais']).agg({'c.poblacion':'mean'})
    resumen['Medias PIB per capita'] = dw.groupby(['pais']).agg({'pibpc':'mean'})
    resumen['Medias desempleo'] = dw.groupby(['pais']).agg({'desempleo':'mean'})
    resumen['Medias expectativa de vida'] = dw.groupby(['pais']).agg({'expect.vida':'mean'})
    resumen['Medias acceso a electricidad'] = dw.groupby(['pais']).agg({'acc.electricidad':'mean'})
    num_tables = len(resumen)
    num_columns = 5
    num_rows = (num_tables + num_columns - 1) // num_columns
    for i in range(num_rows):
        cols = st.columns(num_columns)
        for j in range(num_columns):
            index = i * num_columns + j
            if index < num_tables:
                titulo, serie = list(resumen.items())[index]
                with cols[j]:
                    st.subheader(f"{titulo}")
                    st.dataframe(serie.reset_index()) 

with tab2:
    fig, ax=plt.subplots(1,1)
    fig = px.line(dw, x="año", y="pibpc", color="pais",markers=True, title="Evolución del ingreso per capita")
    fig.update_traces(textposition="bottom right")
    fig.show()
    st.plotly_chart(fig)

    t="""
    Se evidencia que hay una gran diferencia entre los países de sir américa y norteamérica, en el año 2002 el 
    país con el mayor pib per capita fue México con un poco más de 7 mil millones de dólares, mientras que para
    el mismo año en Estados Unidos el pib per capita fue de casi 40 mil millones, otro aspecto interesante es la
    evolución a lo largo de casi 2 décadas, mientras que para el 2019 el pib per capita en Estados Unidos fue de 
    65 mil millones (un aumento de 15 mil millones a lo largo de los 18 años) para el caso de América del sur , 
    México aumento su pib per capita hasta los 10 mil millones, otro dato interesante para observar son los de Uruguay,
    en el 2002 el pib per capita fue de 4 mil millones y para el 2019 el pip fue de casi 18 millones un aumento 
    similar al que obtuvo Estados Unidos
    """
    st.text(t)

    fig, ax=plt.subplots(1,1)
    fig = px.line(dw, x="año", y="expect.vida", color="pais",markers=True, title="Evolución de la expectativa de vida")
    fig.update_traces(textposition="bottom right")
    fig.show()
    st.plotly_chart(fig)

    t="""
    En general se observa que todos los países tiene un aumento contante en la expectativa de vida de las personas, el 
    país que llama la atención es Venezuela, es el único que apartir del año 2013  empezó a a caer la expectativa de vida.
    """
    st.text(t)

    fig, ax=plt.subplots(1,1)
    fig = px.line(dw, x="año", y="desempleo", color="pais",markers=True, title="Evolución del desempleo")
    fig.update_traces(textposition="bottom right")
    fig.show()
    st.plotly_chart(fig)

    t="""
    Con respecto al desempleo la gráfica muestra que para el caso de argentina que tenía un desempleo de 20% en el años 2002
    pasó a tener en el 2019 un 10 % y para el caso de Venezuela, en el  2002 era del 16% y para el 2019 bajo hasta un 5 %. 
    En el periodo del 2008 y 2009 estados unidos llego a su pico de desempleo con casi 10% , pero logro reducir ese porcentaje 
    hasta llegar a los 3.6% en el 2019.
    """
    st.text(t)

    fig, ax=plt.subplots(1,1)
    fig = px.line(dw, x="año", y="c.poblacion", color="pais",markers=True, title="Crecimiento de la población")
    fig.update_traces(textposition="bottom right")
    fig.show()
    st.plotly_chart(fig)

    t="""
    El pais a destacar es Venezuela, este debido a que desde el 2015 bajo casi 3 puntos en el crecimiento de la población, 
    y para ese mismi periodo de tiempo empezó la población a salir del país en grandes cantidades.
    """
    st.text(t)

    fig, ax=plt.subplots(1,1)
    fig = px.bar(dw, x='año', y=['pibpc'],
             color='pais',
             labels={'pibpc':'PIBpc'},
             height=400)

    fig.update_layout(title_text='PIB per capita a lo largo del tiempo')
    fig.show()
    st.plotly_chart(fig)

    t="""
    Se evidencia que la mayor parte del Pib per capita es de Estados 
    Unidos y Canadá representando casi un 40% del Pib per Capita de todos los países 
    """
    st.text(t)

    fig, ax=plt.subplots(1,1)
    fig = px.scatter(dw2, x="año", y="acc.electricidad", color="continente",size='acc.electricidad', hover_data=['pais'])
    fig.show()
    st.plotly_chart(fig)

    t="""
    Para el caso de América del sur, estos países tiene un acceso a la electricidad 
    mayor a 97% a lo largo de las 2 décadas. Para el caso de América del sur  en el 
    año 2002, para bolivia el acceso a la electricidad era de 64% y para Perú de 74%, 
    los más bajos de toda la región,pero en el transcurso de las 2 décadas estos países 
    lograron aumentar su acceso a la electricidad hasta llegar al 95% para el año 2019.
    """
    st.text(t)

with tab3:

    st.subheader('Variable #1: expectativa de vida')
    latex_formula = r"H_0: \text{No hay diferencia significativa de la expectativa de vida entre Colombia y Norteamerica}"
    latex_formula += r", \\ H_1: \text{Existe una diferencia significativa de la expectativa de vida entre Colombia y Norteamerica}"
    st.latex(latex_formula)
    texto_simple = """
    Se realizó la prueba de hipótesis por año y en las 17 pruebas se obtuvo un valor p value menor 
    a 0.05, por lo que se rechaza la hipótesis nula. Con esto se puede decir que no hay evidencia suficiente para afirmar una diferencia significativa.'
    """
    st.text(texto_simple)

    st.subheader('Variable #2: crecimiento de la población')
    latex_formula = r"H_0: \text{El crecimiento de la población no afecta de manera significativa el bienestar de la poblacion entre Colombia y Suramerica}"
    latex_formula += r", \\ H_1: \text{El crecimiento de la poblacion tiene un impacto significativo en el bienestar de la poblacion entre Colombia y Suramerica}"
    st.latex(latex_formula)
    texto_simple = """
    Se realizó la prueba de hipótesis por año y en las 17 pruebas se obtuvo un valor p value menor 
    a 0.05, por lo que se rechaza la hipótesis nula. Con esto se puede decir que no
    existe un impacto significativo en el crecimiento de la población.
    """
    st.text(texto_simple)

    st.subheader('Variable #3: PIB per capita')
    latex_formula = r"H_0: \text{No hay diferencia significativa en el PIB entre Colombia y Suramerica}"
    latex_formula += r", \\ H_1: \text{Existe una diferencia significativa en el PIB entre Colombia y Suramerica}"
    st.latex(latex_formula)
    texto_simple = """
    Se realizó la prueba de hipótesis por año y en las 17 pruebas se obtuvo un valor p value menor 
    a 0.05, por lo que se rechaza la hipótesis nula. Con esto se puede decir que 
    no existe una diferencia significativa entre el ingreso per capita entre Colombia y Suramerica.
    """
    st.text(texto_simple)








with tab4:
   
    st.divider()
    st.subheader('Evolución por variables')
    fig, axs = plt.subplots(2, 2, figsize=(12, 12))
    axs = axs.flatten()
    years = ["2002-2006", "2007-2011", "2012-2016", "2017-2019"]
    dw2['año'] = dw2['año'].astype(int)
    
    for i, ax in enumerate(axs):
        year_range = years[i]
        start_year, end_year = map(int, year_range.split("-"))
        df_year = dw2[(dw2['año'] >= start_year) & (dw2['año'] <= end_year)]
    
        df_year.plot(
            column="pibpc",
            scheme="Quantiles",
            cmap="plasma",
            legend=True,
            legend_kwds={"fmt": "{:.0f}"},
            ax=ax,
        )
    
        ax.set_axis_off()
        ax.set_title(f"PIB de {year_range} en Países de América")
    plt.suptitle("EVOLUCIÓN DEL PIB EN AMÉRICA (2002-2019)")
    plt.tight_layout()
    st.pyplot(fig)

    fig, axs = plt.subplots(2, 2, figsize=(12, 12))
    axs = axs.flatten()
    years = ["2002-2006", "2007-2011", "2012-2016", "2017-2019"]

    for i, ax in enumerate(axs):
        year_range = years[i]
        start_year, end_year = map(int, year_range.split("-"))
        d_year = dw2[(dw2['año'] >= start_year) & (dw2['año'] <= end_year)]

        d_year.plot(column="c.poblacion",scheme="Quantiles",cmap="plasma",
            legend=True,
            legend_kwds={"fmt": "{:.0f}"},
            ax=ax,)

        ax.set_axis_off()
        ax.set_title(f"Crecimiento de la población de {year_range} en América")
    plt.suptitle("EVOLUCIÓN POBLACIONAL EN AMÉRICA (2002-2019)")
    plt.tight_layout()
    plt.show()