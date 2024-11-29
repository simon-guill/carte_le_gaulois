Tests
=====


**Dossier des tests :**
- **`tests/test_carte.py`** : Tests pour les fonctionnalités principales.

Pour exécuter les tests unitaires, utilisez la commande suivante :
``conda run pytest --cov tests/``

- Black

Le fichier carte_le_gaulois.py a été reformaté en utilisant black
``conda run black .\src\carte_le_gaulois\carte_le_gaulois.py``

- Coverage

Pour vérifier la couverture :
``conda run coverage run .\src\carte_le_gaulois\carte_le_gaulois.py``
puis
``conda run coverage report``

- Les tests couvrent 69 % du code. Cependant, les interactions utilisateur via les boutons Streamlit (comme "Ajouter", "Enlever", etc.) déclenchent des fonctions couvertes dans les tests. Cela explique pourquoi la couverture globale semble inférieure, bien que toutes les logiques critiques soient testées.
- En ouvrant le rapport en html (```conda run coverage html```), nous nous rendons compte que les fonctions non couvertes sont les boutons. 

- Pylint check

Pour analyser le code :
``conda run pylint .\src\carte_le_gaulois\carte_le_gaulois.py``
