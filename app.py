import streamlit as st

# Title of the app
st.title("Simple Calculator")

# Input fields for the numbers
num1 = st.number_input("Enter the first number:", step=1.0)
num2 = st.number_input("Enter the second number:", step=1.0)

# Selection of operation
operation = st.selectbox("Select Operation", ("Add", "Subtract", "Multiply", "Divide"))

# Perform calculation based on the selected operation
if operation == "Add":
    result = num1 + num2
    st.write("Result:", result)
elif operation == "Subtract":
    result = num1 - num2
    st.write("Result:", result)
elif operation == "Multiply":
    result = num1 * num2
    st.write("Result:", result)
elif operation == "Divide":
    if num2 != 0:
        result = num1 / num2
        st.write("Result:", result)
    else:
        st.write("Error: Cannot divide by zero")
