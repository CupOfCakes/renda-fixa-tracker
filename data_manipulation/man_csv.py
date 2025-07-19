import csv
from extractor import ext_rate as extr
import os


def get_data():
    gross_cdi = extr.get_gross_cdi_rate()
    net_cdi = extr.get_net_cdi_rate()
    selic = extr.get_selic_rate()
    ipca = extr.get_ipca_rate()

    data = [
        {'name': 'Selic', 'date': selic["data"], 'value': selic["valor"]},
        {'name': 'Gross CDI', 'date': gross_cdi["data"], 'value': gross_cdi["valor"]},
        {'name': 'IPCA', 'date': ipca["data"], 'value': ipca["valor"]},
        {'name': 'Net CDI 22.5%', 'date': selic['data'], 'value': net_cdi['180']},
        {'name': 'Net CDI 20%', 'date': selic['data'], 'value': net_cdi['360']},
        {'name': 'Net CDI 17.5%', 'date': selic['data'], 'value': net_cdi['720']},
        {'name': 'Net CDI 15%', 'date': selic['data'], 'value': net_cdi['720+']}
    ]

    return data


def write_csv():
    file_path = "../data/test.csv"
    datas = get_data()
    header = ["name", "date", "value"]
    if not os.path.exists(file_path):
        with open(file_path, 'w', newline="", encoding="utf-8") as archive:
            write = csv.DictWriter(archive, fieldnames=header)
            write.writeheader()
            write.writerows(datas)
    else:
        with open(file_path, 'a', newline="", encoding="utf-8") as archive:
            write = csv.DictWriter(archive, fieldnames=header)
            write.writerows(datas)


write_csv()
