import pandas as pd
import numpy as np
import datetime as dt

# Configurações
start_date = dt.datetime(2025, 1, 1)
end_date = start_date + dt.timedelta(days=7)
freq = "15min"

# Geração de timestamps
timestamps = pd.date_range(start=start_date, end=end_date, freq=freq)

data = []
sensor_id = 1

for ts in timestamps:
    # Temperatura (22-25 dia, 18-20 noite)
    temp = np.random.normal(23 if 8 <= ts.hour <= 20 else 19, 1)
    
    # Luminosidade (0 noite, 200-500 lux dia)
    lux = 0 if ts.hour < 6 or ts.hour > 20 else np.random.randint(200, 500)
    
    # Ocupação (horário comercial 9h-18h, dias úteis)
    occupied = 1 if (ts.weekday() < 5 and 9 <= ts.hour <= 18) else np.random.choice([0,1], p=[0.9,0.1])
    
    data.append([ts, "temp", sensor_id, round(temp,2)])
    data.append([ts, "lux", sensor_id+1, lux])
    data.append([ts, "occupancy", sensor_id+2, occupied])

df = pd.DataFrame(data, columns=["timestamp","sensor_type","sensor_id","value"])

df.to_csv("smart_office_data.csv", index=False)
print("Arquivo smart_office_data.csv gerado com sucesso!")
