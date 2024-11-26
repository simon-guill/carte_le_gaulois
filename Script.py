import streamlit as st
import folium
from streamlit_folium import st_folium
import geopandas as gpd

# Chargement des départements
geojson_path = 'path_to_file/departements.geojson'  # Remplace ce chemin par le bon
departements = gpd.read_file(geojson_path)

# Initialiser st.session_state si ce n'est pas déjà fait
if 'added_departments' not in st.session_state:
    st.session_state.added_departments = []

# Fonction pour ajouter un département à la liste des départements ajoutés
def add_department(department_code):
    if department_code not in st.session_state.added_departments:
        st.session_state.added_departments.append(department_code)

# Fonction pour supprimer un département de la liste des départements ajoutés
def remove_department(department_code):
    if department_code in st.session_state.added_departments:
        st.session_state.added_departments.remove(department_code)

# Interface Streamlit
st.title("Carte Interactive des Départements")

# Choisir un département par son code
department_code = st.selectbox("Choisir un département à ajouter", departements['code'])  # Utilise 'code' à la place de 'ID'

# Ajouter ou supprimer le département à la session si sélectionné
if st.button("Ajouter le département"):
    add_department(department_code)

if st.button("Supprimer le département"):
    remove_department(department_code)

# Créer la carte de base
m = folium.Map(location=[48.8566, 2.3522], zoom_start=6)  # Centré sur la France

# Ajouter les départements déjà ajoutés sur la carte avec couleurs et bordures
for dept_code in st.session_state.added_departments:
    dept = departements[departements['code'] == dept_code]  # Utilise 'code' à la place de 'ID'
    
    # Définir la couleur et le style de la géoformée
    folium.GeoJson(
        dept,
        style_function=lambda x: {
            'fillColor': 'green',  # Couleur de remplissage
            'color': 'red',        # Couleur de la bordure
            'weight': 2,           # Poids de la bordure
            'fillOpacity': 0.5     # Opacité du remplissage
        }
    ).add_to(m)

# Afficher la carte interactive
st_folium(m, width=700, height=500)

# Affichage de la liste des départements ajoutés
st.write("Départements ajoutés :")
st.write(st.session_state.added_departments)
