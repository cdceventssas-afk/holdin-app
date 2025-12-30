import streamlit as st
import google.generativeai as genai

# Configuration de la page
st.set_page_config(page_title="HoldIn & Full-Auto AI", layout="wide")

# Barre latérale pour la configuration
st.sidebar.title("⚙️ Configuration")
api_key = st.sidebar.text_input("Entre ta clé API Google :", type="password")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')

    # Menu principal
    st.sidebar.divider()
    mode = st.sidebar.radio("Choisis ta Face :", ["🚀 HoldIn-AI (Création)", "📊 Full-Auto (Gestion)"])
    type_soc = st.sidebar.selectbox("Type de société :", ["SASU", "Holding", "EURL"])

    if mode == "🚀 HoldIn-AI (Création)":
        st.title("🚀 HoldIn-AI : Crée ta société sans erreurs")
        st.subheader(f"Module de création pour {type_soc}")
       
        tab1, tab2 = st.tabs(["Générateur de Statuts", "Audit de Refus"])
       
        with tab1:
            activite = st.text_input("Quelle est ton activité ?")
            if st.button("Générer la clause d'Objet Social"):
                prompt = f"Rédige une clause d'objet social juridique complète et large pour une {type_soc} dans le domaine de : {activite}. Utilise un langage pro conforme au greffe français."
                response = model.generate_content(prompt)
                st.write(response.text)
               
        with tab2:
            motif = st.text_area("Copie ici le motif de refus du greffe ou de la banque :")
            if st.button("Analyser le refus"):
                prompt = f"En tant qu'expert juridique, explique simplement pourquoi ce refus a eu lieu et donne la correction exacte à apporter aux statuts de cette {type_soc} : {motif}"
                response = model.generate_content(prompt)
                st.info(response.text)

    else:
        st.title("📊 Full-Auto Holding : Le Pilote Automatique")
        st.subheader(f"Gestion quotidienne de ta {type_soc}")
       
        action = st.selectbox("Que veux-tu faire ?", [
            "Analyser un bilan/relevé (Texte)",
            "Rédiger un Procès-Verbal (PV)",
            "Arbitrage Dividendes/Salaire"
        ])
       
        if action == "Analyser un bilan/relevé (Texte)":
            data = st.text_area("Colle ici les données ou le texte de ton document :")
            if st.button("Extraire les points clés"):
                prompt = f"Analyse ces données financières de ma {type_soc}. Donne-moi : 1. Résumé en 3 points, 2. Alertes rouges, 3. Action à faire. Texte : {data}"
                response = model.generate_content(prompt)
                st.success(response.text)
               
        elif action == "Rédiger un Procès-Verbal (PV)":
            objet_pv = st.text_input("Objet du PV (ex: Achat d'un bateau, Changement d'adresse) :")
            if st.button("Générer le PV"):
                prompt = f"Rédige un modèle de Décision de l'Associé Unique pour une {type_soc} concernant l'objet suivant : {objet_pv}. Respecte le formalisme juridique français."
                response = model.generate_content(prompt)
                st.code(response.text, language="markdown")

else:
    st.warning("Veuillez entrer votre clé API Google dans la barre latérale pour lancer la machine.")
    st.info("Ton outil est prêt. Il n'attend que son cerveau (la clé API).")
