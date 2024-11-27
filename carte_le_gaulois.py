import streamlit as st
import geopandas as gpd
import folium
from streamlit_folium import st_folium
import json

# Chargement du fichier GeoJSON des départements
geojson_path = r"C:\Users\Owner\carte_le_gaulois\carte_le_gaulois\departements.geojson"
departements = gpd.read_file(geojson_path)

# Initialisation des listes dans la session Streamlit si elles n'existent pas encore
if "departements_possedes" not in st.session_state:
    st.session_state["departements_possedes"] = [
        "01",
        "03",
        "06",
        "07",
        "08",
        "10",
        "13",
        "15",
        "18",
        "21",
        "23",
        "25",
        "26",
        "29",
        "30",
        "31",
        "34",
        "37",
        "38",
        "41",
        "42",
        "43",
        "44",
        "45",
        "46",
        "49",
        "50",
        "52",
        "54",
        "57",
        "59",
        "60",
        "62",
        "63",
        "66",
        "68",
        "69",
        "71",
        "72",
        "73",
        "75",
        "76",
        "77",
        "78",
        "80",
        "81",
        "83",
        "84",
        "87",
        "89",
    ]  # Liste initiale
if "departements_doublons" not in st.session_state:
    st.session_state["departements_doublons"] = departements_doublons = {
        "01": 2,
        "13": 3,
        "29": 2,
        "44": 2,
        "49": 3,
        "59": 2,
        "63": 2,
        "69": 2,
        "75": 3,
        "77": 2,
        "78": 2,
        "83": 1,
        "84": 2,
        "89": 2,
        "50": 2,
        "34": 2,
        "42": 2,
        "76": 3,
        "21": 2,
        "10": 2,
    }

# Récupération des listes depuis la session
departements_possedes = st.session_state["departements_possedes"]
departements_doublons = st.session_state["departements_doublons"]
departements_manquants = [
    code for code in departements["code"] if code not in departements_possedes
]

# Titre de l'application
st.title("Carte Interactive des Départements - Collection 'Le Gaulois'")

# Sélection pour ajouter/enlever des départements et gérer les doublons
add_departement = st.selectbox("Ajouter un département", departements_manquants)
remove_departement = st.selectbox("Enlever un département", departements_possedes)
add_doublon = st.selectbox("Ajouter un doublon", departements_possedes)
remove_doublon = st.selectbox("Enlever un doublon", list(departements_doublons.keys()))

# Boutons pour ajouter/enlever des départements et gérer les doublons
if st.button("Ajouter"):
    if add_departement not in departements_possedes:
        departements_possedes.append(add_departement)
        departements_manquants.remove(add_departement)
        # Mise à jour dans la session
        st.session_state["departements_possedes"] = departements_possedes

if st.button("Enlever"):
    if remove_departement in departements_possedes:
        departements_possedes.remove(remove_departement)
        departements_manquants.append(remove_departement)
        # Mise à jour dans la session
        st.session_state["departements_possedes"] = departements_possedes

if st.button("Ajouter un doublon"):
    if add_doublon in departements_possedes:
        if add_doublon in departements_doublons:
            departements_doublons[add_doublon] += 1
        else:
            departements_doublons[add_doublon] = 1
        # Mise à jour dans la session
        st.session_state["departements_doublons"] = departements_doublons

if st.button("Enlever un doublon"):
    if remove_doublon in departements_doublons:
        if departements_doublons[remove_doublon] > 1:
            departements_doublons[remove_doublon] -= 1
        else:
            del departements_doublons[remove_doublon]
        # Mise à jour dans la session
        st.session_state["departements_doublons"] = departements_doublons

# Mise à jour du statut des départements dans le GeoDataFrame
departements["status"] = departements["code"].apply(
    lambda x: "Possédé" if x in departements_possedes else "Manquant"
)

# Création de la première carte
st.header(
    "Carte des Départements Possédés et Manquants"
)  # Ajout d'un titre pour la première carte
m1 = folium.Map(location=[46.603354, 1.888334], zoom_start=5)


# Fonction pour styliser les départements pour la première carte
def style_function(feature):
    if feature["properties"]["status"] == "Possédé":
        return {
            "fillColor": "#228B22",  # Vert pour les départements possédés
            "color": "black",
            "weight": 1,
            "fillOpacity": 0.6,
        }
    else:
        return {
            "fillColor": "#FF6347",  # Rouge pour les départements manquants
            "color": "black",
            "weight": 1,
            "fillOpacity": 0.6,
        }


# Ajout des départements à la première carte avec les styles
folium.GeoJson(
    data=json.loads(departements.to_json()),
    style_function=style_function,
    tooltip=folium.GeoJsonTooltip(
        fields=["nom", "status"], aliases=["Département: ", "Statut: "]
    ),
).add_to(m1)

# Affichage de la première carte avec Streamlit
st_folium(m1, width=700, height=500)

# Création de la deuxième carte pour les doublons
st.header(
    "Carte des Départements en Doublons"
)  # Ajout d'un titre pour la deuxième carte
m2 = folium.Map(location=[46.603354, 1.888334], zoom_start=5)

# Mise à jour du statut des départements pour les doublons
departements["doublon"] = departements["code"].apply(
    lambda x: (
        f"Doublon ({departements_doublons[x]})"
        if x in departements_doublons
        else "Aucun"
    )
)


# Fonction pour styliser les départements pour la deuxième carte
def style_function_doublon(feature):
    if feature["properties"]["doublon"].startswith("Doublon"):
        return {
            "fillColor": "#FFD700",  # Jaune pour les départements en doublons
            "color": "black",
            "weight": 1,
            "fillOpacity": 0.6,
        }
    else:
        return {
            "fillColor": "#D3D3D3",  # Gris pour les départements sans doublons
            "color": "black",
            "weight": 1,
            "fillOpacity": 0.4,
        }


# Ajout des départements à la deuxième carte avec les styles pour les doublons
folium.GeoJson(
    data=json.loads(departements.to_json()),
    style_function=style_function_doublon,
    tooltip=folium.GeoJsonTooltip(
        fields=["nom", "doublon"], aliases=["Département: ", "Doublons: "]
    ),
).add_to(m2)

# Affichage de la deuxième carte avec Streamlit
st_folium(m2, width=700, height=500)