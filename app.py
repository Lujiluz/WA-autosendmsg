import pywhatkit as kit
from datetime import datetime, timedelta


# masukkan nomor hp kamu disini..
phone_numbers = []

message = """
halo, salam kenal aku Zul dari kuas 👋🏻 
kamu yg tahun lalu ikut lomba SKAK 5 yaa? kali ini kuas ngadain lomba lagi nih dengan mata lomba tari tradisional solo. nah, aku mau tanya boleh? di sekolah kamu ada eskul tari yg aktif ga yaa? makasiii ☺️
"""

def send_message():
    try:
        for i, number in enumerate(phone_numbers):
            print(f"sending message no. {i + 1}...")
            kit.sendwhatmsg_instantly(number, message, 10, True, 2)
            print(f'message sent!')
    except:
        print('unexpected error occurs')

if __name__ == '__main__':
    send_message()