import streamlit as st

st.set_page_config(
    page_title="Phone Price Predictor",
    page_icon="📱",
    layout="centered"
)

st.markdown("""
<style>
  /* Overall background */
  .stApp {
      background-color: #EEEEF8;
  }
  /* Hide default streamlit header */
  header[data-testid="stHeader"] {
      background: transparent;
  }
  /* Header card */
  .hero-card {
      background: linear-gradient(135deg, #E0DEFF 0%, #D4D0FF 100%);
      border-radius: 20px;
      padding: 28px 24px 24px 24px;
      margin-bottom: 16px;
  }
  .hero-icon {
      background: #C8C0FF;
      border-radius: 16px;
      width: 52px; height: 52px;
      display: flex; align-items: center; justify-content: center;
      font-size: 28px;
      margin-bottom: 14px;
  }
  .hero-title {
      font-size: 32px;
      font-weight: 800;
      color: #111;
      line-height: 1.1;
      margin: 0 0 8px 0;
  }
  .hero-sub {
      color: #555;
      font-size: 14px;
      margin: 0;
  }
  /* Section cards */
  .section-card {
      background: white;
      border-radius: 20px;
      padding: 20px;
      margin-bottom: 14px;
      box-shadow: 0 1px 6px rgba(0,0,0,0.06);
  }
  .section-header {
      display: flex;
      align-items: center;
      gap: 12px;
      margin-bottom: 16px;
  }
  .section-icon {
      background: #EDE9FF;
      border-radius: 12px;
      width: 40px; height: 40px;
      display: flex; align-items: center; justify-content: center;
      font-size: 18px;
  }
  .section-title {
      font-size: 17px;
      font-weight: 700;
      color: #111;
      margin: 0;
  }
  .field-label {
      font-size: 15px;
      font-weight: 700;
      color: #111;
      margin-bottom: 10px;
      margin-top: 4px;
  }
  .field-selected-badge {
      float: right;
      background: #EDE9FF;
      color: #6C3BFF;
      font-size: 12px;
      font-weight: 600;
      border-radius: 12px;
      padding: 2px 10px;
  }
  /* Radio as pills */
  div[data-testid="stRadio"] label {
      background: white;
      border: 1.5px solid #DDD;
      border-radius: 25px;
      padding: 7px 16px !important;
      font-size: 13px;
      font-weight: 500;
      color: #333;
      cursor: pointer;
      margin: 3px;
      transition: all 0.15s;
  }
  div[data-testid="stRadio"] label:hover {
      border-color: #6C3BFF;
      color: #6C3BFF;
  }
  div[data-testid="stRadio"] > div {
      flex-direction: row !important;
      flex-wrap: wrap;
      gap: 4px;
  }
  div[data-testid="stRadio"] [data-testid="stMarkdownContainer"] p {
      display: none;
  }
  /* Selected radio pill */
  div[data-testid="stRadio"] label:has(input:checked) {
      background: #6C3BFF !important;
      border-color: #6C3BFF !important;
      color: white !important;
      font-weight: 600;
  }
  /* Hide radio circle */
  div[data-testid="stRadio"] input[type="radio"] {
      display: none;
  }
  /* Toggle switch */
  .toggle-row {
      background: #F5F3FF;
      border-radius: 14px;
      padding: 14px 16px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-top: 10px;
  }
  .toggle-left {
      display: flex;
      align-items: center;
      gap: 12px;
  }
  .toggle-icon {
      font-size: 18px;
      color: #6C3BFF;
  }
  .toggle-label {
      font-size: 15px;
      font-weight: 700;
      color: #6C3BFF;
      margin: 0;
  }
  .toggle-sub {
      font-size: 12px;
      color: #888;
      margin: 0;
  }
  /* Predict button */
  div[data-testid="stButton"] > button {
      width: 100%;
      background: linear-gradient(135deg, #7B52FF, #5B35D5);
      color: white;
      font-size: 17px;
      font-weight: 700;
      border: none;
      border-radius: 16px;
      padding: 16px;
      cursor: pointer;
      margin-top: 8px;
  }
  div[data-testid="stButton"] > button:hover {
      background: linear-gradient(135deg, #6942EE, #4A28C4);
  }
  /* Result price card */
  .price-card {
      background: linear-gradient(135deg, #7B52FF 0%, #5B35D5 60%, #3D1DAA 100%);
      border-radius: 20px;
      padding: 24px;
      margin-bottom: 16px;
      color: white;
  }
  .price-label-row {
      display: flex; align-items: center; gap: 8px;
      font-size: 14px; opacity: 0.9; margin-bottom: 8px;
  }
  .price-amount {
      font-size: 42px;
      font-weight: 800;
      margin: 0 0 12px 0;
  }
  .price-badges {
      display: flex; gap: 10px; flex-wrap: wrap; margin-bottom: 16px;
  }
  .badge-filled {
      background: white;
      color: #6C3BFF;
      font-size: 12px;
      font-weight: 700;
      border-radius: 14px;
      padding: 4px 12px;
  }
  .badge-outline {
      background: rgba(255,255,255,0.2);
      color: white;
      font-size: 12px;
      font-weight: 500;
      border-radius: 14px;
      padding: 4px 12px;
  }
  .range-row {
      background: rgba(0,0,0,0.2);
      border-radius: 12px;
      padding: 12px 16px;
      display: flex;
      justify-content: space-between;
      align-items: center;
  }
  .range-item { text-align: center; }
  .range-item-label { font-size: 10px; opacity: 0.7; text-transform: uppercase; letter-spacing: 0.5px; }
  .range-item-value { font-size: 15px; font-weight: 700; }
  /* Phone model cards */
  .models-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 12px;
  }
  .models-title { font-size: 18px; font-weight: 800; color: #111; margin: 0; }
  .models-sub { font-size: 12px; color: #888; margin: 0; }
  .models-count {
      background: #6C3BFF;
      color: white;
      font-size: 13px;
      font-weight: 700;
      border-radius: 10px;
      padding: 3px 10px;
  }
  .model-card {
      background: white;
      border-radius: 16px;
      padding: 16px;
      margin-bottom: 10px;
      border: 1.5px solid #EEE;
  }
  .model-card-best {
      border-color: #6C3BFF;
  }
  .best-badge {
      float: right;
      background: #6C3BFF;
      color: white;
      font-size: 10px;
      font-weight: 700;
      border-radius: 8px;
      padding: 3px 8px;
      letter-spacing: 0.5px;
  }
  .model-brand { font-size: 10px; font-weight: 600; color: #888; text-transform: uppercase; letter-spacing: 0.8px; }
  .model-name { font-size: 16px; font-weight: 700; color: #111; margin: 2px 0 8px; }
  .model-price { font-size: 22px; font-weight: 800; color: #111; display: inline; }
  .model-diff-pos { font-size: 13px; font-weight: 600; color: #16A34A; float: right; }
  .model-diff-neg { font-size: 13px; font-weight: 600; color: #DC2626; float: right; }
  .model-specs {
      display: flex; flex-wrap: wrap; gap: 6px;
      margin: 10px 0;
  }
  .spec-chip {
      background: #F5F5F5;
      border-radius: 8px;
      padding: 3px 8px;
      font-size: 11px;
      color: #555;
      font-weight: 500;
  }
  .buy-row {
      display: flex; align-items: center; gap: 10px; margin-top: 10px;
  }
  .buy-label { font-size: 12px; color: #888; flex: 1; }
  .btn-amazon {
      background: #FF9900;
      color: white;
      border: none;
      border-radius: 20px;
      padding: 6px 14px;
      font-size: 12px;
      font-weight: 600;
      text-decoration: none;
  }
  .btn-flipkart {
      background: #2874F0;
      color: white;
      border: none;
      border-radius: 20px;
      padding: 6px 14px;
      font-size: 12px;
      font-weight: 600;
      text-decoration: none;
  }
  .model-rating { color: #888; font-size: 13px; }
  .model-top-row { display: flex; align-items: flex-start; justify-content: space-between; }
</style>
""", unsafe_allow_html=True)

