import pytest

# Exemple de fonctions simulées du script principal
# Remarque : les tests seront réalisés en fonction des fonctionnalités spécifiques que tu veux tester
# Ici, j'illustre les fonctions avec des exemples simples qui devraient correspondre aux comportements attendus

# Simulons les structures de données des départements
departements_possedes = [
    "01", "03", "06", "07", "08", "10", "13", "15", "18", "21",
    "23", "25", "26", "29", "30", "31", "34", "37", "38", "41",
    "42", "43", "44", "45", "46", "49", "50", "52", "54", "57",
    "59", "60", "62", "63", "66", "68", "69", "71", "72", "73",
    "75", "76", "77", "78", "80", "81", "83", "84", "87", "89"
]
departements_doublons = {
    "01": 2, "13": 3, "29": 2, "44": 2, "49": 3, "59": 2,"63": 2,"69": 2,"75": 3,"77": 2,"78": 2,"83": 1,"84": 2,"89": 2,"50": 2,"34": 2,"42": 2,"76": 3,"21": 2,"10": 2
}
departements_manquants = ["02", "04", "05"]

def ajouter_departement(departement):
    if departement not in departements_possedes:
        departements_possedes.append(departement)
        departements_manquants.remove(departement)
    return departements_possedes, departements_manquants

def enlever_departement(departement):
    if departement in departements_possedes:
        departements_possedes.remove(departement)
        departements_manquants.append(departement)
    return departements_possedes, departements_manquants

def ajouter_doublon(departement):
    if departement in departements_possedes:
        if departement in departements_doublons:
            departements_doublons[departement] += 1
        else:
            departements_doublons[departement] = 1
    return departements_doublons

def enlever_doublon(departement):
    if departement in departements_doublons:
        if departements_doublons[departement] > 1:
            departements_doublons[departement] -= 1
        else:
            del departements_doublons[departement]
    return departements_doublons

# Début des tests unitaires
def test_ajouter_departement():
    # Ajout d'un département
    ajouter_departement("02")
    assert "02" in departements_possedes
    assert "02" not in departements_manquants

def test_enlever_departement():
    # Suppression d'un département
    enlever_departement("13")
    assert "13" not in departements_possedes
    assert "13" in departements_manquants

def test_ajouter_doublon():
    # Ajout d'un doublon pour un département déjà possédé
    ajouter_doublon("01")
    assert departements_doublons["01"] == 3

def test_enlever_doublon():
    # Suppression d'un doublon
    enlever_doublon("01")
    assert departements_doublons["01"] == 2

def test_ajouter_nouveau_doublon():
    # Ajout d'un doublon pour un département sans doublon
    ajouter_doublon("73")
    assert departements_doublons["73"] == 1

def test_enlever_dernier_doublon():
    # Suppression du dernier doublon d'un département
    enlever_doublon("83")
    assert "83" not in departements_doublons
