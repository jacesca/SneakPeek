# pip install gspread
#
# Activate the authenticate process to read google spreadsheets
#  0 Go to https://console.cloud.google.com/
#  1 Enable API Access for a Project if you haven’t done it yet.
#  2 Go to “APIs & Services > Credentials” and choose (Hamburger menu)
#    “Create credentials > Service account key”.
#  3 Fill out the form
#  4 Click “Create” and “Done”.
#  5 Press “Manage service accounts” above Service Accounts.
#  6 Press on ⋮ near recently created service account and select 
#    “Manage keys” and then click on “ADD KEY > Create new key”.
#  7 Select JSON key type and press “Create”. You will automatically 
#    download a JSON file with credentials.
#  8 ***Very important! Go to your spreadsheet and share it with a 
#    <<client_email>> from the step above. Just like you do with any 
#    other Google account. 
#  9 Move the downloaded file to 
#    "C:\Users\jaces\AppData\Roaming\gspread\service_account.json".
# 10 Enable Google Drive API by visiting 
#    https://console.developers.google.com/apis/api/drive.googleapis.com/overview?project=210185355683
#    https://console.cloud.google.com/apis/api/sheets.googleapis.com/metrics?project=gcp-test-308700
# 11 Create the python code

import gspread


gc = gspread.service_account()

# Open a sheet from a spreadsheet in one go
wks = gc.open("TestServiceAccount").sheet1

# Update a range of cells using the top left corner address
wks.update('A1', [[1, 2], [3, 4]])

# Or update a single cell
wks.update('B42', "it's down there somewhere, let me take another look.")


# Format the header
wks.format('A1:B1', {'textFormat': {'bold': True}})

# Writing cell
wks.update_cell(5, 2, 'Hola')
