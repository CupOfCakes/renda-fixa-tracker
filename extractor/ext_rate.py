from datetime import datetime
import requests


def get_selic_rate():
    current_date = datetime.now().date().strftime("%d/%m/%Y")

    url_selic = ("https://api.bcb.gov.br/dados/serie/bcdata.sgs.432/dados?formato=json&"
                 f"dataInicial={current_date}&dataFinal={current_date}")

    try:
        selic = requests.get(url_selic)
        selic.raise_for_status()
        selic = selic.json()

        if not selic:
            return "NU" 

        return selic[0]

    except Exception as e:
        return "Erro ao obter a taxa Selic: ", e
