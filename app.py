import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="HoldIn & Full-Auto AI", layout="wide")

st.sidebar.title("⚙️ Configuration")
api_key = st.sidebar.text_input("Entre ta clé API Google :", type="password")

if api_key:
    try:
        genai.configure(api_key=api_key)
        # On utilise le modèle 1.5-flash qui est le plus robuste
        model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")

        st.sidebar.divider()
        mode = st.sidebar.radio("Choisis ta Face :", ["🚀 HoldIn-AI (Création)", "📊 Full-Auto (Gestion)"])
        type_soc = st.sidebar.selectbox("Type de société :", ["SASU", "Holding", "EURL"])

        if mode == "🚀 HoldIn-AI (Création)":
            st.title("🚀 HoldIn-AI : Crée ta société")
            activite = st.text_input("Quelle est ton activité ?")
            if st.button("Générer l'Objet Social"):
                prompt = f"Rédige une clause d'objet social juridique pour une {type_soc} dans le domaine de : {activite}."
                response = model.generate_content(prompt)
                st.write(response.text)
        else:
            st.title("📊 Full-Auto : Gestion")
            objet_pv = st.text_input("Objet du PV (ex: Achat d'un bateau) :")
            if st.button("Générer le document"):
                prompt = f"Rédige un modèle de PV pour une {type_soc} concernant : {objet_pv}."
                response = model.generate_content(prompt)
                st.code(response.text)

    except Exception as e:
        st.error(f"Oups ! L'IA ne répond pas. Détail : {e}")
else:
    st.info("Entre ta clé API à gauche pour activer l'outil.")
