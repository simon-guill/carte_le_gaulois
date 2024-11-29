
# Projet Carte Interactive des Départements - Collection 'Le Gaulois'

Ce projet permet de visualiser, gérer et suivre la collection des départements français dans le cadre de la collection "Le Gaulois". Il utilise Streamlit pour une interface utilisateur interactive et folium pour la génération de cartes.

## Fonctionnalités

- Affichage des départements possédés et manquants sur une carte interactive.
- Gestion des départements possédés : ajout et suppression.
- Gestion des doublons : ajout et suppression.
- Visualisation distincte des doublons sur une carte.

## Structure du Projet

- `src/carte_le_gaulois/carte_le_gaulois.py` : Le fichier principal contenant l'application Streamlit. Il gère l'interface utilisateur, l'affichage interactif des cartes, ainsi que la logique de gestion des départements et des doublons.
- `src/departements.geojson` : Fichier GeoJSON contenant les données géographiques des départements français. Il est utilisé pour générer les cartes interactives et afficher les départements en fonction de leur statut (possédé, manquant, doublon).
- `tests/` : Dossier contenant les tests unitaires pour vérifier le bon fonctionnement du code. Ces tests couvrent les fonctions critiques du projet, comme l'ajout, la suppression des départements et la gestion des doublons.
- `requirements.txt` : Fichier listant toutes les dépendances nécessaires pour faire fonctionner le projet. Il inclut les bibliothèques comme Streamlit, GeoPandas, Folium, etc.

## Prérequis

python==3.9.20
pillow==9.5.0
streamlit==1.40.1
geopandas==0.14.0
folium==0.14.0
streamlit-folium==0.11.0
pytest==7.4.0
pytest-cov==4.1.0
black==23.9.1
coverage==7.3.1
ruff==0.8.0
pylint==3.3.1

## Documentation

Vous avez accès à une documentation .HTML en ouvrant le document index.html présent dans 
``\carte_le_gaulois\doc\build\html``

## Installation

1. Clonez ce dépôt.

2. Ouvrir le terminal dans le dossier C:\Users\<nom>\Desktop\carte_le_gaulois

3. Installez les dépendances nécessaires :
   ``conda install --file requirements.txt #Si vous utilisez conda``

4. Dans le fichier ``src\carte_le_gaulois\carte_le_gaulois.py`` à la ligne 14, mettre le chemin d'accès au fichier departements.geojson
   Exemple : ``C:\Users\<nom>\Desktop\carte_le_gaulois\src\carte_le_gaulois\departements.geojson``

5. Réalisez les tests :

6. Lancez l'application Streamlit :
   ``conda run streamlit run .\src\carte_le_gaulois\carte_le_gaulois.py``

7. Suivre l'explication ci-dessous pour utiliser la carte intéractive

## Utilisation de la carte 

   1. Ajouter un département :

      Utilisez le menu déroulant pour sélectionner un département manquant.
      Cliquez sur le bouton "Ajouter". Le département sélectionné sera alors ajouté à la carte et apparaîtra en vert (indiquant qu'il est maintenant possédé).

   2. Enlever un département :

      Sélectionnez un département déjà possédé dans le menu déroulant.
      Cliquez sur "Enlever" pour retirer le département de la carte. Il réapparaîtra en rouge, signalant qu'il est maintenant manquant.

   3. Gérer les doublons :

      Vous pouvez ajouter ou supprimer des doublons pour un département.
      Lorsqu'un département est marqué comme doublon, il apparaîtra en jaune sur la carte, avec l'indication du nombre de doublons pour ce département.
      Sélectionnez un département dans le menu pour ajouter ou retirer un doublon.

   4. Interactivité de la carte :
      Info-bulles : En survolant un département, une info-bulle affiche des informations détaillées :
      Le nom du département
      Son statut (Possédé ou Manquant)


## Black

Le fichier carte_le_gaulois.py a été reformaté en utilisant black
``conda run black .\src\carte_le_gaulois\carte_le_gaulois.py``

## Coverage

Pour vérifier la couverture :
``conda run coverage run .\src\carte_le_gaulois\carte_le_gaulois.py``
puis
``conda run coverage report``

- Les tests couvrent 69 % du code. Cependant, les interactions utilisateur via les boutons Streamlit (comme "Ajouter", "Enlever", etc.) déclenchent des fonctions couvertes dans les tests. Cela explique pourquoi la couverture globale semble inférieure, bien que toutes les logiques critiques soient testées.
- En ouvrant le rapport en html (```conda run coverage html```), nous nous rendons compte que les fonctions non couvertes sont les boutons. 

## Tests

Les tests unitaires utilisent `pytest`. Pour exécuter les tests :
``conda run pytest --cov tests/``

## Pylint check

Pour analyser le code :
``conda run pylint .\carte_le_gaulois.py``

## Remarques

- Les boutons Streamlit déclenchent des fonctions directement testées, ce qui garantit leur bon fonctionnement même si leur interaction directe n'est pas comptabilisée dans la couverture du code.
- Si vous avez des idées d'amélioration ou des suggestions, n'hésitez pas à contribuer !


## Auteur

Simon Guillois - simon.guillois@estaca.eu
Thomas Gaboreau - thomas.gaboreau@estaca.eu
