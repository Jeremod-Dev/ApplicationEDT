import json


# =======================
# Fonction qui ouvre le json
# ======================
def ouvreJson():
    data = {}
    with open('donnees.json') as json_data:
        data = json.load(json_data)
    return data


data  = ouvreJson()