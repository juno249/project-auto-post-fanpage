import requests
import datetime

# don't change this!
#fanpageID = 1549950165266687
fanpageID = input('enter your fanpage ID: ')
apiUrl = 'https://graph.facebook.com/'+fanpageID+'/feed?'; 

#token from graph API : https://developers.facebook.com/tools/explorer
#token = 'EAACEdEose0cBAIR3y15oZBtnXBG3ZAkMDz0NPYZANbFBFQppDXcLsZAxXYxIvk0O1mtFxXlGuk6de1GycHvboZAH3OnlTbAa0T0tZAOygBxP4zvjOq39qnBySuj6tABxZA6jacgZA4OrCOEP2yZCYhkApNtVApSsbHAZAhPXVB29fCswZDZD';
token = input('enter your token from https://developers.facebook.com/tools/explorer :')

# your content
message = 'This is 8h40 post';

# your time
#time = 1453389600;


def Post(apiUrl,token,message,time):
    payload = {
        'access_token' : token,
        'published' : 'false',
        'message' : message,
        'scheduled_publish_time': time
    }

    respond = requests.post(apiUrl,data=payload)
    if respond.status_code == 200:
        print("Post successful")
        print("post date ",datetime.datetime.fromtimestamp(time))
    else:
        print(respond.content)

def convertTime(year,month,day,hour,minute,second):
    date = datetime.datetime(year,month,day,hour,minute,second)
    return datetime.datetime.timestamp(date)

##Post(apiUrl,token,"hello 2 wwhy", time) #testing
        

import pyexcel as pe
records = pe.iget_records(file_name="content.xlsx") #import from excel file
for record in records: # for line by lines in sheet
    date = convertTime(record['Year'],record['Month'],record['Day'],record['Hour'],record['Minute'],record['Second'])
    date = int(date)
    Post(apiUrl,token,record['Message'],date)
