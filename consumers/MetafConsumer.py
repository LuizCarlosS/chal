import requests
import pandas as pd

from APIBase import AbstractAPI


class MetafAPI(AbstractAPI):

    def __init__(self):
        self.endpoint = 'metaf'

    def fetch_data(self, idate='2022-06-01', fdate='2023-05-13'):
        headers = {
            'accept': 'application/json'
        }
        params = {
            'token': self.TOKEN,
            'idate': idate,
            'fdate': fdate
        }

        response = requests.get(f"{self.BASE_URL}{self.endpoint}", headers=headers, params=params)

        if response.status_code == 200:
            self.save_data(response.json())
            return response.json()
        else:
            print(f"Erro ao buscar dados de {self.endpoint}. Status Code: {response.status_code}")
            return None

    def save_data(self, data):
        # Convert timestamps to readable dates
        # for entry in consumers:
        #     entry['dt_dep'] = datetime.datetime.fromtimestamp(entry['dt_dep'] / 1000.0).strftime('%Y-%m-%d %H:%M:%S')
        #     entry['dt_arr'] = datetime.datetime.fromtimestamp(entry['dt_arr'] / 1000.0).strftime('%Y-%m-%d %H:%M:%S')

        # Convert the list of dictionaries to a DataFrame
        df = pd.DataFrame(data)

        # Save the DataFrame to a CSV file
        df.to_csv(f"../data/{self.endpoint.strip('/').replace('/', '_')}.csv", index=False)
        print(f"Dados de {self.endpoint} salvos com sucesso!")


datasets_endpoints = [
    "/bimtra",
    "/cat-62",
    "/esperas",
    "/metaf",
    "/metar",
    "/satelite",
    "/tc-prev",
    "/tc-real"
]

metaf = MetafAPI()
metaf.fetch_data()