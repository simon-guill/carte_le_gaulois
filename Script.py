import geopandas as gpd
import folium
import matplotlib.pyplot as plt

# Spécifie le chemin vers ton fichier GeoJSON
geojson_path = r"C:\Users\Owner\carte_le_gaulois\carte_le_gaulois\departements.geojson"

# Charge le fichier GeoJSON des départements
departements = gpd.read_file(geojson_path)

# Imaginons que tu aies une liste des départements possédés et manquants
# Exemple :
departements_possedes = ["01", "13", "33", "75"]  # Numéros des départements possédés
departements_manquants = ["02", "14", "34", "95"]  # Numéros des départements manquants

# Ajoute une colonne pour indiquer si un département est possédé ou non
departements['status'] = departements['code'].apply(
    lambda x: 'Possédé' if x in departements_possedes else 'Manquant'
)

# Crée une carte centrée sur la France
m = folium.Map(location=[46.603354, 1.888334], zoom_start=5)

# Fonction pour styliser les départements en fonction de leur statut (possédé ou manquant)
def style_function(feature):
    if feature['properties']['status'] == 'Possédé':
        return {
            'fillColor': '#228B22',  # Vert pour les départements possédés
            'color': 'black',
            'weight': 1,
            'fillOpacity': 0.6,
        }
    else:
        return {
            'fillColor': '#FF6347',  # Rouge pour les départements manquants
            'color': 'black',
            'weight': 1,
            'fillOpacity': 0.6,
        }

# Fonction pour changer le style lors du survol
def highlight_function(feature):
    return {
        'fillColor': '#ffaf00',  # Couleur changeante lors du survol
        'color': 'black',
        'weight': 2,
        'fillOpacity': 0.9,
    }

# Ajoute les départements à la carte avec les interactions
folium.GeoJson(
    departements,
    style_function=style_function,
    highlight_function=highlight_function,
    tooltip=folium.GeoJsonTooltip(fields=["nom", "status"], aliases=["Département: ", "Statut: "]),  # Info-bulle
).add_to(m)

# Enregistre la carte dans un fichier HTML
m.save('carte_interactive.html')

# Plot de la carte statique avec matplotlib pour visualiser
fig, ax = plt.subplots(figsize=(10, 10))
departements.plot(column='status', ax=ax, legend=True,
                  legend_kwds={'title': "Statut de la collection"},
                  cmap='RdYlGn',  # Colormap pour visualiser en couleurs les possédés/manquants
                  edgecolor='black')
plt.title("Carte des départements collectionnés")
plt.show()