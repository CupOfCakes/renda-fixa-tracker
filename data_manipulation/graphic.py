import pandas as pd
import matplotlib.pyplot as plt


def showGraphic(file_path="../data/rates.csv"):
    # Lê o arquivo CSV
    df = pd.read_csv(file_path)

    # Converte a coluna de data
    df["date"] = pd.to_datetime(df["date"], dayfirst=True)

    # Cria o gráfico
    plt.figure(figsize=(12, 6))

    for name, group in df.groupby("name"):
        plt.plot(group["date"], group["value"], marker='o', label=name)

    # Estiliza o gráfico
    plt.title("Taxas ao Longo do Tempo")
    plt.xlabel("Data")
    plt.ylabel("Valor (%)")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()

    plt.show()
