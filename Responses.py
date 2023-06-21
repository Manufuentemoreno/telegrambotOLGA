from datetime import datetime

bloqueEntero = ["bloque entero", "entero", "bloque", "bloqueentero", "bloqe", "boque"]

class peticion : 
    mensaje = ""
    bloque = False
    drive = True
    rta = False

def respuestas(input_text: str) -> object:
    indicacion = str(input_text).lower()
    momento = datetime.now()
    data_momento = momento.strftime("%d/%m/%y, %H:%M:%S")

    response = peticion()

    # LINK DEL DRIVE
    if "drive" in indicacion:
        response.mensaje = "Link: https://docs.google.com/spreadsheets/d/1gR9xNEhYWcS2XqRWDOdAi2a6AvVTaM7pHbGh49WSy8w/edit?usp=sharing"
        response.drive = False
        return response

    # BLOQUE ENTERO
    if any([palabra in indicacion for palabra in bloqueEntero]):
        # response.mensaje = f"Pedido Bloque Entero cargado en Drive - {data_momento}"
        response.bloque = True
        return response


    # CORTE DE MOMENTO
    # response.mensaje = f"Pedido Corte cargado en Drive - {data_momento}"
    return response

# Agrega data a algo ya enviado antes
def actualiza():
    response = peticion()
    # response.mensaje = "Ok. Actualizado"
    return response