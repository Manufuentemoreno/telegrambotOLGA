import gspread
from oauth2client.service_account import ServiceAccountCredentials 
import Constants as grupo

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
cred = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(cred)
SQV = client.open("CortesOLGA").sheet1

def carga(data: object) -> bool:
    dataFila = [data.dia, data.hora, data.mensaje, data.tipo, data.usuario, "", "Pendiente"] 
   
    if data.group == grupo.SoneGrupo:
        # SQV = client.open("CortesOLGA").sheet1

        datosCargados = SQV.get_all_records()
        ultimaFilaCargada = len(datosCargados)+1
        ultimaCargaHora = str(SQV.cell(ultimaFilaCargada,2).value)
        ultimaCargaMinutos = int(ultimaCargaHora[-2]+ultimaCargaHora[-1])

        if ultimaCargaHora == data.hora or ultimaCargaMinutos+1 == int(data.hora[3:5]):
            columnaMensaje = 3
            valor = str(SQV.cell(ultimaFilaCargada,columnaMensaje).value)
            SQV.update_cell(ultimaFilaCargada,columnaMensaje,f"{valor} | {data.mensaje}")
            print("celda actualizada en Drive")
            return

        SQV.insert_row(dataFila, len(datosCargados)+2)
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