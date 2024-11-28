Documentation de l'API
======================

**Fonctions principales** :

- `style_function` : Définit le style des départements sur la carte principale.
- `style_function_doublon` : Définit le style pour les doublons.

**Exemple d'usage** :
```python
def style_function(feature):
    if feature["properties"]["status"] == "Possédé":
        return {"fillColor": "#228B22", "color": "black", "fillOpacity": 0.6}
    return {"fillColor": "#FF6347", "color": "black", "fillOpacity": 0.6}
```
