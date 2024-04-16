import gspread
from oauth2client.service_account import ServiceAccountCredentials 
import Constants as grupo

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
cred = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(cred)

MILTON = client.open("IntertandasTarde").sheet1
DORADA = client.open("IntertandasTarde").get_worksheet(1)
NONA = client.open("IntertandasTarde").get_worksheet(2)
PRIMO = client.open("IntertandasTarde").get_worksheet(3)

def carga(data: object) -> bool:
    dataFila = [data.dia, data.hora, data.mensaje, data.usuario, "", "Pendiente"] 
    
# MILTON
    if  data.diaSem == "Monday":

        datosCargados = MILTON.get_all_records()
        ultimaFilaCargada = len(datosCargados)+1
        ultimaCargaHora = str(MILTON.cell(ultimaFilaCargada,2).value)
        print(ultimaCargaHora[-2]+ultimaCargaHora[-1])
        ultimaCargaMinutos = int(ultimaCargaHora[-2]+ultimaCargaHora[-1])
        print("hasta aca")

        if ultimaCargaHora == data.hora or ultimaCargaMinutos+1 == int(data.hora[3:5]):
            columnaMensaje = 3
            valor = str(MILTON.cell(ultimaFilaCargada,columnaMensaje).value)
            MILTON.update_cell(ultimaFilaCargada,columnaMensaje,f"{valor} | {data.mensaje}")
            print("celda actualizada en Drive")
            return

        MILTON.insert_row(dataFila, len(datosCargados)+2)
        print("cargado en Drive")

# GEN DORADA
    elif data.diaSem == "Tuesday":

        datosCargados = DORADA.get_all_records()
        ultimaFilaCargada = len(datosCargados)+1
        ultimaCargaHora = str(DORADA.cell(ultimaFilaCargada,2).value)
        ultimaCargaMinutos = int(ultimaCargaHora[-2]+ultimaCargaHora[-1])
        
        if ultimaCargaHora == data.hora or ultimaCargaMinutos+1 == int(data.hora[3:5]):
            columnaMensaje = 3
            valor = str(DORADA.cell(ultimaFilaCargada,columnaMensaje).value)
            DORADA.update_cell(ultimaFilaCargada,columnaMensaje,f"{valor} | {data.mensaje}")
            print("celda actualizada en Drive")
            return

        DORADA.insert_row(dataFila, len(datosCargados)+2)
        print("cargado en Drive")
    
# NONA
    elif data.diaSem == "Wednesday":
        
        datosCargados = NONA.get_all_records()
        ultimaFilaCargada = len(datosCargados)+1
        ultimaCargaHora = str(NONA.cell(ultimaFilaCargada,2).value)
        ultimaCargaMinutos = int(ultimaCargaHora[-2]+ultimaCargaHora[-1])
        
        if ultimaCargaHora == data.hora or ultimaCargaMinutos+1 == int(data.hora[3:5]):
            columnaMensaje = 3
            valor = str(NONA.cell(ultimaFilaCargada,columnaMensaje).value)
            NONA.update_cell(ultimaFilaCargada,columnaMensaje,f"{valor} | {data.mensaje}")
            print("celda actualizada en Drive")
            return

        NONA.insert_row(dataFila, len(datosCargados)+2)
        print("cargado en Drive")
# PRIMO
    elif data.diaSem == "Thursday":

        datosCargados = PRIMO.get_all_records()
        ultimaFilaCargada = len(datosCargados)+1
        ultimaCargaHora = str(PRIMO.cell(ultimaFilaCargada,2).value)
        ultimaCargaMinutos = int(ultimaCargaHora[-2]+ultimaCargaHora[-1])
        
        if ultimaCargaHora == data.hora or ultimaCargaMinutos+1 == int(data.hora[3:5]):
            columnaMensaje = 3
            valor = str(PRIMO.cell(ultimaFilaCargada,columnaMensaje).value)
            PRIMO.update_cell(ultimaFilaCargada,columnaMensaje,f"{valor} | {data.mensaje}")
            print("celda actualizada en Drive")
            return

        PRIMO.insert_row(dataFila, len(datosCargados)+2)
        print("cargado en Drive")

    return True

def agregaDatos(data: object) -> bool:
    
    if data.group == grupo.SoneGrupo:
        SQV = client.open("CortesOLGA").sheet1

        datosCargados = SQV.get_all_records()
        fila = len(datosCargados)+1
        columnaMensaje = 3
        valor = str(SQV.cell(fila,columnaMensaje).value)
        SQV.update_cell(fila,columnaMensaje,f"{valor} | {data.mensaje}")
        print("celda actualizada en Drive")

    # elif  data.group == grupo.SeriaGrupo:
    #     datosCargados = SI.get_all_records()
    #     fila = len(datosCargados)+1
    #     columnaMensaje = 3
    #     valor = str(SI.cell(fila,columnaMensaje).value)
    #     SI.update_cell(fila,columnaMensaje,f"{valor} | {data.mensaje}")
    #     print("celda actualizada en Drive")

    return True