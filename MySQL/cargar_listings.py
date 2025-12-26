import os
import time
import pandas as pd
from sqlalchemy import create_engine, event
from urllib.parse import quote_plus

print("Script arrancó")

DB_USER = "root"
DB_PASSWORD = "Picolina23@23"   
DB_HOST = "127.0.0.1"
DB_PORT = 3306
DB_NAME = "airbnb_project"

CSV_FILE = r"C:\ProgramData\MySQL\MySQL Server 8.0\Uploads\listings_clean.csv"
TABLE_NAME = "listings"

CHUNK_SIZE = 50000

print("Ruta CSV:", CSV_FILE)
print("Archivo existe:", os.path.exists(CSV_FILE))

dbc_str = (
    "DRIVER={MySQL ODBC 9.5 Unicode Driver};"
    f"SERVER={DB_HOST};"
    f"PORT={DB_PORT};"
    f"DATABASE={DB_NAME};"
    f"UID={DB_USER};"
    f"PWD={DB_PASSWORD};"
    "MULTI_HOST=1;"
)

connect_url = "mysql+pyodbc:///?odbc_connect=" + quote_plus(dbc_str)

print("Creando engine...")
engine = create_engine(connect_url)
print("Engine creado. Empezando a leer el CSV...")

@event.listens_for(engine, "before_cursor_execute")
def receive_before_cursor_execute(conn, cursor, statement, params, context, executemany):
    try:
        cursor.fast_executemany = True
    except Exception:
        pass

try:
    first_chunk = True
    chunk_number = 0
    start_total = time.time()

    for chunk in pd.read_csv(CSV_FILE, chunksize=CHUNK_SIZE):
        chunk_number += 1
        print("Procesando lote:", chunk_number, "- filas:", len(chunk))
        start_chunk = time.time()

        if first_chunk:
            chunk.to_sql(
                TABLE_NAME,
                con=engine,
                if_exists="replace",
                index=False,
                method="multi",
                chunksize=100,
            )
            first_chunk = False
        else:
            chunk.to_sql(
                TABLE_NAME,
                con=engine,
                if_exists="append",
                index=False,
                method="multi",
                chunksize=100,
            )

        elapsed = time.time() - start_chunk
        print("Lote", chunk_number, "insertado en", round(elapsed, 2), "segundos")

    total_elapsed = time.time() - start_total
    print("Carga completa en", round(total_elapsed / 60, 2), "minutos")

except Exception as e:
    print("Error durante la carga:")
    print(str(e))

print("Script terminó.")
