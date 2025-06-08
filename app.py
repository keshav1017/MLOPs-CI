import streamlit as st

# streamlit ui
st.title(f"Power Calculator")
st.write(f"Enter a number to calculate it's square, cube and fifth power.")

# get the user input
n = st.number_input("Enter an integer", value = 1, step = 1)

# calculate the results
square = n**2
cube = n**3
fifth = n**5

# display the results
st.write(f"The square of {n} is {square}.")
st.write(f"The cube of {n} is {cube}.")
st.write(f"The fifth power of {n} is {fifth}.")