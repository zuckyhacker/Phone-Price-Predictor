import streamlit as st
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
import pickle
import os

st.set_page_config(
    page_title="Mobile Price Predictor",
    page_icon="📱",
    layout="wide"
)


@st.cache_resource
def train_model():
    np.random.seed(42)
    n = 2000

    price_range = np.random.choice([0, 1, 2, 3], n)

    ram = np.where(
        price_range == 0, np.random.randint(256, 1024, n),
        np.where(
            price_range == 1, np.random.randint(1024, 2048, n),
            np.where(
                price_range == 2, np.random.randint(2048, 4096, n),
                np.random.randint(4096, 8192, n)
            )
        )
    )

    battery_power = np.where(
        price_range == 0, np.random.randint(500, 1500, n),
        np.where(
            price_range == 1, np.random.randint(1200, 2500, n),
            np.where(
                price_range == 2, np.random.randint(2000, 4000, n),
                np.random.randint(3500, 6000, n)
            )
        )
    )

    int_memory = np.where(
        price_range == 0, np.random.randint(4, 16, n),
        np.where(
            price_range == 1, np.random.randint(16, 64, n),
            np.where(
                price_range == 2, np.random.randint(64, 128, n),
                np.random.randint(128, 512, n)
            )
        )
    )

    pc = np.where(
        price_range == 0, np.random.randint(2, 8, n),
        np.where(
            price_range == 1, np.random.randint(8, 16, n),
            np.where(
                price_range == 2, np.random.randint(12, 64, n),
                np.random.randint(48, 200, n)
            )
        )
    )

    fc = np.where(
        price_range == 0, np.random.randint(0, 5, n),
        np.where(
            price_range == 1, np.random.randint(5, 13, n),
            np.where(
                price_range == 2, np.random.randint(13, 32, n),
                np.random.randint(20, 64, n)
            )
        )
    )

    n_cores = np.where(
        price_range == 0, np.random.randint(1, 4, n),
        np.where(
            price_range == 1, np.random.randint(4, 6, n),
            np.where(
                price_range == 2, np.random.randint(6, 8, n),
                np.random.randint(8, 12, n)
            )
        )
    )

    clock_speed = np.round(
        np.where(
            price_range < 2,
            np.random.uniform(0.5, 2.0, n),
            np.random.uniform(1.5, 3.5, n)
        ), 1
    )

    blue = np.where(price_range > 0, np.random.choice([0, 1], n, p=[0.1, 0.9]),
                    np.random.choice([0, 1], n, p=[0.5, 0.5]))

    dual_sim = np.random.choice([0, 1], n)

    four_g = np.where(price_range > 1, np.random.choice([0, 1], n, p=[0.05, 0.95]),
                      np.random.choice([0, 1], n, p=[0.5, 0.5]))

    three_g = np.where(four_g == 1, 1, np.random.choice([0, 1], n))

    touch_screen = np.where(price_range > 0, np.random.choice([0, 1], n, p=[0.05, 0.95]),
                            np.random.choice([0, 1], n, p=[0.3, 0.7]))

    wifi = np.where(price_range > 0, np.random.choice([0, 1], n, p=[0.05, 0.95]),
                    np.random.choice([0, 1], n, p=[0.4, 0.6]))

    px_height = np.where(
        price_range == 0, np.random.randint(240, 720, n),
        np.where(
            price_range == 1, np.random.randint(720, 1080, n),
            np.where(
                price_range == 2, np.random.randint(1080, 2160, n),
                np.random.randint(1440, 3840, n)
            )
        )
    )

    px_width = np.where(
        price_range == 0, np.random.randint(240, 720, n),
        np.where(
            price_range == 1, np.random.randint(720, 1080, n),
            np.where(
                price_range == 2, np.random.randint(1080, 2160, n),
                np.random.randint(1440, 3840, n)
            )
        )
    )

    sc_h = np.random.randint(5, 19, n)
    sc_w = np.random.randint(0, 18, n)
    m_dep = np.round(np.random.uniform(0.1, 1.0, n), 1)
    mobile_wt = np.random.randint(80, 220, n)
    talk_time = np.random.randint(2, 20, n)

    df = pd.DataFrame({
        'battery_power': battery_power,
        'blue': blue,
        'clock_speed': clock_speed,
        'dual_sim': dual_sim,
        'fc': fc,
        'four_g': four_g,
        'int_memory': int_memory,
        'm_dep': m_dep,
        'mobile_wt': mobile_wt,
        'n_cores': n_cores,
        'pc': pc,
        'px_height': px_height,
        'px_width': px_width,
        'ram': ram,
        'sc_h': sc_h,
        'sc_w': sc_w,
        'talk_time': talk_time,
        'three_g': three_g,
        'touch_screen': touch_screen,
        'wifi': wifi,
        'price_range': price_range
    })

    X = df.drop('price_range', axis=1)
    y = df['price_range']

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    model = RandomForestClassifier(n_estimators=200, random_state=42)
    model.fit(X_scaled, y)

    return model, scaler, X.columns.tolist()