PHONES = [
    dict(brand="Apple", model="iPhone 13", price=59900, ram="6GB", storage="128GB", camera="12MP", display="AMOLED/OLED", battery="3000mAh", five_g=True,  processor="Upper mid-range", rating=4.6, amazon="https://amzn.in/d/iphone13", flipkart="https://www.flipkart.com/search?q=iphone+13"),
    dict(brand="Apple", model="iPhone 14", price=69900, ram="6GB", storage="128GB", camera="12MP", display="AMOLED/OLED", battery="3000mAh", five_g=True,  processor="Upper mid-range", rating=4.7, amazon="https://amzn.in/d/iphone14", flipkart="https://www.flipkart.com/search?q=iphone+14"),
    dict(brand="Apple", model="iPhone 14 Plus", price=79900, ram="6GB", storage="128GB", camera="12MP", display="AMOLED/OLED", battery="4000mAh", five_g=True,  processor="Upper mid-range", rating=4.5, amazon="https://amzn.in/d/iphone14plus", flipkart="https://www.flipkart.com/search?q=iphone+14+plus"),
    dict(brand="Apple", model="iPhone 15", price=79900, ram="6GB", storage="128GB", camera="48MP", display="AMOLED/OLED", battery="3000mAh", five_g=True,  processor="Flagship", rating=4.7, amazon="https://amzn.in/d/iphone15", flipkart="https://www.flipkart.com/search?q=iphone+15"),
    dict(brand="Apple", model="iPhone 15 Plus", price=89900, ram="6GB", storage="256GB", camera="48MP", display="AMOLED/OLED", battery="4000mAh", five_g=True,  processor="Flagship", rating=4.6, amazon="https://amzn.in/d/iphone15plus", flipkart="https://www.flipkart.com/search?q=iphone+15+plus"),
    dict(brand="Apple", model="iPhone 15 Pro", price=134900, ram="8GB", storage="256GB", camera="48MP", display="AMOLED/OLED", battery="3000mAh", five_g=True,  processor="Flagship", rating=4.8, amazon="https://amzn.in/d/iphone15pro", flipkart="https://www.flipkart.com/search?q=iphone+15+pro"),
    dict(brand="Samsung", model="Galaxy A35 5G", price=26999, ram="6GB", storage="128GB", camera="50MP", display="AMOLED/OLED", battery="5000mAh", five_g=True,  processor="Mid-range", rating=4.3, amazon="https://amzn.in/d/galaxya35", flipkart="https://www.flipkart.com/search?q=samsung+galaxy+a35"),
    dict(brand="Samsung", model="Galaxy A54 5G", price=38999, ram="8GB", storage="128GB", camera="50MP", display="AMOLED/OLED", battery="5000mAh", five_g=True,  processor="Upper mid-range", rating=4.4, amazon="https://amzn.in/d/galaxya54", flipkart="https://www.flipkart.com/search?q=samsung+galaxy+a54"),
    dict(brand="Samsung", model="Galaxy S23", price=74999, ram="8GB", storage="128GB", camera="50MP", display="AMOLED/OLED", battery="3000mAh", five_g=True,  processor="Flagship", rating=4.6, amazon="https://amzn.in/d/galaxys23", flipkart="https://www.flipkart.com/search?q=samsung+galaxy+s23"),
    dict(brand="Samsung", model="Galaxy S24", price=79999, ram="8GB", storage="256GB", camera="50MP", display="AMOLED/OLED", battery="4000mAh", five_g=True,  processor="Flagship", rating=4.7, amazon="https://amzn.in/d/galaxys24", flipkart="https://www.flipkart.com/search?q=samsung+galaxy+s24"),
    dict(brand="Samsung", model="Galaxy M34 5G", price=17999, ram="6GB", storage="128GB", camera="50MP", display="AMOLED/OLED", battery="5000mAh", five_g=True,  processor="Mid-range", rating=4.2, amazon="https://amzn.in/d/galaxym34", flipkart="https://www.flipkart.com/search?q=samsung+galaxy+m34"),
    dict(brand="OnePlus", model="OnePlus Nord CE 3 Lite", price=19999, ram="8GB", storage="128GB", camera="108MP", display="FHD+ LCD", battery="5000mAh", five_g=True,  processor="Mid-range", rating=4.1, amazon="https://amzn.in/d/oneplusnordce3lite", flipkart="https://www.flipkart.com/search?q=oneplus+nord+ce+3+lite"),
    dict(brand="OnePlus", model="OnePlus Nord 4", price=29999, ram="8GB", storage="256GB", camera="50MP", display="AMOLED/OLED", battery="5000mAh", five_g=True,  processor="Upper mid-range", rating=4.4, amazon="https://amzn.in/d/oneplusnord4", flipkart="https://www.flipkart.com/search?q=oneplus+nord+4"),
    dict(brand="OnePlus", model="OnePlus 12R", price=39999, ram="8GB", storage="128GB", camera="50MP", display="AMOLED/OLED", battery="5000mAh", five_g=True,  processor="Upper mid-range", rating=4.5, amazon="https://amzn.in/d/oneplus12r", flipkart="https://www.flipkart.com/search?q=oneplus+12r"),
    dict(brand="OnePlus", model="OnePlus 12", price=64999, ram="12GB", storage="256GB", camera="50MP", display="AMOLED/OLED", battery="5000mAh", five_g=True,  processor="Flagship", rating=4.7, amazon="https://amzn.in/d/oneplus12", flipkart="https://www.flipkart.com/search?q=oneplus+12"),
    dict(brand="Xiaomi", model="Redmi 13C", price=9999,  ram="4GB", storage="128GB", camera="50MP", display="HD+ LCD", battery="5000mAh", five_g=False, processor="Entry-level", rating=3.9, amazon="https://amzn.in/d/redmi13c", flipkart="https://www.flipkart.com/search?q=redmi+13c"),
    dict(brand="Xiaomi", model="Redmi Note 13 5G", price=17999, ram="6GB", storage="128GB", camera="108MP", display="AMOLED/OLED", battery="5000mAh", five_g=True,  processor="Mid-range", rating=4.2, amazon="https://amzn.in/d/redminote135g", flipkart="https://www.flipkart.com/search?q=redmi+note+13+5g"),
    dict(brand="Xiaomi", model="Redmi Note 13 Pro+", price=29999, ram="8GB", storage="256GB", camera="200MP", display="AMOLED/OLED", battery="5000mAh", five_g=True,  processor="Upper mid-range", rating=4.4, amazon="https://amzn.in/d/redminote13proplus", flipkart="https://www.flipkart.com/search?q=redmi+note+13+pro+plus"),
    dict(brand="Xiaomi", model="Xiaomi 14", price=69999, ram="12GB", storage="256GB", camera="50MP", display="AMOLED/OLED", battery="4000mAh", five_g=True,  processor="Flagship", rating=4.6, amazon="https://amzn.in/d/xiaomi14", flipkart="https://www.flipkart.com/search?q=xiaomi+14"),
    dict(brand="Realme", model="Realme C65 5G", price=11999, ram="4GB", storage="128GB", camera="50MP", display="HD+ LCD", battery="5000mAh", five_g=True,  processor="Entry-level", rating=3.9, amazon="https://amzn.in/d/realmec65", flipkart="https://www.flipkart.com/search?q=realme+c65+5g"),
    dict(brand="Realme", model="Realme 12 Pro+", price=29999, ram="8GB", storage="256GB", camera="50MP", display="AMOLED/OLED", battery="5000mAh", five_g=True,  processor="Upper mid-range", rating=4.3, amazon="https://amzn.in/d/realme12proplus", flipkart="https://www.flipkart.com/search?q=realme+12+pro+plus"),
    dict(brand="Realme", model="Realme GT 6", price=49999, ram="12GB", storage="256GB", camera="50MP", display="AMOLED/OLED", battery="5000mAh", five_g=True,  processor="Flagship", rating=4.5, amazon="https://amzn.in/d/realmegt6", flipkart="https://www.flipkart.com/search?q=realme+gt+6"),
    dict(brand="POCO", model="POCO M6 Pro 5G", price=12999, ram="6GB", storage="128GB", camera="50MP", display="FHD+ LCD", battery="5000mAh", five_g=True,  processor="Mid-range", rating=4.1, amazon="https://amzn.in/d/pocom6pro", flipkart="https://www.flipkart.com/search?q=poco+m6+pro+5g"),
    dict(brand="POCO", model="POCO X6 Pro", price=26999, ram="8GB", storage="256GB", camera="64MP", display="AMOLED/OLED", battery="5000mAh", five_g=True,  processor="Upper mid-range", rating=4.4, amazon="https://amzn.in/d/pocox6pro", flipkart="https://www.flipkart.com/search?q=poco+x6+pro"),
    dict(brand="POCO", model="POCO F6", price=29999, ram="12GB", storage="256GB", camera="50MP", display="AMOLED/OLED", battery="5000mAh", five_g=True,  processor="Flagship", rating=4.5, amazon="https://amzn.in/d/pocof6", flipkart="https://www.flipkart.com/search?q=poco+f6"),
    dict(brand="Motorola", model="Moto G64 5G", price=14999, ram="8GB", storage="128GB", camera="50MP", display="FHD+ LCD", battery="5000mAh", five_g=True,  processor="Mid-range", rating=4.0, amazon="https://amzn.in/d/motog64", flipkart="https://www.flipkart.com/search?q=moto+g64+5g"),
    dict(brand="Motorola", model="Moto Edge 50 Pro", price=31999, ram="12GB", storage="256GB", camera="50MP", display="AMOLED/OLED", battery="4000mAh", five_g=True,  processor="Upper mid-range", rating=4.3, amazon="https://amzn.in/d/motoedge50pro", flipkart="https://www.flipkart.com/search?q=moto+edge+50+pro"),
]

