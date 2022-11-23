
import streamlit 
import pandas as pd

streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
my_fruit_list = my_fruit_list.set_index('Fruit')
#pick list widget
fruits_list = streamlit.multiselect("Pick some fruits: ", list(my_fruit_list.index), ['Avocados', 'Strawberries'])
#display table on page
my_fruit_list = my_fruit_list.loc[fruit_list]
streamlit.dataframe(my_fruit_list)
