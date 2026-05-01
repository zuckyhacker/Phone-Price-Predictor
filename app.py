import streamlit as st

st.set_page_config(
    page_title="Phone Price Predictor",
    page_icon="📱",
    layout="centered"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

* { font-family: 'Inter', sans-serif; box-sizing: border-box; }

.stApp { background: linear-gradient(160deg, #F0EEFF 0%, #E8E8F8 50%, #EEF0FF 100%); min-height: 100vh; }
header[data-testid="stHeader"] { background: transparent; }
[data-testid="stAppViewContainer"] > section > div { padding-top: 0 !important; }
div[data-testid="stVerticalBlock"] > div { gap: 0 !important; }

.hero {
    background: linear-gradient(145deg, #7C3AED 0%, #6D28D9 40%, #4C1D95 100%);
    border-radius: 0 0 32px 32px;
    padding: 36px 24px 32px;
    margin: -16px -16px 0 -16px;
    position: relative; overflow: hidden;
}
.hero::before {
    content: ''; position: absolute; inset: 0;
    background: radial-gradient(ellipse at 80% 20%, rgba(167,139,250,0.35) 0%, transparent 60%),
                radial-gradient(ellipse at 20% 80%, rgba(109,40,217,0.4) 0%, transparent 60%);
}
.hero-inner { position: relative; z-index: 1; }
.hero-badge {
    display: inline-flex; align-items: center; gap: 6px;
    background: rgba(255,255,255,0.15); border: 1px solid rgba(255,255,255,0.25);
    border-radius: 20px; padding: 5px 12px; font-size: 12px; color: rgba(255,255,255,0.9);
    font-weight: 600; letter-spacing: 0.3px; margin-bottom: 14px; backdrop-filter: blur(8px);
}
.hero-title { font-size: 34px; font-weight: 900; color: white; line-height: 1.08; margin: 0 0 10px; letter-spacing: -0.5px; }
.hero-sub { color: rgba(255,255,255,0.7); font-size: 14px; margin: 0 0 20px; line-height: 1.5; }
.hero-stats { display: flex; gap: 16px; }
.hero-stat {
    background: rgba(255,255,255,0.12); border: 1px solid rgba(255,255,255,0.2);
    border-radius: 12px; padding: 10px 16px; flex: 1; text-align: center; backdrop-filter: blur(8px);
}
.hero-stat-num { font-size: 20px; font-weight: 800; color: white; }
.hero-stat-label { font-size: 10px; color: rgba(255,255,255,0.65); font-weight: 500; margin-top: 1px; }

.card {
    background: white; border-radius: 20px; padding: 20px 20px 16px; margin-bottom: 12px;
    box-shadow: 0 2px 12px rgba(100,80,200,0.08), 0 1px 3px rgba(0,0,0,0.05);
    border: 1px solid rgba(200,190,255,0.3); transition: box-shadow 0.2s;
}
.card:hover { box-shadow: 0 4px 20px rgba(100,80,200,0.13), 0 1px 4px rgba(0,0,0,0.06); }
.card-head { display: flex; align-items: center; justify-content: space-between; margin-bottom: 14px; }
.card-left { display: flex; align-items: center; gap: 11px; }
.card-icon {
    width: 38px; height: 38px; border-radius: 11px;
    background: linear-gradient(135deg, #EDE9FF, #DDD6FE);
    display: flex; align-items: center; justify-content: center; font-size: 17px; flex-shrink: 0;
}
.card-title { font-size: 16px; font-weight: 700; color: #1a1a2e; }
.card-sel-badge {
    background: linear-gradient(135deg, #7C3AED, #6D28D9);
    color: white; font-size: 11px; font-weight: 700;
    border-radius: 20px; padding: 4px 12px;
    white-space: nowrap; max-width: 180px;
    overflow: hidden; text-overflow: ellipsis; flex-shrink: 0;
}
.field-label { font-size: 13px; font-weight: 700; color: #374151; margin: 12px 0 8px; letter-spacing: 0.1px; }

div[data-testid="stRadio"] > div { flex-direction: row !important; flex-wrap: wrap; gap: 6px; }
div[data-testid="stRadio"] label {
    background: #F8F7FF !important; border: 1.5px solid #E5E1FF !important;
    border-radius: 22px !important; padding: 7px 15px !important;
    font-size: 13px !important; font-weight: 500 !important; color: #444 !important;
    cursor: pointer !important; transition: all 0.15s !important; margin: 0 !important;
}
div[data-testid="stRadio"] label:hover {
    border-color: #7C3AED !important; color: #7C3AED !important; background: #F3F0FF !important;
}
div[data-testid="stRadio"] label:has(input:checked) {
    background: linear-gradient(135deg, #7C3AED, #6D28D9) !important;
    border-color: transparent !important; color: white !important;
    font-weight: 700 !important; box-shadow: 0 3px 10px rgba(124,58,237,0.35) !important;
}
div[data-testid="stRadio"] input[type="radio"] {
    position: absolute; opacity: 0; width: 0; height: 0; pointer-events: none;
}
div[data-testid="stRadio"] [data-testid="stMarkdownContainer"] p { display: none; }

.toggle-wrap {
    background: linear-gradient(135deg, #F5F3FF, #EDE9FF);
    border: 1.5px solid #DDD6FE; border-radius: 14px;
    padding: 13px 16px; margin-top: 10px; display: flex; align-items: center; gap: 12px;
}
.toggle-text-title { font-size: 14px; font-weight: 700; color: #5B21B6; }
.toggle-text-sub { font-size: 11px; color: #8B5CF6; margin-top: 1px; }

.summary-card {
    background: linear-gradient(135deg, #1E1B4B, #2D1B69);
    border-radius: 20px; padding: 20px; margin-bottom: 14px;
    box-shadow: 0 8px 24px rgba(30,27,75,0.25);
}
.summary-title { font-size: 13px; font-weight: 700; color: rgba(255,255,255,0.6); letter-spacing: 1px; text-transform: uppercase; margin-bottom: 14px; }
.summary-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; }
.summary-item {
    background: rgba(255,255,255,0.08); border: 1px solid rgba(255,255,255,0.12);
    border-radius: 11px; padding: 9px 12px;
}
.summary-item-label { font-size: 10px; color: rgba(255,255,255,0.5); font-weight: 600; letter-spacing: 0.5px; text-transform: uppercase; margin-bottom: 3px; }
.summary-item-value { font-size: 13px; color: white; font-weight: 700; }

div[data-testid="stButton"] > button {
    width: 100%;
    background: linear-gradient(135deg, #7C3AED 0%, #6D28D9 50%, #5B21B6 100%);
    color: white; font-size: 16px; font-weight: 700;
    border: none; border-radius: 16px; padding: 16px 24px;
    cursor: pointer; letter-spacing: 0.2px;
    box-shadow: 0 6px 20px rgba(109,40,217,0.4); transition: all 0.2s;
}
div[data-testid="stButton"] > button:hover { transform: translateY(-1px); box-shadow: 0 10px 28px rgba(109,40,217,0.5); }
div[data-testid="stButton"] > button:active { transform: translateY(0); }
div[data-testid="stToggle"] label { font-size: 14px; font-weight: 600; color: #5B21B6; }

.price-hero {
    background: linear-gradient(145deg, #7C3AED 0%, #5B21B6 50%, #3B0764 100%);
    border-radius: 24px; padding: 28px 24px; margin-bottom: 14px;
    box-shadow: 0 12px 32px rgba(109,40,217,0.4); position: relative; overflow: hidden;
}
.price-hero::after {
    content: ''; position: absolute; top: -40px; right: -40px;
    width: 160px; height: 160px; border-radius: 50%; background: rgba(167,139,250,0.15);
}
.price-hero-inner { position: relative; z-index: 1; }
.price-eyebrow { font-size: 11px; font-weight: 700; color: rgba(255,255,255,0.6); letter-spacing: 1.5px; text-transform: uppercase; margin-bottom: 6px; }
.price-amount { font-size: 48px; font-weight: 900; color: white; letter-spacing: -1px; margin: 0 0 4px; line-height: 1; }
.price-brand-note { font-size: 13px; color: rgba(255,255,255,0.65); margin-bottom: 16px; }
.price-badges { display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 20px; }
.badge-cat { background: rgba(255,255,255,0.95); color: #7C3AED; font-size: 12px; font-weight: 800; border-radius: 20px; padding: 5px 14px; }
.badge-desc { background: rgba(255,255,255,0.12); color: rgba(255,255,255,0.9); font-size: 12px; font-weight: 500; border-radius: 20px; padding: 5px 14px; border: 1px solid rgba(255,255,255,0.2); }
.range-box { background: rgba(0,0,0,0.25); border-radius: 14px; padding: 14px 16px; display: flex; align-items: center; gap: 12px; }
.range-col { flex: 1; }
.range-col-label { font-size: 9px; color: rgba(255,255,255,0.5); font-weight: 700; letter-spacing: 1px; text-transform: uppercase; margin-bottom: 3px; }
.range-col-val { font-size: 16px; font-weight: 800; color: white; }
.range-divider { width: 1px; height: 32px; background: rgba(255,255,255,0.2); }
.range-mid { flex: 2; padding: 0 8px; }
.range-track { height: 4px; background: rgba(255,255,255,0.2); border-radius: 2px; position: relative; }
.range-dot { position: absolute; left: 45%; top: -5px; width: 14px; height: 14px; background: white; border-radius: 50%; box-shadow: 0 0 0 3px rgba(255,255,255,0.3); }

.models-hdr { display: flex; justify-content: space-between; align-items: flex-end; margin: 20px 0 12px; }
.models-hdr-title { font-size: 20px; font-weight: 800; color: #1a1a2e; }
.models-hdr-sub { font-size: 12px; color: #888; margin-top: 2px; }
.models-count-badge { background: linear-gradient(135deg, #7C3AED, #6D28D9); color: white; font-size: 13px; font-weight: 800; border-radius: 10px; padding: 4px 12px; }
.model-card {
    background: white; border-radius: 18px; padding: 16px;
    margin-bottom: 10px; border: 1.5px solid #F0EEFF;
    box-shadow: 0 2px 10px rgba(100,80,200,0.07); transition: box-shadow 0.2s, transform 0.15s;
}
.model-card:hover { box-shadow: 0 6px 20px rgba(100,80,200,0.14); transform: translateY(-1px); }
.model-card-best { border-color: #7C3AED; box-shadow: 0 4px 16px rgba(124,58,237,0.18); }
.best-chip {
    display: inline-block; background: linear-gradient(135deg, #7C3AED, #6D28D9);
    color: white; font-size: 9px; font-weight: 800;
    border-radius: 6px; padding: 3px 8px; letter-spacing: 0.8px;
    vertical-align: middle; margin-left: 6px;
}
.model-top { display: flex; align-items: flex-start; gap: 12px; margin-bottom: 10px; }
.model-avatar {
    width: 44px; height: 44px; border-radius: 13px;
    background: linear-gradient(135deg, #EDE9FF, #DDD6FE);
    display: flex; align-items: center; justify-content: center;
    font-size: 19px; font-weight: 900; color: #7C3AED; flex-shrink: 0;
}
.model-brand-name { font-size: 10px; font-weight: 700; color: #9CA3AF; letter-spacing: 0.8px; text-transform: uppercase; }
.model-name { font-size: 15px; font-weight: 800; color: #111827; margin: 2px 0; }
.model-rating-row { display: flex; align-items: center; gap: 4px; }
.rating-num { font-size: 11px; color: #6B7280; font-weight: 600; }
.model-price-row { display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 10px; }
.model-price { font-size: 24px; font-weight: 900; color: #111827; }
.diff-pos { font-size: 12px; font-weight: 700; color: #059669; background: #ECFDF5; border-radius: 8px; padding: 3px 8px; }
.diff-neg { font-size: 12px; font-weight: 700; color: #DC2626; background: #FEF2F2; border-radius: 8px; padding: 3px 8px; }
.diff-zero { font-size: 12px; font-weight: 700; color: #7C3AED; background: #EDE9FF; border-radius: 8px; padding: 3px 8px; }
.spec-row { display: flex; flex-wrap: wrap; gap: 5px; margin-bottom: 12px; }
.spec-pill {
    background: #F9F9FF; border: 1px solid #EDE9FF; border-radius: 8px; padding: 4px 9px;
    font-size: 11px; color: #4B5563; font-weight: 600; display: flex; align-items: center; gap: 4px;
}
.buy-row { display: flex; align-items: center; gap: 8px; padding-top: 10px; border-top: 1px solid #F3F4F6; }
.buy-label { font-size: 11px; color: #9CA3AF; flex: 1; font-weight: 600; }
.buy-amazon {
    background: linear-gradient(135deg, #FF9900, #F08000); color: white; text-decoration: none;
    border-radius: 22px; padding: 7px 14px; font-size: 12px; font-weight: 700;
    box-shadow: 0 2px 8px rgba(255,153,0,0.3);
}
.buy-flipkart {
    background: linear-gradient(135deg, #2874F0, #1a5fd4); color: white; text-decoration: none;
    border-radius: 22px; padding: 7px 14px; font-size: 12px; font-weight: 700;
    box-shadow: 0 2px 8px rgba(40,116,240,0.3);
}
.divider { height: 1px; background: linear-gradient(90deg, transparent, #DDD6FE, transparent); margin: 4px 0 14px; }
.footer { text-align: center; padding: 20px 0 8px; color: #A0A0B0; font-size: 11px; }
</style>
""", unsafe_allow_html=True)

PHONES = [
    dict(brand="Apple",    model="iPhone 13",            price=59900,  ram="6GB",  storage="128GB", camera="12MP",  display="AMOLED/OLED",  battery="3000mAh", five_g=True,  processor="Upper mid-range", rating=4.6),
    dict(brand="Apple",    model="iPhone 14",            price=69900,  ram="6GB",  storage="128GB", camera="12MP",  display="AMOLED/OLED",  battery="3000mAh", five_g=True,  processor="Upper mid-range", rating=4.7),
    dict(brand="Apple",    model="iPhone 14 Plus",       price=79900,  ram="6GB",  storage="128GB", camera="12MP",  display="AMOLED/OLED",  battery="4000mAh", five_g=True,  processor="Upper mid-range", rating=4.5),
    dict(brand="Apple",    model="iPhone 15",            price=79900,  ram="6GB",  storage="128GB", camera="48MP",  display="AMOLED/OLED",  battery="3000mAh", five_g=True,  processor="Flagship",        rating=4.7),
    dict(brand="Apple",    model="iPhone 15 Plus",       price=89900,  ram="6GB",  storage="256GB", camera="48MP",  display="AMOLED/OLED",  battery="4000mAh", five_g=True,  processor="Flagship",        rating=4.6),
    dict(brand="Apple",    model="iPhone 15 Pro",        price=134900, ram="8GB",  storage="256GB", camera="48MP",  display="AMOLED/OLED",  battery="3000mAh", five_g=True,  processor="Flagship",        rating=4.8),
    dict(brand="Samsung",  model="Galaxy M34 5G",        price=17999,  ram="6GB",  storage="128GB", camera="50MP",  display="AMOLED/OLED",  battery="5000mAh", five_g=True,  processor="Mid-range",       rating=4.2),
    dict(brand="Samsung",  model="Galaxy A35 5G",        price=26999,  ram="6GB",  storage="128GB", camera="50MP",  display="AMOLED/OLED",  battery="5000mAh", five_g=True,  processor="Mid-range",       rating=4.3),
    dict(brand="Samsung",  model="Galaxy A54 5G",        price=38999,  ram="8GB",  storage="128GB", camera="50MP",  display="AMOLED/OLED",  battery="5000mAh", five_g=True,  processor="Upper mid-range", rating=4.4),
    dict(brand="Samsung",  model="Galaxy S23",           price=74999,  ram="8GB",  storage="128GB", camera="50MP",  display="AMOLED/OLED",  battery="3000mAh", five_g=True,  processor="Flagship",        rating=4.6),
    dict(brand="Samsung",  model="Galaxy S24",           price=79999,  ram="8GB",  storage="256GB", camera="50MP",  display="AMOLED/OLED",  battery="4000mAh", five_g=True,  processor="Flagship",        rating=4.7),
    dict(brand="OnePlus",  model="Nord CE 3 Lite",       price=19999,  ram="8GB",  storage="128GB", camera="108MP", display="FHD+ LCD",     battery="5000mAh", five_g=True,  processor="Mid-range",       rating=4.1),
    dict(brand="OnePlus",  model="Nord 4",               price=29999,  ram="8GB",  storage="256GB", camera="50MP",  display="AMOLED/OLED",  battery="5000mAh", five_g=True,  processor="Upper mid-range", rating=4.4),
    dict(brand="OnePlus",  model="OnePlus 12R",          price=39999,  ram="8GB",  storage="128GB", camera="50MP",  display="AMOLED/OLED",  battery="5000mAh", five_g=True,  processor="Upper mid-range", rating=4.5),
    dict(brand="OnePlus",  model="OnePlus 12",           price=64999,  ram="12GB", storage="256GB", camera="50MP",  display="AMOLED/OLED",  battery="5000mAh", five_g=True,  processor="Flagship",        rating=4.7),
    dict(brand="Xiaomi",   model="Redmi 13C",            price=9999,   ram="4GB",  storage="128GB", camera="50MP",  display="HD+ LCD",      battery="5000mAh", five_g=False, processor="Entry-level",     rating=3.9),
    dict(brand="Xiaomi",   model="Redmi Note 13 5G",     price=17999,  ram="6GB",  storage="128GB", camera="108MP", display="AMOLED/OLED",  battery="5000mAh", five_g=True,  processor="Mid-range",       rating=4.2),
    dict(brand="Xiaomi",   model="Redmi Note 13 Pro+",   price=29999,  ram="8GB",  storage="256GB", camera="200MP", display="AMOLED/OLED",  battery="5000mAh", five_g=True,  processor="Upper mid-range", rating=4.4),
    dict(brand="Xiaomi",   model="Xiaomi 14",            price=69999,  ram="12GB", storage="256GB", camera="50MP",  display="AMOLED/OLED",  battery="4000mAh", five_g=True,  processor="Flagship",        rating=4.6),
    dict(brand="Realme",   model="Realme C65 5G",        price=11999,  ram="4GB",  storage="128GB", camera="50MP",  display="HD+ LCD",      battery="5000mAh", five_g=True,  processor="Entry-level",     rating=3.9),
    dict(brand="Realme",   model="Realme 12 Pro+",       price=29999,  ram="8GB",  storage="256GB", camera="50MP",  display="AMOLED/OLED",  battery="5000mAh", five_g=True,  processor="Upper mid-range", rating=4.3),
    dict(brand="Realme",   model="Realme GT 6",          price=49999,  ram="12GB", storage="256GB", camera="50MP",  display="AMOLED/OLED",  battery="5000mAh", five_g=True,  processor="Flagship",        rating=4.5),
    dict(brand="POCO",     model="POCO M6 Pro 5G",       price=12999,  ram="6GB",  storage="128GB", camera="50MP",  display="FHD+ LCD",     battery="5000mAh", five_g=True,  processor="Mid-range",       rating=4.1),
    dict(brand="POCO",     model="POCO X6 Pro",          price=26999,  ram="8GB",  storage="256GB", camera="64MP",  display="AMOLED/OLED",  battery="5000mAh", five_g=True,  processor="Upper mid-range", rating=4.4),
    dict(brand="POCO",     model="POCO F6",              price=29999,  ram="12GB", storage="256GB", camera="50MP",  display="AMOLED/OLED",  battery="5000mAh", five_g=True,  processor="Flagship",        rating=4.5),
    dict(brand="Motorola", model="Moto G64 5G",          price=14999,  ram="8GB",  storage="128GB", camera="50MP",  display="FHD+ LCD",     battery="5000mAh", five_g=True,  processor="Mid-range",       rating=4.0),
    dict(brand="Motorola", model="Moto Edge 50 Pro",     price=31999,  ram="12GB", storage="256GB", camera="50MP",  display="AMOLED/OLED",  battery="4000mAh", five_g=True,  processor="Upper mid-range", rating=4.3),
]

BRANDS     = ["Apple", "Samsung", "Xiaomi", "OnePlus", "Realme", "POCO", "Motorola"]
PROCESSORS = ["Entry-level", "Mid-range", "Upper mid-range", "Flagship"]
RAMS       = ["2GB", "4GB", "6GB", "8GB", "12GB", "16GB"]
STORAGES   = ["32GB", "64GB", "128GB", "256GB", "512GB"]
CAMERAS    = ["8MP", "12MP", "13MP", "16MP", "48MP", "50MP", "108MP", "200MP"]
DISPLAYS   = ["HD+ LCD", "FHD+ LCD", "AMOLED/OLED", "120Hz AMOLED"]
BATTERIES  = ["3000mAh", "4000mAh", "4500mAh", "5000mAh", "5000mAh+"]

BRAND_EMOJI = {"Apple":"🍎","Samsung":"🌟","Xiaomi":"🔴","OnePlus":"➕","Realme":"🟡","POCO":"⚡","Motorola":"🦋"}

CATEGORY_MAP = [
    (0,     15000,  "Budget",          "Great value everyday use",        "#10B981"),
    (15000, 25000,  "Mid-range",       "Balanced performance & features", "#3B82F6"),
    (25000, 40000,  "Upper mid-range", "Premium features, smart price",   "#8B5CF6"),
    (40000, 70000,  "Premium",         "Flagship-level experience",       "#F59E0B"),
    (70000, 999999, "Flagship",        "Best-in-class everything",        "#EF4444"),
]


def estimate_price(brand, processor, ram, storage, camera, display, battery, five_g):
    base = {"Apple":65000,"Samsung":35000,"OnePlus":28000,"Xiaomi":14000,"Realme":13000,"POCO":14000,"Motorola":16000}.get(brand,20000)
    pm   = {"Entry-level":0.55,"Mid-range":0.80,"Upper mid-range":1.0,"Flagship":1.5}.get(processor,1.0)
    r    = {"2GB":0,"4GB":500,"6GB":1500,"8GB":3500,"12GB":7000,"16GB":12000}.get(ram,0)
    s    = {"32GB":0,"64GB":1000,"128GB":2500,"256GB":5000,"512GB":10000}.get(storage,0)
    c    = {"8MP":0,"12MP":1000,"13MP":1000,"16MP":2000,"48MP":4000,"50MP":5000,"108MP":8000,"200MP":12000}.get(camera,0)
    d    = {"HD+ LCD":0,"FHD+ LCD":2000,"AMOLED/OLED":5000,"120Hz AMOLED":8000}.get(display,0)
    b    = {"3000mAh":0,"4000mAh":500,"4500mAh":800,"5000mAh":1000,"5000mAh+":1500}.get(battery,0)
    return round(int(base*pm + r + s + c + d + b + (3000 if five_g else 0)) / 50) * 50


def get_category(price):
    for lo,hi,name,desc,color in CATEGORY_MAP:
        if lo <= price < hi:
            return name, desc, color
    return "Flagship","Best-in-class everything","#EF4444"


def score_phone(phone, brand, processor, ram, storage, camera, display, five_g, target):
    sc = 0
    if phone["brand"] == brand: sc += 40
    pi = PROCESSORS.index(phone["processor"]); ti = PROCESSORS.index(processor)
    if pi == ti: sc += 20
    elif abs(pi-ti) == 1: sc += 10
    if phone["ram"]     == ram:     sc += 15
    if phone["storage"] == storage: sc += 10
    if phone["display"] == display: sc += 10
    if phone["five_g"]  == five_g:  sc += 8
    diff = abs(phone["price"] - target)
    sc += 15 if diff < 5000 else 8 if diff < 10000 else 3 if diff < 20000 else 0
    return sc


def fmt_inr(n):
    s = str(int(n))
    return "₹" + (s[:-3]+","+s[-3:] if len(s)>3 else s)


def pill_radio(label, options, key):
    st.markdown(f'<p class="field-label">{label}</p>', unsafe_allow_html=True)
    val = st.radio("x", options, key=key, horizontal=True, label_visibility="hidden")
    return val


def card_head(icon, title, badge):
    return (
        f'<div class="card"><div class="card-head">'
        f'<div class="card-left"><div class="card-icon">{icon}</div>'
        f'<span class="card-title">{title}</span></div>'
        f'<span class="card-sel-badge">{badge}</span>'
        f'</div>'
    )


# ── Hero ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
  <div class="hero-inner">
    <div class="hero-badge">📱 &nbsp; AI-Powered Estimator</div>
    <p class="hero-title">Phone Price<br>Predictor</p>
    <p class="hero-sub">Pick your specs and get an instant price estimate<br>with top phone recommendations in Indian Rupees</p>
    <div class="hero-stats">
      <div class="hero-stat"><div class="hero-stat-num">27+</div><div class="hero-stat-label">Phones</div></div>
      <div class="hero-stat"><div class="hero-stat-num">7</div><div class="hero-stat-label">Brands</div></div>
      <div class="hero-stat"><div class="hero-stat-num">INR</div><div class="hero-stat-label">Currency</div></div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div style="height:16px;"></div>', unsafe_allow_html=True)

# ── Read current selections from session state ────────────────────────────────
ss = st.session_state
_brand     = ss.get("brand",     BRANDS[0])
_processor = ss.get("processor", PROCESSORS[0])
_ram       = ss.get("ram",       RAMS[0])
_storage   = ss.get("storage",   STORAGES[0])
_camera    = ss.get("camera",    CAMERAS[0])
_display   = ss.get("display",   DISPLAYS[0])
_battery   = ss.get("battery",   BATTERIES[0])
_five_g    = ss.get("5g",        True)

# ── Inputs ────────────────────────────────────────────────────────────────────
st.markdown(card_head("🏷️", "Brand", f"{BRAND_EMOJI.get(_brand,'')} {_brand}"), unsafe_allow_html=True)
selected_brand = pill_radio("Select Brand", BRANDS, "brand")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown(card_head("⚙️", "Performance", f"{_processor} · {_ram}"), unsafe_allow_html=True)
selected_processor = pill_radio("Processor", PROCESSORS, "processor")
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
selected_ram = pill_radio("RAM", RAMS, "ram")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown(card_head("💾", "Storage", _storage), unsafe_allow_html=True)
selected_storage = pill_radio("Internal Storage", STORAGES, "storage")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown(card_head("📸", "Camera", _camera), unsafe_allow_html=True)
selected_camera = pill_radio("Main Camera (MP)", CAMERAS, "camera")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown(card_head("🖥️", "Display", _display), unsafe_allow_html=True)
selected_display = pill_radio("Display Type", DISPLAYS, "display")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown(card_head("🔋", "Battery &amp; Connectivity", f"{_battery} · {'5G' if _five_g else '4G'}"), unsafe_allow_html=True)
selected_battery = pill_radio("Battery Capacity", BATTERIES, "battery")
st.markdown('<div class="toggle-wrap">', unsafe_allow_html=True)
col_t, col_s = st.columns([4, 1])
with col_t:
    st.markdown('<div class="toggle-text-title">📶 &nbsp; 5G Connectivity</div><div class="toggle-text-sub">Next-generation network support</div>', unsafe_allow_html=True)
with col_s:
    five_g = st.toggle("5g", value=True, label_visibility="hidden")
st.markdown('</div></div>', unsafe_allow_html=True)

# ── Specs summary card ────────────────────────────────────────────────────────
st.markdown(f"""
<div class="summary-card">
  <div class="summary-title">Your Selected Specs</div>
  <div class="summary-grid">
    <div class="summary-item">
      <div class="summary-item-label">Brand</div>
      <div class="summary-item-value">{BRAND_EMOJI.get(selected_brand,"")} {selected_brand}</div>
    </div>
    <div class="summary-item">
      <div class="summary-item-label">Processor</div>
      <div class="summary-item-value">{selected_processor}</div>
    </div>
    <div class="summary-item">
      <div class="summary-item-label">RAM</div>
      <div class="summary-item-value">{selected_ram}</div>
    </div>
    <div class="summary-item">
      <div class="summary-item-label">Storage</div>
      <div class="summary-item-value">{selected_storage}</div>
    </div>
    <div class="summary-item">
      <div class="summary-item-label">Camera</div>
      <div class="summary-item-value">{selected_camera}</div>
    </div>
    <div class="summary-item">
      <div class="summary-item-label">Display</div>
      <div class="summary-item-value">{selected_display}</div>
    </div>
    <div class="summary-item">
      <div class="summary-item-label">Battery</div>
      <div class="summary-item-value">{selected_battery}</div>
    </div>
    <div class="summary-item">
      <div class="summary-item-label">Connectivity</div>
      <div class="summary-item-value">{"5G ✓" if five_g else "4G"}</div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# ── Predict button ────────────────────────────────────────────────────────────
predict = st.button("📈   Predict Price Now", use_container_width=True)

# ── Results ───────────────────────────────────────────────────────────────────
if predict:
    price = estimate_price(selected_brand, selected_processor, selected_ram,
                           selected_storage, selected_camera, selected_display,
                           selected_battery, five_g)
    lo = int(price * 0.85); hi = int(price * 1.15)
    cat, desc, cat_color = get_category(price)

    st.markdown('<div style="height:12px;"></div>', unsafe_allow_html=True)

    st.markdown(f"""
    <div class="price-hero">
      <div class="price-hero-inner">
        <div class="price-eyebrow">Estimated Price</div>
        <div class="price-amount">{fmt_inr(price)}</div>
        <div class="price-brand-note">Based on {selected_brand} · {selected_processor} tier</div>
        <div class="price-badges">
          <span class="badge-cat">{cat}</span>
          <span class="badge-desc">{desc}</span>
          {"<span class='badge-desc'>5G Ready</span>" if five_g else ""}
        </div>
        <div class="range-box">
          <div class="range-col">
            <div class="range-col-label">Min</div>
            <div class="range-col-val">{fmt_inr(lo)}</div>
          </div>
          <div class="range-divider"></div>
          <div class="range-mid">
            <div class="range-track"><div class="range-dot"></div></div>
          </div>
          <div class="range-divider"></div>
          <div class="range-col" style="text-align:right;">
            <div class="range-col-label">Max</div>
            <div class="range-col-val">{fmt_inr(hi)}</div>
          </div>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    ranked = sorted(
        [(score_phone(p, selected_brand, selected_processor, selected_ram,
                      selected_storage, selected_camera, selected_display, five_g, price), p)
         for p in PHONES],
        key=lambda x: -x[0]
    )[:7]

    st.markdown(f"""
    <div class="models-hdr">
      <div>
        <div class="models-hdr-title">Recommended Models</div>
        <div class="models-hdr-sub">Phones matching your budget &amp; specs</div>
      </div>
      <span class="models-count-badge">{len(ranked)}</span>
    </div>
    """, unsafe_allow_html=True)

    for i, (sc, phone) in enumerate(ranked):
        diff = phone["price"] - price
        if diff > 500:
            diff_html = f'<span class="diff-pos">+{fmt_inr(diff)}</span>'
        elif diff < -500:
            diff_html = f'<span class="diff-neg">-{fmt_inr(abs(diff))}</span>'
        else:
            diff_html = f'<span class="diff-zero">Best match</span>'

        best = '<span class="best-chip">BEST MATCH</span>' if i == 0 else ""
        card_cls = "model-card model-card-best" if i == 0 else "model-card"
        avatar = BRAND_EMOJI.get(phone["brand"], phone["brand"][0])
        five_g_pill = '<span class="spec-pill">📶 5G</span>' if phone["five_g"] else ""
        search_q = phone["model"].replace(" ", "+")

        st.markdown(f"""
        <div class="{card_cls}">
          <div class="model-top">
            <div class="model-avatar">{avatar}</div>
            <div style="flex:1;min-width:0;">
              <div class="model-brand-name">{phone["brand"]}{best}</div>
              <div class="model-name">{phone["model"]}</div>
              <div class="model-rating-row">
                <span style="color:#F59E0B;font-size:11px;">{"★"*int(phone["rating"])}{"☆"*(5-int(phone["rating"]))}</span>
                <span class="rating-num">&nbsp;{phone["rating"]}</span>
              </div>
            </div>
          </div>
          <div class="model-price-row">
            <span class="model-price">{fmt_inr(phone["price"])}</span>
            {diff_html}
          </div>
          <div class="spec-row">
            <span class="spec-pill">⚙ {phone["ram"]} RAM</span>
            <span class="spec-pill">💾 {phone["storage"]}</span>
            <span class="spec-pill">📸 {phone["camera"]}</span>
            <span class="spec-pill">🔋 {phone["battery"]}</span>
            {five_g_pill}
          </div>
          <div class="buy-row">
            <span class="buy-label">Buy from</span>
            <a href="https://www.amazon.in/s?k={search_q}" target="_blank" class="buy-amazon">🛒 Amazon</a>
            <a href="https://www.flipkart.com/search?q={search_q}" target="_blank" class="buy-flipkart">🛍 Flipkart</a>
          </div>
        </div>
        """, unsafe_allow_html=True)

st.markdown('<div class="footer">Phone Price Predictor · Prices are estimates based on current market data</div>', unsafe_allow_html=True)
