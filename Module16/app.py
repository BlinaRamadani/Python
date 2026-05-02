import streamlit as st

def main():
    st.title("Hello World")
    st.button("Click here")
    if st.button("Click Me"):
        st.write("Button Clicked")
    if st.checkbox("Click"):
        st.write("The Checkbox was clicked")
    user_input = st.text_input("Enter Text","Sample")
    st.write("You wrote: ", user_input)
    age = st.number_input("Enter your age",min_value=0, max_value=100)
    st.write(f"Your age is: {age}")

if __name__ == "__main__":
    main()
