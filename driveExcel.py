import gspread
from oauth2client.service_account import ServiceAccountCredentials 
import Constants as grupo

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
cred = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(cred)
SQV = client.open("CortesOLGA").sheet1
SI = client.open("CortesOLGA").get_worksheet(1)

def carga(data: object) -> bool:
    dataFila = [data.dia, data.hora, data.usuario, data.tipo, data.mensaje, "", "Pendiente"] 
    
    if data.group == grupo.SoneGrupo:
        data = SQV.get_all_records()
        SQV.insert_row(dataFila, len(data)+2)
        print("cargado en Drive")

    elif  data.group == grupo.SeriaGrupo:
        data = SI.get_all_records()
        SI.insert_row(dataFila, len(data)+2)
        print("cargado en Drive")
    
    return True