BRANDS     = ["Apple", "Samsung", "Xiaomi", "OnePlus", "Realme", "POCO", "Motorola"]
PROCESSORS = ["Entry-level", "Mid-range", "Upper mid-range", "Flagship"]
RAMS       = ["2GB", "4GB", "6GB", "8GB", "12GB", "16GB"]
STORAGES   = ["32GB", "64GB", "128GB", "256GB", "512GB"]
CAMERAS    = ["8MP", "12MP", "13MP", "16MP", "48MP", "50MP", "108MP", "200MP"]
DISPLAYS   = ["HD+ LCD", "FHD+ LCD", "AMOLED/OLED", "120Hz AMOLED"]
BATTERIES  = ["3000mAh", "4000mAh", "4500mAh", "5000mAh", "5000mAh+"]

CATEGORY_MAP = {
    (0,     15000):  ("Budget",           "Great value everyday use"),
    (15000, 25000):  ("Mid-range",        "Balanced performance & features"),
    (25000, 40000):  ("Upper mid-range",  "Premium features, smart price"),
    (40000, 70000):  ("Premium",          "Flagship experience"),
    (70000, 999999): ("Flagship",         "Best-in-class everything"),
}


def estimate_price(brand, processor, ram, storage, camera, display, battery, five_g):
    base = {"Apple": 65000, "Samsung": 35000, "OnePlus": 28000,
            "Xiaomi": 14000, "Realme": 13000, "POCO": 14000, "Motorola": 16000}.get(brand, 20000)
    proc_mult = {"Entry-level": 0.55, "Mid-range": 0.80,
                 "Upper mid-range": 1.0, "Flagship": 1.5}.get(processor, 1.0)
    ram_add  = {"2GB": 0, "4GB": 500, "6GB": 1500, "8GB": 3500, "12GB": 7000, "16GB": 12000}.get(ram, 0)
    stor_add = {"32GB": 0, "64GB": 1000, "128GB": 2500, "256GB": 5000, "512GB": 10000}.get(storage, 0)
    cam_add  = {"8MP": 0, "12MP": 1000, "13MP": 1000, "16MP": 2000, "48MP": 4000,
                "50MP": 5000, "108MP": 8000, "200MP": 12000}.get(camera, 0)
    disp_add = {"HD+ LCD": 0, "FHD+ LCD": 2000, "AMOLED/OLED": 5000, "120Hz AMOLED": 8000}.get(display, 0)
    bat_add  = {"3000mAh": 0, "4000mAh": 500, "4500mAh": 800, "5000mAh": 1000, "5000mAh+": 1500}.get(battery, 0)
    five_g_add = 3000 if five_g else 0
    price = int((base * proc_mult) + ram_add + stor_add + cam_add + disp_add + bat_add + five_g_add)
    return round(price / 50) * 50


