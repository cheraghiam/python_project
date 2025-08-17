import streamlit as st
import nltk
from src.password_generator import PinPasswordGenerator, RandomPasswordGenerator, MemorablePasswordGenerator


nltk.download('words')


st.image("images/password_image.png", width=500)
st.title(":key: Password Generator")
sb = st.selectbox("Choose a password generation method:", ("Pin", "Random", "Memorable"))

if sb == "Pin":
    length = st.slider("Length Password: ", 8, 32)
    pin_generator = PinPasswordGenerator(length)
    st.write(f"pin Password: ```{pin_generator.generate()}``` ")

elif sb == "Random":
    length = st.slider("Length Password: ", 8, 32)
    include_number = st.toggle("include number")
    include_symbols = st.toggle("include symbols")
    random_generator = RandomPasswordGenerator(length=length, include_digits=include_number, include_symbols=include_symbols)
    st.write(f"Random Password: ```{random_generator.generate()}``` ")

elif sb == "Memorable":
    length = st.slider("Length Password: ", 2, 12)
    memory_generator = MemorablePasswordGenerator(length=length)
    st.write(f"Memorable password: ```{memory_generator.generate()}```")    
