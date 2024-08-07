import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

def power(x, y):
    return x ** y

def square_root(x):
    return math.sqrt(x)

def sine(x):
    return math.sin(math.radians(x))

def cosine(x):
    return math.cos(math.radians(x))

def tangent(x):
    return math.tan(math.radians(x))

import streamlit as st

# Calculator functions (import or define them here)

def main():
    st.title("Scientific Calculator")

    menu = ["Addition", "Subtraction", "Multiplication", "Division", "Power", "Square Root", "Sine", "Cosine", "Tangent"]
    choice = st.selectbox("Select Operation", menu)

    if choice in ["Addition", "Subtraction", "Multiplication", "Division", "Power"]:
        num1 = st.number_input("Enter first number", value=0.0)
        num2 = st.number_input("Enter second number", value=0.0)

        if st.button("Calculate"):
            if choice == "Addition":
                result = add(num1, num2)
            elif choice == "Subtraction":
                result = subtract(num1, num2)
            elif choice == "Multiplication":
                result = multiply(num1, num2)
            elif choice == "Division":
                result = divide(num1, num2)
            elif choice == "Power":
                result = power(num1, num2)
            st.write("Result:", result)

    elif choice == "Square Root":
        num = st.number_input("Enter number", value=0.0)
        if st.button("Calculate"):
            result = square_root(num)
            st.write("Result:", result)

    elif choice in ["Sine", "Cosine", "Tangent"]:
        angle = st.number_input("Enter angle in degrees", value=0.0)
        if st.button("Calculate"):
            if choice == "Sine":
                result = sine(angle)
            elif choice == "Cosine":
                result = cosine(angle)
            elif choice == "Tangent":
                result = tangent(angle)
            st.write("Result:", result)

if __name__ == "__main__":
    main()
