import pandas as pd

df = pd.read_csv("C:/Users/cebal/OneDrive/Documentos/Personal/Data Analyst/Desafio Profesional/airbnb_project/data_clean/calendar_clean.csv")

print("Total filas:", len(df))

dups = df[df.duplicated(subset=["listing_id", "date"], keep=False)]

print("Total duplicados:", len(dups))

print(dups.head(20))

