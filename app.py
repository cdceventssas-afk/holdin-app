import streamlit as st
import google.generativeai as genai

# Configuration de la page
st.set_page_config(page_title="HoldIn & Full-Auto AI", layout="wide")

st.sidebar.title("⚙️ Configuration")
api_key = st.sidebar.text_input("Entre ta clé API Google :", type="password")

if api_key:
    try:
        # Initialisation de l'API
        genai.configure(api_key=api_key)
       
        # Tentative d'utiliser le modèle le plus stable
        # Note : On l'assigne à la variable 'model'
        model = genai.GenerativeModel('gemini-1.5-flash')

        st.sidebar.success("Clé API connectée !")
        st.sidebar.divider()
       
        mode = st.sidebar.radio("Choisis ta Face :", ["🚀 HoldIn-AI (Création)", "📊 Full-Auto (Gestion)"])
        type_soc = st.sidebar.selectbox("Type de société :", ["SASU", "Holding", "EURL"])

        if mode == "🚀 HoldIn-AI (Création)":
            st.title("🚀 HoldIn-AI : Création de société")
            st.subheader(f"Module pour {type_soc}")
           
            activite = st.text_input("Quelle est ton activité ? (ex: Conseil IT, Commerce vin)")
            if st.button("Générer l'Objet Social"):
                with st.spinner('Rédaction juridique en cours...'):
                    prompt = f"Rédige une clause d'objet social juridique complète pour une {type_soc} dans le domaine de : {activite}."
                    response = model.generate_content(prompt)
                    st.info(response.text)
       
        else:
            st.title("📊 Full-Auto : Gestion de Holding")
            objet_pv = st.text_input("Objet du document (ex: Transfert de siège, Achat matériel) :")
            if st.button("Générer le Procès-Verbal"):
                with st.spinner('Génération du PV...'):
                    prompt = f"Rédige un modèle de décision de l'associé unique de {type_soc} pour : {objet_pv}."
                    response = model.generate_content(prompt)
                    st.code(response.text)

    except Exception as e:
        st.error(f"Oups ! L'IA ne répond pas. Détail : {e}")
