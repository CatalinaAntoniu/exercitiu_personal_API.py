import json
from configsx import file_path, fisier_optiuni_denumire
import datetime
import asyncio
import telegram


print("Bun venit la Rutina de miscare zilnica pentru  o sanatate de fier!")
print("Fiecare optiune arde un anumit numar de calorii daca timpul de practica este o ora/zi")


with open(f'{file_path}/{fisier_optiuni_denumire}', 'r') as f:
    data = json.loads(f.read())
    #print(json.dumps(Optiune_1, indent=2))

print(data)
lista_optiuni = data['elemente']
print(type(lista_optiuni))
print(len(lista_optiuni))


print("Alegeți o optiune din lista, rutina dv pe care doriti sa o exersati zilnic:")


for index, element in enumerate(lista_optiuni):
    #print(lista_optiuni[i])
    print(f"Pentru optiunea #{index+1} aveti activitatile sportive recomadate:")
    for key, value in element.items():
        print(f"{key}:  calorii arse {value} ")
    print(f"{'_'*20}")

optiune_aleasa = input("Introduceți numărul corespunzător opțiunii: ")

optiune_aleasa_dictionar = lista_optiuni[int(optiune_aleasa)-1]

# Afișarea opțiunii selectate
if optiune_aleasa.isnumeric() and optiune_aleasa_dictionar in lista_optiuni:
    print("Ați selectat opțiunea:", optiune_aleasa)
else:
    # Afișarea unei erori în cazul în care valoarea introdusă nu se află în lista de opțiuni
    print("Valoarea introdusă nu este validă!")



# afisam ce rutina trebuie sa  faca utilizatorul in functie de momentul zilei

while True:
    now = datetime.datetime.now()

    dimineata = datetime.time(7, 0, 0)
    seara = datetime.time(18, 0, 0)

    mesaj_dimineata = "Buna dimineata, este timpul pt prima rutina!"
    mesaj_seara = "Buna seara, este timpul pt a doua rutina!"
    mesaj_noapte = "Este timpul de somn!!"


    if dimineata <= now.time() < seara:
        print(mesaj_dimineata)
    elif seara <= now.time() <= datetime.time(7, 0, 0):
        print(mesaj_seara)
    else:
        print(mesaj_noapte)

        break


# pt a primi mesajul in telegram

tg_api = "6010269247:AAGAEgctZzTjB-uQ2WccRx40rNxkB0rYlOU"
id_Catalina = 5442026236
text_to_send = mesaj_seara or mesaj_dimineata or mesaj_noapte
if seara <= now.time() <= datetime.time(7, 0, 0):
    text_to_send = mesaj_seara
elif dimineata <= now.time() < seara:
    text_to_send = mesaj_dimineata
else:
    text_to_send = mesaj_noapte
async def send_mes(id,text):
    bot = telegram.Bot(tg_api)
    async with bot:
        await bot.sendMessage(id, text)

asyncio.run(send_mes(id_Catalina, text_to_send))


