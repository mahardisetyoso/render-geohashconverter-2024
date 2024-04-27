from pathlib import Path
import streamlit as st

st.title("ABOUT ME")
from PIL import Image

current_dir = Path(__file__).parent if "_file_" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
profile_pic = current_dir / "assets" / "sample_1.jpg"

image = Image.open(profile_pic)
st.image(image, width= 400)

st.write("Mahardi Setyoso Pratomo")
st.write("Linkedin [link](https://www.linkedin.com/in/mahardi-setyoso-pratomo-5ab97432/)")
st.write("Github [link](https://github.com/mahardisetyoso)")
st.write("Email: [mahardisetyoso@gmail.com]")