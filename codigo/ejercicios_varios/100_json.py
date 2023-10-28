import json
import pandas as pd
# escritura 
datos = {
    "Nombre":["Jose","Diego"],
    "Edad":[25,30]
}
dataframe = pd.DataFrame(datos)
dataframe.to_json("datos.json",orient="records")
# lectura
fichero = "datos.json"
dataframe = pd.read_json(fichero, orient="records")
print(dataframe)