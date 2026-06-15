'''
read spread sheet and convert into csv
'''

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import requests

# Script for authorization of pydrive.
gauth = GoogleAuth()
gauth.LocalWebserverAuth()

# Download the specific sheet in Google Spreadsheet as a CSV data.
spreadsheetId = '1BLWBL51Th4gtIsKg2uzP0lg5v0RcHxHocjP9ZvMQWeI' # Please set the Spreadsheet ID.
sheetId = '705794348'


# Please set the sheet ID. (GID)
url = 'https://docs.google.com/spreadsheets/d/' + spreadsheetId + '/gviz/tq?tqx=out:csv&gid=' + sheetId
headers = {'Authorization': 'Bearer ' + gauth.credentials.access_token}
res = requests.get(url, headers=headers)
with open('men_tops.csv', 'wb') as f:
    f.write(res.content)
