import requests
from twilio.rest import Client
api_key="c18477b290ee8bc5eacb64e56def5a04"
OWM_Endpoint="https://api.openweathermap.org/data/2.5/forecast"
account_sid = 'ACb52a7dbd7e3a62801dc7cd7f0810d324'#we get over the twilio this key
auth_token = 'f3d202a65219c56995073b61c1a2ed2d'#we get over the twilio this key

params={
    "lat":41.0252832, #your country latitude position
    "lon":28.8726498,#your country longitude position
    "appid":api_key,
    "cnt":4,##we will find only 4 time sequences in the request, but the buddha will have given a 12-hour forecast, because he gives an estimate of 3 hours
##we have written the parameters in json our latitude longitude location and api key the format version the site wants
# we entered with different names
}

response=requests.get(OWM_Endpoint,params=params)
response.raise_for_status()#if there is a mistake, we asked him to tell us what happened
weather_data=response.json()#we converted the data to json fomratina
will_rain=False
for hour_data in weather_data["list"]:#we have entered the list change of our weather data
    condition_code=(hour_data["weather"][0]['id'])#we have assigned the id to us from the internal ice lists and the condution code to
    if int(condition_code)<700:#if the condition code is less than 700, we gave the message to bring it to the train
        will_rain=True
if will_rain:#if the variable return true
    client = Client(account_sid, auth_token)#the code we got from the document on the twilio page
    message = client.messages.create(
        body="It's going to rain today,Remember to bring an unmbrella ??" ,#our message
        from_='+12098829412',#the virtual number created in twilio
        to='your number'
    )
    print(message.status)