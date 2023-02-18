import streamlit
streamlit.title("My Mom's new healthy diner")
streamlit.header( 'Breakfast Favorites')
streamlit.text('🥣omega 3 & Blueberry oatmeal')
streamlit.text('🥗kale Spinach & Rocket smoothie')
streamlit.text('🐔Hard-boiled Free range Egg')
streamlit.text('🥑🍞Avacado Spinach Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)

# Display the table on the page.
fruits_selected = streamlit.multiselect("pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])

fruits_to_show = my_fruit_list.loc[fruits_selected]

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)
