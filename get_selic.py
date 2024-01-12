import requests

def get_selic():
    try:
        # URL Banco Central do Brasil API - dados da SELIC
        api_url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json"

        response = requests.get(api_url)

        if response.status_code == 200:

            selic_data = response.json()

            most_recent_entry = selic_data[len(selic_data)-1]

            value = most_recent_entry["valor"]

            return float(value)
        else:
            print(f"Failed to fetch SELIC data. Status code: {response.status_code}")
            return 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0