model, scaler, feature_cols = train_model()

st.title("📱 Mobile Price Predictor")
st.markdown("Enter your phone's specifications below to predict its price range.")
st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Hardware")
    battery_power = st.slider("Battery Power (mAh)", 500, 6000, 2000, 100)
    ram = st.select_slider("RAM (MB)", options=[256, 512, 1024, 2048, 3072, 4096, 6144, 8192], value=2048)
    int_memory = st.select_slider("Internal Memory (GB)", options=[4, 8, 16, 32, 64, 128, 256, 512], value=64)
    n_cores = st.slider("Number of CPU Cores", 1, 12, 4)
    clock_speed = st.slider("Clock Speed (GHz)", 0.5, 3.5, 1.5, 0.1)
    mobile_wt = st.slider("Weight (grams)", 80, 220, 150)
    m_dep = st.slider("Depth (cm)", 0.1, 1.0, 0.5, 0.1)

with col2:
    st.subheader("Camera")
    pc = st.slider("Primary Camera (MP)", 0, 200, 12)
    fc = st.slider("Front Camera (MP)", 0, 64, 8)

    st.subheader("Display")
    px_height = st.slider("Resolution Height (px)", 240, 3840, 1920, 10)
    px_width = st.slider("Resolution Width (px)", 240, 3840, 1080, 10)
    sc_h = st.slider("Screen Height (cm)", 5, 19, 14)
    sc_w = st.slider("Screen Width (cm)", 0, 18, 7)
    talk_time = st.slider("Talk Time (hours)", 2, 20, 10)

with col3:
    st.subheader("Connectivity")
    blue = st.checkbox("Bluetooth", value=True)
    dual_sim = st.checkbox("Dual SIM", value=True)
    four_g = st.checkbox("4G / LTE", value=True)
    three_g = st.checkbox("3G", value=True)
    touch_screen = st.checkbox("Touch Screen", value=True)
    wifi = st.checkbox("WiFi", value=True)

st.markdown("---")

if st.button("🔍 Predict Price Range", use_container_width=True, type="primary"):
    input_data = pd.DataFrame([[
        battery_power,
        int(blue),
        clock_speed,
        int(dual_sim),
        fc,
        int(four_g),
        int_memory,
        m_dep,
        mobile_wt,
        n_cores,
        pc,
        px_height,
        px_width,
        ram,
        sc_h,
        sc_w,
        talk_time,
        int(three_g),
        int(touch_screen),
        int(wifi)
    ]], columns=feature_cols)

    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)[0]
    probabilities = model.predict_proba(input_scaled)[0]

    price_labels = {
        0: ("Low Cost", "💚", "Under $150", "#28a745"),
        1: ("Medium Cost", "💛", "$150 – $350", "#ffc107"),
        2: ("High Cost", "🟠", "$350 – $700", "#fd7e14"),
        3: ("Very High Cost", "🔴", "Above $700", "#dc3545")
    }

    label, icon, price_range_text, color = price_labels[prediction]

    st.markdown(f"""
    <div style="background-color:{color}22; border-left: 6px solid {color}; padding: 20px; border-radius: 8px; margin-bottom: 20px;">
        <h2 style="color:{color}; margin:0;">{icon} {label}</h2>
        <p style="font-size: 1.2rem; margin-top: 8px; margin-bottom: 0;">Estimated Price Range: <strong>{price_range_text}</strong></p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("Prediction Confidence")
    prob_df = pd.DataFrame({
        "Price Range": ["Low Cost", "Medium Cost", "High Cost", "Very High Cost"],
        "Confidence (%)": [round(p * 100, 1) for p in probabilities]
    })
    st.bar_chart(prob_df.set_index("Price Range"))

    st.subheader("Key Factors")
    feature_importance = pd.Series(
        model.feature_importances_,
        index=feature_cols
    ).sort_values(ascending=False).head(5)

    labels_map = {
        'ram': 'RAM',
        'battery_power': 'Battery Power',
        'px_height': 'Resolution Height',
        'px_width': 'Resolution Width',
        'int_memory': 'Internal Memory',
        'pc': 'Primary Camera',
        'fc': 'Front Camera',
        'n_cores': 'CPU Cores',
        'clock_speed': 'Clock Speed',
        'mobile_wt': 'Weight',
        'talk_time': 'Talk Time',
        'four_g': '4G Support',
        'blue': 'Bluetooth',
        'dual_sim': 'Dual SIM',
        'three_g': '3G Support',
        'touch_screen': 'Touch Screen',
        'wifi': 'WiFi',
        'sc_h': 'Screen Height',
        'sc_w': 'Screen Width',
        'm_dep': 'Depth',
    }
    feature_importance.index = [labels_map.get(i, i) for i in feature_importance.index]
    st.bar_chart(feature_importance)

st.markdown("---")
st.caption("This predictor uses a Random Forest model trained on phone specification patterns to estimate price ranges.")
