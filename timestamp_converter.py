import pandas as pd
from datetime import timedelta

# Carica il file CSV
gps_df = pd.read_csv("GPS_output_TEST.csv", sep=';')

# Converti Timestamp in formato datetime con precisione al millisecondo
gps_df['Timestamp_converted'] = pd.to_datetime(gps_df['Timestamp'], unit='s')

# Aggiungi TimeUS (microsecondi) come timedelta al Timestamp
gps_df['FullTime'] = gps_df['Timestamp_converted'] + pd.to_timedelta(gps_df['TimeUS'], unit='us')

# Salva il nuovo file CSV con i valori convertiti
gps_df.to_csv("GPS_output_with_fulltime.csv", index=False)
  