def get_category(price):
    for (lo, hi), (name, desc) in CATEGORY_MAP.items():
        if lo <= price < hi:
            return name, desc
    return "Flagship", "Best-in-class everything"


def score_phone(phone, brand, processor, ram, storage, camera, display, battery, five_g, target_price):
    score = 0
    if phone["brand"] == brand: score += 40
    if phone["processor"] == processor: score += 20
    elif abs(PROCESSORS.index(phone["processor"]) - PROCESSORS.index(processor)) == 1: score += 10
    if phone["ram"] == ram: score += 15
    if phone["storage"] == storage: score += 10
    if phone["display"] == display: score += 10
    if phone["five_g"] == five_g: score += 8
    diff = abs(phone["price"] - target_price)
    if diff < 5000: score += 15
    elif diff < 10000: score += 8
    elif diff < 20000: score += 3
    return score


def fmt_inr(n):
    s = str(int(n))
    return "₹" + (s[:-3] + "," + s[-3:] if len(s) > 3 else s)


def pill_radio(label, options, key, badge=True):
    st.markdown(f'<p class="field-label">{label}</p>', unsafe_allow_html=True)
    selected = st.radio("select", options, key=key, horizontal=True, label_visibility="hidden")
    if badge:
        st.markdown(f'<p style="margin-top:-12px;color:#6C3BFF;font-size:12px;font-weight:600;">{selected}</p>', unsafe_allow_html=True)
    return selected


