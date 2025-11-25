import requests
import time
import pandas as pd

URL = "https://dataportal.livsmedelsverket.se/livsmedel/api/v1"

# get nutritions
def get_nutritions(limit=200, sprak=1, delay=0.1):
    
    url = f"{URL}/livsmedel"
    offset = 0
    nutritions = []

    while True:
        params = {
            "offset": offset,
            "limit": limit,
            "sprak": sprak
        }

        try:
            response = requests.get(url, params=params, timeout=20)
            response.raise_for_status()
        except requests.exceptions.RequestException as err:
            print(f"Offset error: {err}")
            break

        try:
            data = response.json()
        except ValueError as err:
            print(f"JSON error: {err}")
            break

        nutrition_data = data.get("livsmedel", [])
        if not isinstance(nutrition_data, list):
            print(f"API call in wrong format")
            break

        nutritions.extend(nutrition_data)

        if len(nutrition_data) < limit:
            break

        offset += limit
        time.sleep(delay)

    return nutritions

# get values
def get_nutrition_values(nummer, sprak=1):
    url = f"{URL}/livsmedel/{nummer}/naringsvarden"
    params = {"sprak": sprak}

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as err:
        print(f"Error getting values for {nummer}: {err}")
        return []

    try:
        data = response.json()
    except ValueError as err:
        print(f"JSON error: {err}")

    if isinstance(data, list):
        return data

    if isinstance(data, dict):
        return data.get("naringsvarden", [])

    print(f"Wrong format for values in {nummer}")
    return []

# get food_group
def get_food_group(nummer, sprak=1):
    url = f"{URL}/livsmedel/{nummer}/klassificeringar"
    params = {"sprak": sprak}

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
    except Exception as e:
        print(f"Error getting values for {nummer}: {e}")

    for item in data:
        if item.get("typ") == "Huvudgrupp":
            return item.get("kod", "Övrigt")
    
    return "Övrigt"


# create df
def create_dataframe():
    try:
        products = get_nutritions()
    except Exception as e:
        print(f"Couldn't get product list: {e}")
        return pd.DataFrame()

    records = []

    for item in products:
        number = item["nummer"]
        name = item["namn"]

        value_list = get_nutrition_values(number)
        group = get_food_group(number)

        for value in value_list:
            records.append({
                "nummer": number,
                "namn": name,
                "naringsnamn": value.get("namn"),
                "gruppering": group,
                "mangd": value.get("varde"),
                "enhet": value.get("enhet")
            })

        time.sleep(0.05)

    df = pd.DataFrame(records)

    return df