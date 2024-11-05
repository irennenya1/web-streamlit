from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie
import subprocess
from streamlit_option_menu import option_menu
from flask import Flask, render_template

st.set_page_config(
    page_title="Bruule.it",
    page_icon="🫶🏻", 
    layout="wide"                                                                      
)
st.title("Home")
st.sidebar.success("Made by kelompok . ")
#----manual selected----
if st.session_state.get('switch_button', False):
    st.session_state['menu_option'] = (st.session_state.get('menu_option', 0) + 1) % 4
    manual_select = st.session_state['menu_option']
else:
    manual_select = None

selected4 = option_menu(None, ["Home", "Menu", "Kontak", 'Settings'], 
    icons=['house', 'cloud-upload', "list-task", 'gear'], 
    orientation="horizontal", manual_select=manual_select, key='menu_4')
st.button(f"Next {st.session_state.get('menu_option', 1)}", key='switch_button')

result = subprocess.run(['node', 'path/indeks.js'], capture_output=True, text=True)
print(result.stdout) 

# Fungsi untuk memuat animasi Lottie dari URL
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Menggunakan CSS lokal untuk gaya khusus
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

#---- Memuat aset ----
lottie_coding = load_lottieurl("https://lottie.host/355fa541-b609-43dc-ac4e-31fc080c2104/86nEFIiyws.json")
Image_contact_form = Image.open("images/1.png")
Image_lottie_animation = Image.open("images/2.png")
Image_3 = Image.open("images/3.png")
Image_4 = Image.open("images/4.png")
Image_5 = Image.open("images/5.png")
Image_6 = Image.open("images/6.png")
Image_7 = Image.open("images/7.png")
Image_8 = Image.open("images/8.png")
Image_9 = Image.open("images/9.png")
Image_10 = Image.open("images/10.png")

# CSS khusus untuk tombol dan animasi hover
st.markdown("""
    <style>
        .stButton button {
            background-color: #007bff;
            color: white;
            border-radius: 10px;
            font-size: 16px;
            padding: 10px 20px;
            transition: all 0.3s ease;
        }
        .stButton button:hover {
            background-color: #0056b3;
            transform: scale(1.05);
        }
        .centered-header {
            font-size: 60px;
            text-align: center;
            font-weight: bold;
            color: #007bff;
            margin-top: 20px;
        }
        .product-card {
            border: 1px solid #e0e0e0;
            border-radius: 15px;
            padding: 20px;
            box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s;
        }
        .product-card:hover {
            transform: translateY(-15px);
        }
        .product-header {
            font-size: 24px;
            font-weight: bold;
            color: #f5f5f5;
        }
        .product-description {
            color: white;  /* Mengubah warna font deskripsi produk menjadi putih */
        }
        body {
            background-color: #f5f5f5;
        }
    </style>
""", unsafe_allow_html=True)

#---- Bagian Header Tengah ----
with st.container():
    st.markdown("<h1 class='centered-header'>Bruule.it</h1>", unsafe_allow_html=True)
    st.subheader("Brulee.it – Sensasi Rasa Italia dalam Setiap Gigitan! 🍝🧀")
    st.write(""" Nikmati kelezatan hidangan khas Brulee.it yang memadukan cita rasa Italia dan sentuhan keju
              yang meleleh sempurna! Mulai dari dimsum lembut, spaghetti klasik, hingga macaroni lumer dengan
              balutan keju premium, setiap menu di Brulee.it dibuat khusus untuk memanjakan lidah Anda.
              Terinspirasi dari hidangan otentik Italia, kami hadir dengan bahan berkualitas dan resep yang telah dicintai
              pelanggan sejak pertama kali membuka pintu pada 2020.
Dengan layanan melalui Shopee Food, Grab Food, WhatsApp, Instagram, dan situs web resmi kami, memesan favorit Anda dari Brulee.it kini lebih mudah. Bergabunglah dengan pelanggan setia kami dan temukan sendiri kenapa Brulee.it jadi pilihan utama! ❤""")
    st.write("""
        Brulee.it telah beroperasi selama 5 tahun. Dimulai setelah lulus sekolah tanpa pekerjaan dan menunggu lama untuk masuk universitas.
        Awalnya usaha ini berjalan lambat, tetapi berkembang setelah kami mulai berkolaborasi dengan influencer.
        Kini, kami memiliki toko offline dan tersedia di GrabFood serta ShopeeFood.
        """)
    st.subheader("Kami siap melayani pesanan Anda!")
    st.write("WhatsApp, Grabfood, ShopeeFood👇")
    st.write("Link WhatsApp")
    st.write("[Link WhatsApp untuk Pesan 👈](https://wa.link/rx574l)")
    st.write("Link GrabFood")
    st.write("[Link GrabFood untuk presan 🛵](https://food.grab.com/id/id/restaurant/brulee-it-adiarsa-timur-delivery/6-C6TBRUJAUA6YNX?sourceID=20240808_233808_4a3bec2307dce745_MEXMPS)")
    st.write("Link ShopeeFood")
    st.write("[Link ShopeeFood untuk pesan 📳](https://shopee.co.id/universal-link/now-food/shop/21742059?deep_and_deferred=1&shareChannel=copy_link)")

#---- Bagian Apa yang Kami Lakukan ----
with st.container():
    st.write("------")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Tentang Toko Kami")
        st.write("Kami juga memiliki akun Instagram untuk menampilkan beberapa pilihan produk atau etalase")
        st.write("Brulée Pasta")
        st.write("100% HALAL")
        st.write("DIMSUM, SPAGHETTI , MACAARONI")
        st.write("✉️ DM untuk Pesanan (Tersedia untuk acara)")
        st.write("🫶🏻 Homemade & Fresh selalu tersedia")
        st.write("Untuk info lebih lanjut silakan kunjungi link instagram kita di bawah")
        st.write("[Kunjungi Instagram Kami 👇](https://www.instagram.com/brulee.it?igsh=MW1iano3Nm9qcWEzZw==)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")
        st.write("----------")
