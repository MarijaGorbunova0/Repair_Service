import streamlit as st
from datetime import datetime

teenused = {
    "Arvutite remont": "Pakume kiiret ja kvaliteetset arvutite remonti, sealhulgas ekraani, klaviatuuri, emaplaadi vahetust ja muid teenuseid.",
    "Laudade remont": "Meil on spetsialiseerumine laua-arvutite remondile, sealhulgas komponentide vahetus, operatsioonisüsteemi paigaldus ja muud teenused.",
    "Tolmu puhastamine": "Pakume professionaalset arvutite ja sülearvutite tolmupuhastust, et parandada jahutusvõimekust ja pikendada seadme eluiga.",
    "Tarkvara paigaldamine": "Me aitame paigaldada vajalikke tarkvarasid, sealhulgas operatsioonisüsteeme, draivereid ja utiliite, et teie seade töötaks paremini."
}

galerii = {
    "Sülearvuti ekraani vahetus": "💻🔧",
    "Arvuti tolmupuhastus": "🧹💻",
    "Emaplaadi remont": "🔧🖥️"
}

st.set_page_config(page_title="Arvutite remont teenused", layout="centered")

if "on_form_opened" not in st.session_state:
    st.session_state.on_form_opened = False

st.title("Arvutite remont teenused")

col1, col2 = st.columns([1, 6])

with col1:
    if st.button("🏠 Naudi teenuseid", key="home_button_top"):
        st.session_state.on_form_opened = False

with col2:
    if st.button("Tellige teenus", key="order_service_button_top", on_click=lambda: st.session_state.update({"on_form_opened": True})):
        st.session_state.on_form_opened = True

if not st.session_state.on_form_opened:
    st.subheader("Meie teenused:")
    
    for teenus, kirjeldus in teenused.items():
        st.write(f"**{teenus}**: {kirjeldus}")
    
    st.subheader("Meie tehtud tööd:")
    for töö, emojid in galerii.items():
        st.write(f"{töö}: {emojid}")

else:
    st.subheader("Arvutite teenuse tellimine")

    with st.form(key='service_form'):
        nimi = st.text_input("Teie nimi:")
        email = st.text_input("Teie e-mail:")
        telefon = st.text_input("Teie telefon (soovituslik):")
        
        teenuse_päring = st.selectbox("Vali teenus", list(teenused.keys()))
        
        sõnum = st.text_area("Kirjelda probleemi või teenuse soovi:")
        
        kuupäev = st.date_input("Valige teenuse kuupäev", min_value=datetime.today())
        aeg = st.time_input("Valige teenuse kellaaeg", value=datetime.now().time())

        submit_button = st.form_submit_button("Saada päring")

        if submit_button:
            if nimi and email and teenuse_päring and sõnum:
                st.success(f"Teie päring teenusele '{teenuse_päring}' on edukalt saadetud!")
                st.write(f"**Teie andmed:**")
                st.write(f"Nimi: {nimi}")
                st.write(f"Email: {email}")
                st.write(f"Telefon: {telefon}")
                st.write(f"Teenuse kirjeldus: {sõnum}")
                st.write(f"Valitud teenuse kuupäev ja kellaaeg: {kuupäev} kell {aeg}")
            else:
                st.error("Palun täida kõik vajalikud väljad.")

    if st.button("🏠", key="home_button_back"):
        st.session_state.on_form_opened = False
