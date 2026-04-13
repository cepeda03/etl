import mysql.connector
import pandas as pd

conexion = mysql.connector.connect(
    host = "10.50.48.227",
    user = "dw_user",
    password = "123456",
    database = "dw_star_lab"
)

query = """



"""

df = pd.read_sql(query, conexion)


print("Datos extraidos: ")
print(df.head())