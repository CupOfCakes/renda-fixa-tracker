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
    for i in range(10):
        date = (datetime.now() - timedelta(days=i)).strftime("%d/%m/%Y")

        url_cdi = (
            f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.4389/dados?"
            f"formato=json&dataInicial={date}&dataFinal={date}"
        )

        try:
            response = requests.get(url_cdi)
            response.raise_for_status()
            data = response.json()

            if data and isinstance(data, list):
                return data[0]

        except requests.RequestException as e:
            #print(f"Erro ao obter CDI em {date}: {e}")
            pass

    return "NU"


def get_net_cdi_rate():
    gross_cdi = get_gross_cdi_rate()
    nominal_gross_cdi = float(gross_cdi["valor"]) / 100

    ipca = get_ipca_rate()
    ipca = float(ipca["valor"]) / 100

    faixas_ir = {
        "180": 22.5,
        "360": 20.0,
        "720": 17.5,
        "720+": 15.0
    }

    resultado = {}

    for faixa, aliquota in faixas_ir.items():
        taxa_liquida = nominal_gross_cdi * (1 - aliquota / 100)

        taxa_real = (((1 + taxa_liquida) / (1 + ipca)) - 1) * 100

        resultado[faixa] = round(taxa_real, 2)

    return resultado


def print_all_rates():
    gross_cdi = get_gross_cdi_rate()
    net_cdi = get_net_cdi_rate()
    selic = get_selic_rate()
    ipca = get_ipca_rate()

    print(
        "NAME        DATE        RATE\n"
        f"SELIC       {selic["data"]}  {selic["valor"]}\n"
        f"GROSS CDI   {gross_cdi["data"]}  {gross_cdi["valor"]}\n"
        f"IPCA        {ipca["data"]}  {ipca["valor"]}\n"
        "------------------------------\n"
        "NET CDI\n"
    )

    for key, valor in net_cdi.items():
        print(f"{key}: {valor}")

