import requests
import pandas as pd
from tqdm import tqdm

from APIBase import AbstractAPI
from datetime import timedelta, datetime

class BimtraAPI(AbstractAPI):

    def __init__(self):
        self.endpoint = 'cat-62'

    def fetch_data(self, idate='2022-06-01 00:00:00.000', fdate='2023-05-13 23:59:00.000'):
        start_date = datetime.strptime(idate, '%Y-%m-%d %H:%M:%S.%f')
        end_date = datetime.strptime(fdate, '%Y-%m-%d %H:%M:%S.%f')

        total_days = (end_date - start_date).days + 1

        current_date = start_date
        index = 1  # Ordered index

        for _ in tqdm(range(total_days), desc="Fetching data"):
            start_of_day = current_date.strftime('%Y-%m-%d 00:00:00.000')
            end_of_day = current_date.strftime('%Y-%m-%d 23:59:59.999')

            headers = {
                'accept': 'application/json'
            }

            params = {
                'token': self.TOKEN,
                'idate': start_of_day,
                'fdate': end_of_day
            }

            response = requests.get(f"{self.BASE_URL}{self.endpoint}", headers=headers, params=params)

            if response.status_code == 200:
                # Assuming save_data also saves the index; modify as needed
                self.save_data(response.json(), index=index)
                index += 1
            else:
                print(f"Error fetching data from {self.endpoint}. Status Code: {response.status_code}")

            # Move to the next day
            current_date += timedelta(days=1)

    def save_data(self, data, **kwargs):
        index = kwargs['index']
        # Convert timestamps to readable dates
        # for entry in consumers:
        #     entry['dt_dep'] = datetime.datetime.fromtimestamp(entry['dt_dep'] / 1000.0).strftime('%Y-%m-%d %H:%M:%S')
        #     entry['dt_arr'] = datetime.datetime.fromtimestamp(entry['dt_arr'] / 1000.0).strftime('%Y-%m-%d %H:%M:%S')

        # Convert the list of dictionaries to a DataFrame
        df = pd.DataFrame(data)

        # Save the DataFrame to a CSV file
        df.to_csv(f"../data/{index}_{self.endpoint.strip('/').replace('/', '_')}.csv", index=False)
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

bimtra = BimtraAPI()
bimtra.fetch_data()
