import datetime

import requests
import pandas as pd
from abc import ABC, abstractmethod


class AbstractAPI(ABC):
    BASE_URL = "http://montreal.icea.decea.mil.br:5002/api/v1/"
    TOKEN = "a779d04f85c4bf6cfa586d30aaec57c44e9b7173"  # enviar para arquivo de configuracao
    endpoint = ''

    @abstractmethod
    def fetch_data(self):
        pass

    @abstractmethod
    def save_data(self, data, **kwargs):
        pass

