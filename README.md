
# Projet Carte Interactive des Départements - Collection 'Le Gaulois'

Ce projet permet de visualiser, gérer et suivre la collection des départements français dans le cadre de la collection "Le Gaulois". Il utilise Streamlit pour une interface utilisateur interactive et folium pour la génération de cartes.

## Fonctionnalités

- Affichage des départements possédés et manquants sur une carte interactive.
- Gestion des départements possédés : ajout et suppression.
- Gestion des doublons : ajout et suppression.
- Visualisation distincte des doublons sur une carte.

## Structure du Projet

- `src/carte_le_gaulois.py` : Script principal contenant l'application Streamlit permettant l'affichage.
- `tests/` : Contient les tests unitaires pour les fonctions du projet.
- `departements.geojson` : Fichier GeoJSON des départements utilisé pour générer les cartes.

## Couverture du Code

Les tests couvrent 69 % du code. Cependant, les interactions utilisateur via les boutons Streamlit (comme "Ajouter", "Enlever", etc.) déclenchent des fonctions couvertes dans les tests. Cela explique pourquoi la couverture globale semble inférieure, bien que toutes les logiques critiques soient testées.

## Prérequis

- Python 3.9.20
- Streamlit 1.40.1
- Folium
- GeoPandas

## Installation

1. Clonez ce dépôt.
2. Ouvrir le terminal dans le dossier py_carte_le_gaulois
2. Installez les dépendances nécessaires :
   ```bash
   pip install -r requirements.txt #Si vous utilisez pip
      # OU
   conda install --file requirements.txt #Si vous utilisez conda
   ```
3. Lancez l'application Streamlit :
   ```bash
   streamlit run carte_le_gaulois.py
      #OU
   conda run streamlit run .\src\carte_le_gaulois\carte_le_gaulois.py
   ```
4. Suivre l'explication ci-dessous pour utiliser la carte intéractive

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

## Tests

Les tests unitaires utilisent `pytest`. Pour exécuter les tests :
```bash
conda run pytest --cov tests/
```

Pour vérifier la couverture :
```bash
conda run coverage run .\src\carte_le_gaulois\carte_le_gaulois.py
conda run coverage report
```

## Remarques

- Les boutons Streamlit déclenchent des fonctions directement testées, ce qui garantit leur bon fonctionnement même si leur interaction directe n'est pas comptabilisée dans la couverture du code.
- Si vous avez des idées d'amélioration ou des suggestions, n'hésitez pas à contribuer !

## Auteur

Simon Guillois - simon.guillois@estaca.eu
Thomas Gaboreau - thomas.gaboreau@estaca.eu
