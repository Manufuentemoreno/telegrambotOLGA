from telegram import Update
from telegram.ext import *
import pytz
from datetime import datetime as date

import Constants as keys
import Responses as resp
import driveExcel as driveSQV
import driveExcelTarde as driveTarde

# ***************************** COMANDOS ***************************** 
# async def link_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
# # INTERTANDAS SQV
#     print(update.message.chat.title)
#     if update.message.chat.title == "CORTES SQV":
#         await update.message.reply_text("Link: https://docs.google.com/spreadsheets/d/1gR9xNEhYWcS2XqRWDOdAi2a6AvVTaM7pHbGh49WSy8w/edit?usp=sharing")
#         return

# # INTERTANDAS TARDE
#     await update.message.reply_text("Link: https://docs.google.com/spreadsheets/d/1HHFsjmQ8fd2lsEWZU0KJPqE2B0Ip0MaFbZl_xujLCSk/edit?usp=sharing")


#  ***************************** MENSAJES ***************************** 
async def handlle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text : str = update.message.text
    nombreGrupo = update.message.chat.title
    quienManda = update.message.from_user.first_name
    fechaHora = str(update.message.date)

    print(quienManda+"  -   "+nombreGrupo)
    # INTERTANDAS TARDE

    aceptados = ["Lucas", "Martu", "Yamila", "Manu"]

    # MENSAJES QUE IGNORA
    if quienManda in aceptados:
        print(quienManda)
    else:
        print("ignorado")
        return
    
    if text[0] == "@":
        return

    response: object = resp.respuestas(text)

    # Log solicitud
    print(f"SOLICITUD | Usuario: {quienManda} | Tipo de solicitud: {response.bloque} | Grupo/Pnal: {message_type} | Mensaje: {text} | Tiempo: {fechaHora}")
    
    # Log respuesta
    print("Bot: ", response.mensaje)
    if response.rta:
        await update.message.reply_text(response.mensaje)

    # Carga de contenido en Drive
    response.dia = f"{fechaHora[8:10]}/{fechaHora[5:7]}"
    response.hora = fechaHora[11:16]
    response.usuario = quienManda
    response.tipo = "Bloque Entero" if response.bloque else "Corte"
    response.mensaje = text
    response.group = nombreGrupo
    response.diaSem = date.today().strftime("%A")

    if response.drive and response.group == "CORTES SQV":
        driveSQV.carga(response)
        return
    
    driveTarde.carga(response)

#  ***************************** ERROR  ***************************** 
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"El Update- {update} generó el error- {context.error}")


#  ***************************** INICIALIZA BOT  ***************************** 
def main():

    defaults = Defaults(tzinfo=pytz.timezone('America/Argentina/Buenos_Aires'))

    print("Bot inicializado...")
    app = Application.builder().token(keys.API_KEY).defaults(defaults).build()

    # Comandos
    # app.add_handler(CommandHandler("link", link_command))

    # Mensajes
    app.add_handler(MessageHandler(filters.TEXT, handlle_message))

    # Errores
    app.add_error_handler(error)

    print("Actualizando...")
    app.run_polling(poll_interval=30)

if __name__ == "__main__":
    main()



# MENSAJE PRIV
    #Message(channel_chat_created=False, chat=Chat(first_name='Manu', id=2011249585, type=<ChatType.PRIVATE>), date=datetime.datetime(2023, 6, 20, 1, 27, 35, tzinfo=datetime.timezone.utc), delete_chat_photo=False, from_user=User(first_name='Manu', id=2011249585, is_bot=False, language_code='es'), group_chat_created=False, message_id=9, supergroup_chat_created=False, text='chiste migue')

# MENSAJE GRUPO:
    # Message(channel_chat_created=False, chat=Chat(api_kwargs={'all_members_are_administrators': True}, id=-933134718, title='Volaba', type=<ChatType.GROUP>), date=datetime.datetime(2023, 6, 20, 13, 4, 24, tzinfo=<DstTzInfo 'America/Argentina/Buenos_Aires' -03-1 day, 21:00:00 STD>), delete_chat_photo=False, from_user=User(first_name='Manu', id=2011249585, is_bot=False, language_code='es'), group_chat_created=False, message_id=48, supergroup_chat_created=False, text='Hola')
