import streamlit as st
import pickle
import numpy as np

# ------------------ CONFIG ------------------
st.set_page_config(page_title="Walmart App", page_icon="🛒", layout="wide")

st.markdown("""
    <style>
    .stApp {
        background-color: #f5f7fa;
    }
    .stButton>button {
        background-color: green;
        color: white;
        border-radius: 10px;
        height: 3em;
        width: 100%;
    }
    </style>
""", unsafe_allow_html=True)

# ------------------ SESSION ------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# ------------------ LOGIN FUNCTION ------------------
def login():
    st.markdown("<h2 style='text-align:center;'>Login Page</h2>", unsafe_allow_html=True)

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "admin" and password == "1234":
            st.session_state.logged_in = True
        else:
            st.error("Invalid Credentials")

# ------------------ MAIN APP ------------------
def main_app():
    model = pickle.load(open("sales_model.pkl", "rb"))

    st.markdown("<h1 style='text-align:center; color:green;'>🛒 Walmart Sales Predictor</h1>", unsafe_allow_html=True)

    st.markdown("Enter Details Below")

    col1, col2 = st.columns(2)

    with col1:
        Store = st.number_input("Store")
        Dept = st.number_input("Dept")
        Temperature = st.slider("Temperature", 0.0, 100.0, 25.0)
        Fuel_Price = st.number_input("Fuel Price")

    with col2:
        CPI = st.number_input("CPI")
        Unemployment = st.number_input("Unemployment")
        Size = st.number_input("Size")
        Year = st.number_input("Year")

    st.markdown("Promotions (MarkDown)")
    m1, m2, m3 = st.columns(3)

    with m1:
        MarkDown1 = st.number_input("MarkDown1")
        MarkDown2 = st.number_input("MarkDown2")

    with m2:
        MarkDown3 = st.number_input("MarkDown3")
        MarkDown4 = st.number_input("MarkDown4")

    with m3:
        MarkDown5 = st.number_input("MarkDown5")
        Month = st.number_input("Month")

    Week = st.number_input("Week")

    Isholiday = st.selectbox("Isholiday?", ["No", "Yes"])
    Isholiday = 1 if Isholiday == "Yes" else 0

    Type_B = st.selectbox("Type_B", [0, 1])
    Type_C = st.selectbox("Type_C", [0, 1])

    # Prediction
    if st.button("Predict Sales"):
        input_data = np.array([[Store, Dept, Isholiday, Temperature, Fuel_Price,
                                MarkDown1, MarkDown2, MarkDown3, MarkDown4, MarkDown5,
                                CPI, Unemployment, Size, Year, Month, Week,
                                Type_B, Type_C]])

        prediction = model.predict(input_data)

        st.success(f"Predicted Sales: {prediction[0]:.2f}")

    # Logout button
    if st.button("Logout"):
        st.session_state.logged_in = False

# ------------------ ROUTING ------------------
if st.session_state.logged_in:
    main_app()
else:
    login()