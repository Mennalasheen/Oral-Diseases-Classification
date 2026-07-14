import os
import base64
import bcrypt
import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# ==================================================
# CONFIGURATION
# ==================================================

MODEL_PATH = "best_model.h5"
CREDENTIALS_FILE = "credentials.txt"
BACKGROUND_IMAGE = "Dental2.jpg"

IMAGE_WIDTH = 225
IMAGE_HEIGHT = 225

class_names = [
    "Calculus",
    "Data caries",
    "Gingivitis",
    "Mouth Ulcer",
    "Tooth Discoloration",
    "Hypodontia"
]

# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="Oral Disease Detection",
    page_icon="🦷",
    layout="centered"
)

# ==================================================
# BACKGROUND IMAGE
# ==================================================

def get_base64(file_path):
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()


def set_background(image_file):

    if not os.path.exists(image_file):
        return

    encoded = get_base64(image_file)

    st.markdown(
        f"""
        <style>

        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}

        [data-testid="stHeader"] {{
            background: rgba(0,0,0,0);
        }}

        [data-testid="stSidebar"] {{
            background: rgba(255,255,255,0.15);
            backdrop-filter: blur(10px);
        }}

        .block-container {{
            background: rgba(255,255,255,0.15);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border-radius: 20px;
            padding: 2rem;
            border: 1px solid rgba(255,255,255,0.2);
}}
        </style>
        """,
        unsafe_allow_html=True
    )

# ==================================================
# LOAD MODEL
# ==================================================

@st.cache_resource
def load_model():
    return tf.keras.models.load_model(MODEL_PATH)

model = load_model()

# ==================================================
# PASSWORD FUNCTIONS
# ==================================================

def hash_password(password):
    return bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt()
    ).decode("utf-8")


def check_password(password, hashed):
    return bcrypt.checkpw(
        password.encode("utf-8"),
        hashed.encode("utf-8")
    )

# ==================================================
# SIGNUP
# ==================================================

def signup(username, password):

    if os.path.exists(CREDENTIALS_FILE):

        with open(CREDENTIALS_FILE, "r") as f:

            for line in f:

                saved_user = line.strip().split(",")[0]

                if saved_user == username:
                    st.error("Username already exists.")
                    return

    hashed_password = hash_password(password)

    with open(CREDENTIALS_FILE, "a") as f:
        f.write(
            f"{username},{hashed_password}\n"
        )

    st.success("Account created successfully!")

# ==================================================
# LOGIN
# ==================================================

def login(username, password):

    if not os.path.exists(CREDENTIALS_FILE):
        st.error("No users found. Please sign up.")
        return

    with open(CREDENTIALS_FILE, "r") as f:
        credentials = f.readlines()

    for row in credentials:

        user, pwd_hash = row.strip().split(",")

        if user == username and check_password(password, pwd_hash):

            st.session_state["authenticated"] = True
            st.session_state["username"] = username

            st.success("Login successful!")

            st.rerun()

    st.error("Invalid username or password.")

# ==================================================
# LOGOUT
# ==================================================

def logout():

    st.session_state["authenticated"] = False
    st.session_state["username"] = None

    st.rerun()

# ==================================================
# IMAGE PREPROCESSING
# ==================================================

def preprocess_image(image):

    image = image.convert("RGB")

    image = image.resize(
        (IMAGE_WIDTH, IMAGE_HEIGHT)
    )

    image = np.array(image)

    image = np.expand_dims(
        image,
        axis=0
    )

    return image

# ==================================================
# PREDICTION
# ==================================================

def predict_disease(image):

    img = preprocess_image(image)

    preds = model.predict(img, verbose=0)

    predicted_index = np.argmax(preds)

    predicted_class = class_names[predicted_index]

    confidence = float(np.max(preds))

    return (
        predicted_class,
        confidence,
        preds[0]
    )

# ==================================================
# LOGIN / SIGNUP PAGE
# ==================================================

def show_login_signup_page():

    st.title("🦷 Oral Disease Detection System")

    page = st.sidebar.radio(
        "Navigation",
        ["Login", "Signup"]
    )

    if page == "Login":

        st.subheader("Login")

        username = st.text_input(
            "Username"
        )

        password = st.text_input(
            "Password",
            type="password"
        )

        if st.button("Login"):
            login(username, password)

    else:

        st.subheader("Create Account")

        username = st.text_input(
            "Username"
        )

        password = st.text_input(
            "Password",
            type="password"
        )

        confirm_password = st.text_input(
            "Confirm Password",
            type="password"
        )

        if st.button("Signup"):

            if password != confirm_password:
                st.error("Passwords do not match.")

            else:
                signup(
                    username,
                    password
                )

# ==================================================
# PREDICTION PAGE
# ==================================================

def show_prediction_page():

    st.title("🦷 Oral Disease Detection System")

    col1, col2 = st.columns([5, 1])

    with col1:
        st.write(
            f"### Welcome, {st.session_state['username']}"
        )

    with col2:
        st.write("")
        if st.button("Logout"):
            logout()

    st.markdown("---")

    uploaded_file = st.file_uploader(
        "Upload Oral Image",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_file is not None:

        image = Image.open(uploaded_file)

        st.image(
            image,
            caption="Uploaded Image",
        )

        if st.button("Predict Disease"):

            disease, confidence, probs = predict_disease(image)

            st.success(
                f"Predicted Disease: {disease}"
            )

            st.info(
                f"Confidence: {confidence:.2%}"
            )

            st.subheader(
                "Class Probabilities"
            )

            for i, cls in enumerate(class_names):

                st.write(
                    f"**{cls}** : {probs[i]*100:.2f}%"
                )

                st.progress(
                    float(probs[i])
                )

# ==================================================
# SESSION STATE
# ==================================================

if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if "username" not in st.session_state:
    st.session_state["username"] = None

# ==================================================
# APPLY BACKGROUND
# ==================================================

set_background(BACKGROUND_IMAGE)

# ==================================================
# MAIN APP
# ==================================================

if st.session_state["authenticated"]:
    show_prediction_page()
else:
    show_login_signup_page()