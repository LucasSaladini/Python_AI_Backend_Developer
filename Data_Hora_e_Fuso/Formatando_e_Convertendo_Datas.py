from datetime import datetime

data_hora_atual = datetime.now()
data_hora_string = "2024-05-23 12:00"

mascara_ptbr = '%d/%m/%Y'
mascara_ptbr_completa = '%d/%m/%Y %a %H:%M:%S'
mascara_en = "%Y-%m-%d %H:%M"

print(data_hora_atual.strftime(mascara_ptbr))
print(data_hora_atual.strftime(mascara_ptbr_completa))

print(datetime.strptime(data_hora_string, mascara_en))
print(type(datetime.strptime(data_hora_string, mascara_en)))