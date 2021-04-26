import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

by_residence = pd.read_excel("Urbanization-data.xlsx", sheet_name='by_residence', engine='openpyxl')
by_res_wealth = pd.read_excel("Urbanization-data.xlsx", sheet_name='by_residence_wealthquintiles', engine='openpyxl')

# print(by_residence.head())

# print(by_residence['Area name'].unique())


indicators = by_residence["Indicator name"].unique().tolist()

st.title('Final project - Urbanization data')
st.sidebar.title('Final project - Urbanization data')
st.header("Urban versus rural graph for chosen categories")
st.sidebar.header("Urban versus rural graph for chosen categories")
select_indicators = st.sidebar.multiselect('Choose a service', indicators)

st.write("The graph below will look at the averages of Urban and Rural indicator scores across chosen indicator categories")

#get data for grouped bar graph
def grouped_bar_data(selected):
    selected = list(selected)
    dict_data = {}
    urban_list = []
    rural_list = []
    for i in selected:
        data = by_residence[by_residence['Indicator name'] == i]
        data_urban = data[data['Residence'] == 'Urban']
        urban_mean = data_urban['Indicator value'].mean()
        data_rural = data[data['Residence'] == 'Rural']
        rural_mean = data_rural['Indicator value'].mean()
        urban_list.append(urban_mean)
        rural_list.append(rural_mean)
    dict_data['Urban'] = urban_list
    dict_data['Rural'] = rural_list
    return dict_data

b_data = grouped_bar_data(select_indicators)

def grouped_bar(data, title, indicator, amount):
    x = np.arange(int(amount))
    width = 0.125
    count = 0
    for key in data:
        plt.bar(x+count*width, data[key], width)
        count+=1
    plt.xticks(x, indicator, rotation=85)
    plt.xlabel("Indicator category")
    plt.ylabel('Indicator score')
    plt.legend(list(data.keys()))
    plt.title(title)
    plt.show()

# st.write(b_data)

title = 'Average indicator score in selected categories for Urban vs Rural'
n = len(select_indicators)
st.set_option('deprecation.showPyplotGlobalUse', False)

st.pyplot(grouped_bar(b_data, title, select_indicators, n))


#by_res_wealth

st.header("Urban versus rural graph between quintiles")
st.sidebar.header("Urban versus rural graph between quintiles")

st.write("The below graph will look at average Urban and Rural values across five wealth quintiles for a chosen indicator category")

select_indicator = st.sidebar.selectbox("Select an indicator", indicators)

wealth_quintiles = by_res_wealth["Wealth quintile"].unique().tolist()

def grouped_bar_data2(select):
    dict_data = {}
    urban_list = []
    rural_list = []
    data = by_res_wealth[by_res_wealth["Indicator name"] == select]
    for i in wealth_quintiles:
        data_by_quintile = data[data["Wealth quintile"] == i]
        urban_data = data_by_quintile[data_by_quintile["Residence"] == "Urban"]
        rural_data = data_by_quintile[data_by_quintile["Residence"] == "Rural"]
        urban_mean = urban_data["Indicator value"].mean()
        rural_mean = rural_data["Indicator value"].mean()
        urban_list.append(urban_mean)
        rural_list.append(rural_mean)
    dict_data["Urban"] = urban_list
    dict_data["Rural"] = rural_list
    return dict_data

# st.write(grouped_bar_data2(select_indicator))

b_data2 = grouped_bar_data2(select_indicator)

def grouped_bar2(data, title, wealth_quintiles, amount):
    x = np.arange(int(amount))
    width = 0.25
    count = 0
    for key in data:
        plt.bar(x+count*width, data[key], width)
        count+=1
    plt.xticks(x, wealth_quintiles)
    plt.xlabel("Wealth Quintiles")
    plt.ylabel('Indicator value')
    plt.legend(list(data.keys()))
    plt.title(title)
    plt.show()

title2 = f"Grouped Bar Graph of Average Urban versus Rural Indicator values in the ({select_indicator}) category"
n2 = len(wealth_quintiles)
st.pyplot(grouped_bar2(b_data2, title2, wealth_quintiles, n2))








