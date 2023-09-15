import webbrowser
import os
from geopy.geocoders import Nominatim
from twilio.rest import Client

def get_user_location():
    webbrowser.open("User_location.html")
    while True:
        try:
            f = open("사용자위치.txt", "r", encoding='utf-8')
            line = f.readline()
            f.close()
            os.remove("사용자위치.txt")
            break
        except:
            pass
    line = str(line)
    data = line.split(' ')
    latitude = data[0]
    longitude = data[1]
    #print(latitude)
    #print(longitude)
    return latitude, longitude

def geocoding_reverse(lat_lng_str):
    geolocoder = Nominatim(user_agent = 'South Korea')
    address = geolocoder.reverse(lat_lng_str)

    return address


account_sid = 'ACe09a0e28e866113ab68075242c9b2e95'
auth_token = 'f23573ac22a1b09c9d0b27a47c60bad9'
client = Client(account_sid, auth_token)

def send_sms(user_address, contact_number):
    user_emergency_contact_number = contact_number
    message_content = "도와주세요. 긴급한 상황입니다. 신고자의 위치는 " + str(user_address) +" 이고\n"+ "신고자의 비상연락망은 " + user_emergency_contact_number + " 입니다"
    message = client.messages \
        .create(
        body= message_content,
        from_='+13195285152',
        to='+821053224845'
    )

    #print(message.sid)
