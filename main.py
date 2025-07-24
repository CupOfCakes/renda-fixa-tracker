from data_manipulation import man_csv as mc, graphic as gr

file_path = "data/rates.csv"
mc.write_csv(file_path=file_path)
gr.showGraphic(file_path=file_path)
