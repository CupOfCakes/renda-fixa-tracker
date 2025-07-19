import csv
from extractor import ext_rate as extr
import os


def already_exists(entry, file_path):
    if not os.path.exists(file_path):
        return False
    with open(file_path, 'r', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['date'] == entry['date']:
                return True
    return False


def get_data():
    gross_cdi = extr.get_gross_cdi_rate()
    net_cdi = extr.get_net_cdi_rate()
    selic = extr.get_selic_rate()
    ipca = extr.get_ipca_rate()

    data = [
        {'name': 'Selic', 'date': selic["data"], 'value': selic["valor"]},
        {'name': 'Gross CDI', 'date': gross_cdi["data"], 'value': gross_cdi["valor"]},
        {'name': 'IPCA', 'date': ipca["data"], 'value': ipca["valor"]},
        {'name': 'Net CDI 22.5%', 'date': selic["data"], 'value': net_cdi['180']},
        {'name': 'Net CDI 20%', 'date': selic["data"], 'value': net_cdi['360']},
        {'name': 'Net CDI 17.5%', 'date': selic["data"], 'value': net_cdi['720']},
        {'name': 'Net CDI 15%', 'date': selic["data"], 'value': net_cdi['720+']}
    ]

    return data


def write_csv():
    file_path = "../data/rates.csv"
    datas = get_data()
    header = ["name", "date", "value"]

    filtred_data = [d for d in datas if not already_exists(d, file_path)]

    write_mode = 'a' if os.path.exists(file_path) else 'w'

    with open(file_path, write_mode, newline="", encoding="utf-8") as archive:
        writer = csv.DictWriter(archive, fieldnames=header)
        if write_mode == 'w':
            writer.writeheader()
        writer.writerows(filtred_data)

    print(f"{len(filtred_data)} registros salvos com sucesso!!!")


write_csv()