# ── Hero ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero-card">
  <div class="hero-icon">📱</div>
  <p class="hero-title">Phone Price<br>Predictor</p>
  <p class="hero-sub">Select your desired specs and get an accurate price estimate in Indian Rupees</p>
</div>
""", unsafe_allow_html=True)

# ── Brand ─────────────────────────────────────────────────────────────────────
st.markdown('<div class="section-card"><div class="section-header"><div class="section-icon">🏷️</div><p class="section-title">Brand</p></div>', unsafe_allow_html=True)
selected_brand = pill_radio("Select Brand", BRANDS, key="brand")
st.markdown('</div>', unsafe_allow_html=True)

# ── Performance ───────────────────────────────────────────────────────────────
st.markdown('<div class="section-card"><div class="section-header"><div class="section-icon">⚙️</div><p class="section-title">Performance</p></div>', unsafe_allow_html=True)
selected_processor = pill_radio("Processor", PROCESSORS, key="processor")
selected_ram = pill_radio("RAM", RAMS, key="ram")
st.markdown('</div>', unsafe_allow_html=True)

# ── Storage ───────────────────────────────────────────────────────────────────
st.markdown('<div class="section-card"><div class="section-header"><div class="section-icon">💾</div><p class="section-title">Storage</p></div>', unsafe_allow_html=True)
selected_storage = pill_radio("Internal Storage", STORAGES, key="storage")
st.markdown('</div>', unsafe_allow_html=True)

# ── Camera ────────────────────────────────────────────────────────────────────
st.markdown('<div class="section-card"><div class="section-header"><div class="section-icon">📸</div><p class="section-title">Camera</p></div>', unsafe_allow_html=True)
selected_camera = pill_radio("Main Camera", CAMERAS, key="camera")
st.markdown('</div>', unsafe_allow_html=True)

# ── Display ───────────────────────────────────────────────────────────────────
st.markdown('<div class="section-card"><div class="section-header"><div class="section-icon">🖥️</div><p class="section-title">Display</p></div>', unsafe_allow_html=True)
selected_display = pill_radio("Display Type", DISPLAYS, key="display")
st.markdown('</div>', unsafe_allow_html=True)

# ── Battery & Connectivity ────────────────────────────────────────────────────
st.markdown('<div class="section-card"><div class="section-header"><div class="section-icon">🔋</div><p class="section-title">Battery &amp; Connectivity</p></div>', unsafe_allow_html=True)
selected_battery = pill_radio("Battery Capacity", BATTERIES, key="battery")
five_g = st.toggle("5G Connectivity", value=True)
if five_g:
    st.markdown('<p style="font-size:12px;color:#6C3BFF;margin-top:-8px;">Next-gen network support ✓</p>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ── Predict ───────────────────────────────────────────────────────────────────
predict = st.button("📈  Predict Price", use_container_width=True)

# ── Results ───────────────────────────────────────────────────────────────────
if predict:
    price = estimate_price(selected_brand, selected_processor, selected_ram,
                           selected_storage, selected_camera, selected_display,
                           selected_battery, five_g)
    min_price = int(price * 0.85)
    max_price = int(price * 1.15)
    category, cat_desc = get_category(price)

    st.markdown(f"""
    <div class="price-card">
      <div class="price-label-row">📈 &nbsp; Estimated Price</div>
      <p class="price-amount">{fmt_inr(price)}</p>
      <div class="price-badges">
        <span class="badge-filled">{category}</span>
        <span class="badge-outline">{cat_desc}</span>
      </div>
      <div class="range-row">
        <div class="range-item">
          <div class="range-item-label">MIN</div>
          <div class="range-item-value">{fmt_inr(min_price)}</div>
        </div>
        <div style="flex:1;height:4px;background:rgba(255,255,255,0.3);border-radius:2px;margin:0 12px;position:relative;">
          <div style="position:absolute;left:40%;top:-4px;width:12px;height:12px;background:white;border-radius:50%;"></div>
        </div>
        <div class="range-item">
          <div class="range-item-label">MAX</div>
          <div class="range-item-value">{fmt_inr(max_price)}</div>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    scored = sorted(
        [(score_phone(p, selected_brand, selected_processor, selected_ram,
                      selected_storage, selected_camera, selected_display,
                      selected_battery, five_g, price), p) for p in PHONES],
        key=lambda x: -x[0]
    )[:7]

    st.markdown(f"""
    <div class="models-header" style="margin-top:20px;">
      <div>
        <p class="models-title">Recommended Models</p>
        <p class="models-sub">Phones matching your budget &amp; specs</p>
      </div>
      <span class="models-count">{len(scored)}</span>
    </div>
    """, unsafe_allow_html=True)

    for i, (score, phone) in enumerate(scored):
        diff = phone["price"] - price
        diff_str  = (f'+{fmt_inr(diff)}' if diff > 0 else f'-{fmt_inr(abs(diff))}') if diff != 0 else ""
        diff_cls  = "model-diff-pos" if diff > 0 else "model-diff-neg"
        best_badge = '<span class="best-badge">BEST MATCH</span>' if i == 0 else ""
        card_class = "model-card model-card-best" if i == 0 else "model-card"
        five_g_chip = '<span class="spec-chip">5G</span>' if phone["five_g"] else ""

        st.markdown(f"""
        <div class="{card_class}">
          {best_badge}
          <div style="display:flex;align-items:center;gap:12px;margin-bottom:10px;">
            <div style="background:#EDE9FF;border-radius:12px;width:40px;height:40px;
                        display:flex;align-items:center;justify-content:center;
                        font-size:18px;font-weight:800;color:#6C3BFF;flex-shrink:0;">
              {phone["brand"][0]}
            </div>
            <div style="flex:1;min-width:0;">
              <div class="model-brand">{phone["brand"]}</div>
              <div class="model-name">{phone["model"]}</div>
            </div>
            <div style="text-align:right;flex-shrink:0;font-size:11px;color:#888;">☆ {phone["rating"]}</div>
          </div>
          <div style="display:flex;align-items:baseline;justify-content:space-between;">
            <span class="model-price">{fmt_inr(phone["price"])}</span>
            <span class="{diff_cls}">{diff_str}</span>
          </div>
          <div class="model-specs">
            <span class="spec-chip">⚙ {phone["ram"]} RAM</span>
            <span class="spec-chip">💾 {phone["storage"]}</span>
            <span class="spec-chip">📸 {phone["camera"]}</span>
            <span class="spec-chip">🔋 {phone["battery"]}</span>
            {five_g_chip}
          </div>
          <div class="buy-row">
            <span class="buy-label">Buy from</span>
            <a href="{phone["amazon"]}" target="_blank" class="btn-amazon">🛒 Amazon</a>
            <a href="{phone["flipkart"]}" target="_blank" class="btn-flipkart">🛍 Flipkart</a>
          </div>
        </div>
        """, unsafe_allow_html=True)
