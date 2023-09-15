from datetime import datetime

import requests
import pandas as pd

from APIBase import AbstractAPI

DATEFORMAT = '%Y-%m-%d %H:%M:%S'

class SatelliteAPI(AbstractAPI):

    def __init__(self):
        self.endpoint = 'satelite'

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
        for entry in data:
            date_obj = datetime.strptime(entry['data'], DATEFORMAT)
            entry['data'] = date_obj.strftime("%Y%m%d%H%M%S")

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

sat = SatelliteAPI()
sat.fetch_data()