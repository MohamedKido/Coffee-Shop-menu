import streamlit as st # type: ignore
import qrcode # type: ignore
from io import BytesIO
from PIL import Image

st.set_page_config(page_title="African Aroma Cafe Menu", page_icon="☕", layout="centered")

# --- Menu Data ---
menu = {
    "Beverages - Hot": {
        "Karak Tea": 1500,
        "Espresso": 3000,
        "Double Espresso": 4000,
        "Cappuccino": 5000,
        "Cafe Latte": 5000,
    },
    "Beverages - Cold": {
        "Dafu": 4000,
        "Sharbat": 3000,
        "Ndimu": 2000,
        "Tanga Juice": 2000,
        "Iced Latte": 7000,
        "Water": 500,
    },
    "Bites / Snacks": {
        "Slice Cream Cake": 3500,
        "Mini Cheese Buns": 4000,
        "Nutella Swiss Rolls": 1200,
        "Jam Swiss Rolls": 1000,
        "Parfait Cake": 6000,
        "Caramel Pudding": 3000,
        "Oreo Cheesecake": 4000,
        "Biscoff Cheesecake": 5000,
        "Kunafa Pistachio Nutella Mix": 2000,
        "Chocolate": 3000,
        "Sweet Samosa (5pcs)": 5000,
        "Chocolate Hazelnut Croissant": 1500,
        "Mini Croissant": 3000,
        "Mini Cinnamon Swirl": 3000,
        "Mini Chocolate Twist": 3000,
        "Mini Custard Extravagant": 3000,
    },
    "Savory Bites": {
        "Beef Samosa": 1000,
        "Spring Rolls": 1000,
        "Kachori": 300,
    },
}

# --- Header Content ---
st.image("logo.png", width=500)  # Larger logo width at the top
st.title("African Aroma Cafe")
st.caption("Select your favorite beverages and bites!")

# --- QR Code Generation ---
col1, col2, col3 = st.columns([1, 3, 1])  # Create columns for layout

with col3:
    menu_url = "https://coffee-shop-menu-jvbwey72ay4snxkgs9x9k3.streamlit.app/"
    qr = qrcode.make(menu_url)
    buf = BytesIO()
    qr.save(buf)
    st.image(Image.open(buf), width=100)  # Place QR code here

# --- Main Content ---
selected_items = []
total = 0

# Using columns for a more centered layout
col1, col2, col3 = st.columns([1, 3, 1])

with col2:
    for section, items in menu.items():
        st.header(section)
        for item, price in items.items():
            selected = st.checkbox(f"{item} - {price:,} TZS")
            if selected:
                selected_items.append((item, price))
                total += price

# --- Footer (Total and Submit Order) ---
st.divider()  # Optional divider before footer

col1, col2, col3 = st.columns([1, 3, 1])  # New column setup for footer

with col2:
    # Centered total with the button aligned to the right
    st.markdown(f"### **Total: {total:,} TZS**", unsafe_allow_html=True)
    
    # Align the button to the right of the total
    col1, col2, col3 = st.columns([1, 4, 1])
    with col2:
        submit_button = st.button("✅ Submit Order", use_container_width=False)

# After Submit
if submit_button:
    if selected_items:
        st.success("✅ Order submitted successfully!")
        st.write("**📝 Order Summary:**")
        for item, price in selected_items:
            st.write(f"- {item}: {price:,} TZS")
    else:
        st.warning("⚠️ No items selected yet!")

# --- Custom CSS for Styling ---
st.markdown("""
    <style>
        /* Remove button background color */
        .stButton button {
            color: #4CAF50;
            font-size: 1.2rem;
            border-radius: 10px;
            padding: 10px 20px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
            border: 2px solid #4CAF50;
        }
        .stButton button:hover {
            background-color: #45a049;
            color: white;
        }
        .stCheckbox > div {
            font-size: 1rem;
        }
    </style>
""", unsafe_allow_html=True)
