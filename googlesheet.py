from googleapiclient import discovery
import httplib2
import os
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
import datetime
import gspread
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

SCOPES = 'https://www.googleapis.com/auth/spreadsheets'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Sheets API Python Quickstart'

def get_credentials():
    """Gets valid user credentials from storage.
    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.
    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'sheets.googleapis.com-python-quickstart.json')
    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

credentials = get_credentials()
http = credentials.authorize(httplib2.Http())
discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                'version=v4')
service = discovery.build('sheets', 'v4', http=http, discoveryServiceUrl=discoveryUrl)

gc = gspread.authorize(credentials)
# Open up the workbook based on the spreadsheet name
SPREADSHEET = "the_name_of_your_spreadsheet"
workbook = gc.open(SPREADSHEET)
# Get the first sheet
sheet = workbook.sheet1
# Extract all data into a dataframe
res = pd.DataFrame(sheet.get_all_records())

datelist = res.Time.tolist()
fmt = '%Y-%m-%d %H:%M:%S' # check the time format of the timestamp in the first column
x_axis = [datetime.datetime.strptime(dat, fmt) for dat in datelist]
vary1 = 'T outside [ºC]' # name of the column you want to plot, typically written in the first row
vary2 = 'T inside [ºC]'

plt.style.use('ggplot')
xFmt = mdates.DateFormatter('%d-%m')
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x_axis,res[vary1],'b', label=vary1)
ax.fill_between(x_axis, 0, res[vary1], facecolor='blue', alpha=0.25)
ax.plot(x_axis,res[vary2],'r', label=vary2)
ax.fill_between(x_axis, 0, res[vary2], facecolor='red', alpha=0.25)
ax.xaxis.set_major_formatter(xFmt)
fig.autofmt_xdate()
ax.legend(loc=2)
fig.savefig('/tmp/temperatures.png') # file name in your local system