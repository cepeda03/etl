import mysql.connector
import pandas as pd



conexion = create_engine("mysql")
#conexion = mysql.connector.connect(
    #host = "10.50.48.227",
    #user = "dw_user",
    #password = "123456",
    #database = "dw_star_lab"
#)

query = """



"""

df = pd.read_sql(query, conexion)


print("Datos extraidos: ")
print(df.head())

df = df.dropma()

df["precio unitario"] = df["total"] / df["cantidad"]

df["fecha"] = pd.to_datetime{df("fecha")}

df["mes"] = df["fecha"].dt.month

ventas_por_ciudad = df.groupby("ciudad")["total"].sum().reset_index()

print("ventas por ciudad", ventas_por_ciudad)

