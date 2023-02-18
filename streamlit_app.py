import streamlit
streamlit.title('My parents new healthy diner')
streamlit.header( 'Breakfast Favorites')
streamlit.text('🥣omega 3 & Blueberry oatmeal')
streamlit.text('🥗kale Spinach & Rocket smoothie')
streamlit.text('🐔Hard-boiled Free range Egg')
streamlit.text('🥑🍞Avacado Spinach Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

