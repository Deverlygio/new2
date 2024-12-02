from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

# Load Lottie animation from URL
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Set page configuration
st.set_page_config(page_title="computer enineering", page_icon="💻", layout="wide")

# Load local CSS
def local_css(file_name):
    try:
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.error("CSS file not found. Make sure the path is correct.")

local_css("style/style.css")

# Load Lottie animation
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")

# Load images
try:
    img_contact_form = Image.open("download.jpg")
    img_github = Image.open("download.jpg")
except FileNotFoundError:
    st.error("Image file not found. Make sure the paths are correct.")

# Header section
with st.container():
    st.subheader("Hi, I am Deverly Gio")
    st.title("programming requires a range of skills!")
    st.write(
        """
       Welcome to my blog! Come along as I dive into the fascinating world of Computer Engineering. 
       I'll be sharing my experiences, challenges, and the excitement of being a Computer Engineering student."
        """
    )
    st.write("[Message me on Gmail >](mailto:giodeverly21@gmail.com)")

# First-year perspective section
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Computer Programming: First-Year Experiences")
        st.write(
            """
           Starting university was a blend of excitement and anxiety.
           Learning programming felt like unlocking a mysterious new language. 
           From binary code to algorithms, it's been an unforgettable journey!"
            """
        )
        st.write("[Learn more >](https://www.youtube.com/watch?v=VqgUkExPvLY)")
    with right_column:
        if lottie_coding:
            st_lottie(lottie_coding, height=300, key="coding")
        else:
            st.error("Lottie animation could not load.")

# Insights and reflections
with st.container():
    st.write("---")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form, caption="Debugging: the secouth of taking risk!")
    with text_column:
        st.write(
            """
           "Programming assignments are both exciting and occasionally tough.
           Debugging is like a daily challenge, but the sense of accomplishment when solving a problem is incomparable.
           Managing academics, personal time, and social life can be tricky, but staying organized is essential."
            """
        )


with st.container():
    st.write("---")
    st.subheader("PROS AND CONS")
    st.write("### PROS:")
    st.write("""
  1. High-paying job opportunities with strong demand for programmers.
2. Enhance logical thinking and problem-solving abilities.
3. The opportunity to be creative in designing innovative solutions.
4. Flexibility in work settings, such as remote options.
5. Ongoing learning in a rapidly evolving field.
6. Build connections with a global network of developers.
    """)
    st.write("### CONS:")
    st.write("""
  1. A challenging learning process for newcomers.
2. Sedentary nature of the job can affect physical well-being.
3. Debugging can be tedious and often frustrating.
4. Constant technological advancements demand ongoing learning.
5. Some work environments may feel isolating.
6. Handling the complexity of code in large projects can be difficult.

""")


with st.container():
    st.write("---")
    st.header("For Comments:")
    st.write("##")
    
    contact_form = """
    <form action="https://formspree.io/f/{your-form-id}" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
