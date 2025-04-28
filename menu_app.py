
import streamlit as st
import qrcode
from io import BytesIO
from PIL import Image

st.set_page_config(page_title="African Aroma Cafe Menu", page_icon="☕", layout="wide")

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

# --- Sidebar Content ---
with st.sidebar:
    st.image("logo.png", width=350) 
    st.title("African Aroma Cafe")
    st.divider()

    st.subheader("📱 Scan Menu")
    menu_url = "https://coffee-shop-menu-jvbwey72ay4snxkgs9x9k3.streamlit.app/" 

    qr = qrcode.make(menu_url)
    buf = BytesIO()
    qr.save(buf)
    st.image(Image.open(buf), width=150)

    st.divider()
    st.subheader("🧾 Your Cart")
    total_placeholder = st.empty()  # Dynamic total
    submit_button = st.button("✅ Submit Order", use_container_width=True)

# --- Main Content ---
st.title("☕ African Aroma Cafe ")
st.caption("Select your favorite beverages and bites!")

selected_items = []
total = 0

for section, items in menu.items():
    st.header(section)
    for item, price in items.items():
        selected = st.checkbox(f"{item} - {price:,} TZS")
        if selected:
            selected_items.append((item, price))
            total += price

# Update total dynamically
total_placeholder.markdown(f"### **Total: {total:,} TZS**")

# After Submit
if submit_button:
    if selected_items:
        st.success("✅ Order submitted successfully!")
        st.write("**📝 Order Summary:**")
        for item, price in selected_items:
            st.write(f"- {item}: {price:,} TZS")
    else:
        st.warning("⚠️ No items selected yet!")


