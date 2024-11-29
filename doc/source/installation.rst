Installation
============

Pour installer le projet, suivez les étapes ci-dessous :

1. Clonez ce dépôt.
2. Ouvrir le terminal dans le dossier où vous avez cloné le dépôt Git. Par exemple : ``C:\Users\<nom>\Desktop\carte_le_gaulois``
3. Installez les dépendances nécessaires :
   ``conda install --file requirements.txt #Si vous utilisez conda``
4. Dans le fichier src/carte_le_gaulois/carte_le_gaulois.py à la ligne 14, mettre le chemin d'accès au fichier departements.geojson
   Exemple : ``C:\Users\<nom>\Desktop\carte_le_gaulois\src\carte_le_gaulois\departements.geojson``
5. Réalisez les tests
   Suivre la section **Tests** de la documentation

6. Lancez l'application Streamlit :
   ``conda run streamlit run .\src\carte_le_gaulois\carte_le_gaulois.py``
7. Suivre la section utilisation pour interagir avec la carte