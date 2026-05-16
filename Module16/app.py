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
    message = st.text_area("Enter a message")
    st.write(f"Your message: {message}")
    choice = st.radio("Pick one",["Choice 1","Choice 2", "Choice 3"])
    st.write(f"You chose: {choice}")
    if st.button("Success"):
        st.success("Operation was successful")

    try:
        1/0
    except Exception as e:
        st.exception(e)





if __name__ == "__main__":
    main()
