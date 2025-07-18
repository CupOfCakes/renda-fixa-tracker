from datetime import datetime, timedelta
import requests


# all results are in %
def get_selic_rate():
    current_date = datetime.now().strftime("%d/%m/%Y")

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


def get_ipca_rate():
    date = (datetime.now() - timedelta(days=30)).strftime("%d/%m/%Y")

    url_ipca = (
        f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.433/dados?"
        f"formato=json&dataInicial={date}&dataFinal={date}"
    )

    try:
        ipca = requests.get(url_ipca)
        ipca.raise_for_status()
        ipca = ipca.json()

        if not ipca:
            return "NU"

        return ipca[0]

    except Exception as e:
        return "Erro ao obter a taxa Selic: ", e

def get_gross_cdi_rate():
    for i in range(2):
        date = (datetime.now() - timedelta(days=i)).strftime("%d/%m/%Y")

        url_cdi = (
            f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.4389/dados?"
            f"formato=json&dataInicial={date}&dataFinal={date}"
        )

        try:
            response = requests.get(url_cdi)
            response.raise_for_status()
            data = response.json()

            if data:
                return data[0]

        except requests.RequestException as e:
            #print(f"Erro ao obter CDI em {date}: {e}")
            pass

    return "NU"


def get_net_cdi_rate():
    gross_cdi = get_gross_cdi_rate()
    nominal_gross_cdi = float(gross_cdi["valor"])/100

    ipca = get_ipca_rate()
    ipca = float(ipca["valor"])/100

    net_cdi = (((1 + nominal_gross_cdi) / (1 + ipca)) - 1) * 100

    return round(net_cdi, 2)


print(get_net_cdi_rate())
