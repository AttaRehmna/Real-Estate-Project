import streamlit as st
import pandas as pd
import plotly.express as px

# Streamlit app title
st.set_page_config(page_title="Dashboard Analytics", layout="wide")
st.markdown("""
    <style>
        .main-title {
            font-size: 50px;
            font-weight: bold;
            color: #FF5733;
            text-align: center;
        }
        .menu-container {
            display: flex;
            justify-content: center;
            background-color: #282c34;
            padding: 15px;
            border-radius: 10px;
            margin-bottom: 30px;
        }
        .menu-container label {
            color: white;
            font-size: 20px;
            margin: 0 20px;
        }
        .stButton > button {
            background-color: #FF5733;
            color: white;
            border-radius: 20px;
            font-size: 18px;
        }
        .sidebar .sidebar-content {
            display: none;
        }
        .block-container {
            background-color: #f5f5f5;
            padding: 40px;
            border-radius: 20px;
            box-shadow: 0 0 20px rgba(0,0,0,0.1);
        }
        .name-box {
            background-color: #4CAF50;
            color: white;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            font-size: 22px;
            font-weight: bold;
            margin: 20px 0;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='main-title'>📊 Dashboard Analytics</div>", unsafe_allow_html=True)

# Centered menu navigation
st.markdown("<div class='menu-container'>", unsafe_allow_html=True)
menu = st.radio("", ["Home", "Data Analysis", "Prediction", "Contact Us"], horizontal=True)
st.markdown("</div>", unsafe_allow_html=True)

if menu == "Home":
    st.header("🏠 Welcome to the Dashboard")
    st.write("Analyze your data efficiently with our interactive dashboard.")
    st.markdown("""
        <div class='name-box'>
            Developed by:<br>
            Ahmad Raza<br>
            Atta Ur Rehman<br>
            Waqas Ahmad Shaheen
        </div>
    """, unsafe_allow_html=True)
    st.image("https://via.placeholder.com/900x400", use_column_width=True)

elif menu == "Data Analysis":
    st.subheader("Upload and Analyze Data")
    uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)

        st.subheader("🔍 Data Overview")
        st.dataframe(df.head())
        
        selected_column = st.selectbox("Select Column for Visualization", df.columns)
        
        # Process data for charts
        value_counts = df[selected_column].value_counts().reset_index()
        value_counts.columns = [selected_column, 'count']

        tab1, tab2 = st.tabs(["📊 Bar Chart", "🍕 Pie Chart"])
        
        with tab1:
            st.subheader("Bar Chart")
            fig_bar = px.bar(value_counts, x=selected_column, y='count', title=f"Distribution of {selected_column}", color=selected_column)
            st.plotly_chart(fig_bar, use_container_width=True)

        with tab2:
            st.subheader("Pie Chart")
            fig_pie = px.pie(value_counts, names=selected_column, values='count', title=f"{selected_column} Distribution")
            st.plotly_chart(fig_pie, use_container_width=True)

elif menu == "Prediction":
    st.header("🔮 Prediction")
    st.write("Coming soon: Predictive analysis powered by AI.")
    st.image("https://via.placeholder.com/700x350", use_column_width=True)

elif menu == "Contact Us":
    st.header("📧 Contact Us")
    st.write("For inquiries, reach us at support@example.com or visit our website.")
    st.markdown("[Visit our website](https://www.example.com)")
