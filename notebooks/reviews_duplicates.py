import pandas as pd

df = pd.read_csv(
    r"C:/Users/cebal/OneDrive/Documentos/Personal/Data Analyst/Desafio Profesional/airbnb_project/data_clean/reviews_clean.csv"
)

print("Total filas:", len(df))

dups_id = df[df.duplicated(subset=["id"], keep=False)]
print("Total duplicados por id:", len(dups_id))

