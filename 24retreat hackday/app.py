import streamlit as st
import subprocess
import requests
from PIL import Image
from io import BytesIO
import call_supermeme

# Function to execute call_supermeme.py
def execute_script(meme_sentence):
    cmd = ["python", "call_supermeme.py", meme_sentence]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout

# Function to display text from Duc's prompt


# Function to display image from URL
def display_image_from_url(url):
    try:
        # Fetch image from URL
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
        
        # Display image
        st.image(img, caption="Image", use_column_width=True)
    except Exception as e:
        st.error("Error loading image.")
        st.write(f"Error details: {e}")

# Streamlit app
def main():
    
    # Logo image
    logo_url = "https://uploads-ssl.webflow.com/5d279ebd3e4dac05c81d8ac5/5d27a3053e4dacc11a1dc1f3_madkudu_rectangle_xlarge_white.svg"
    st.markdown(
    f'<div class="logo-container"><img src="{logo_url}" alt="Logo" style="width:200px;float: right;"></div>',
    unsafe_allow_html=True
    )

    # Custom CSS for changing title font
    st.markdown(
        """
        <h1 style='font-family: Impact, Charcoal, sans-serif;'>MEME-AUGMENTED KUDU</h1>
        """,
        unsafe_allow_html=True
    )


    # Text input for account name
    account_name = st.text_input("Enter an account name")

    if st.button("Bring on the memes!"):
        if account_name:
            st.write("Summoning powerful memes...")
            # TODO
            # output = execute_script(account_name)

            # TODO retrieve text from Duc
            text = "Charles is surprised when he realizes Copilot weekly usage has gone 2x"
            text = "Duc is sad that Chloé is leaving MadKudu tomorrow"

            # Assuming the output of call_supermeme.py is a single URL
            url = call_supermeme.generate_meme(text)

            if url:
                # Display the first image URL as an image
                st.write(text)
                display_image_from_url(url)
            else:
                st.warning("No image URLs found.")
        else:
            st.warning("Please enter an account name.")

if __name__ == "__main__":
    main()
