from bs4 import BeautifulSoup
import lxml
import requests
from googleapiclient.discovery import build
from google.oauth2 import service_account
from selenium import webdriver
import os

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)

SERVICE_ACCOUNT_FILE = 'creds.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

def OverviewExractor(url):
    driver.get(url)
    driver.implicitly_wait(3)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.implicitly_wait(3)
    soup = BeautifulSoup(driver.execute_script('return document.documentElement.outerHTML'), 'html.parser')

    #soup = BeautifulSoup(source, 'lxml')
    table = soup.find('table', {'id': 'tblTS2'})
    rows = table.find_all('tr')
    overview = []
    for row in rows:
        RowData = []
        cols = row.find_all('td')
        for col in cols:
            name = col.find('span').text
            number = col.find('a').text
            RowData.append(number)
            RowData.append(name)
            break
        cols = row.find_all('td', class_='txt_r')
        for col in cols:
            RowData.append(col.text)


        overview.append(RowData)
    del overview[0]
    return overview


# If modifying these scopes, delete the file token.json.


# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1nuo5qffcnK1jPvxOy3AMO_IvjdV1v7h7pqWp21i1r4U'


service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()
#result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
#                            range="Sheet1!A1:G5").execute()
#values = result.get('values', [])

#High Stocks
High_1_month = 'http://www.aastocks.com/tc/stocks/market/high-low-stocks.aspx?catg=1&period=1&t=1&p='
High_3_month = 'http://www.aastocks.com/tc/stocks/market/high-low-stocks.aspx?catg=1&period=2&t=1&p='
High_6_month = 'http://www.aastocks.com/tc/stocks/market/high-low-stocks.aspx?catg=1&period=6&t=1&p='
High_52_week = 'http://www.aastocks.com/tc/stocks/market/high-low-stocks.aspx?catg=1&period=3&t=1&p='
High_3_year = 'http://www.aastocks.com/tc/stocks/market/high-low-stocks.aspx?catg=1&period=4&t=1&p='
All_time_high = 'http://www.aastocks.com/tc/stocks/market/high-low-stocks.aspx?catg=1&period=5&t=1&p='

#Low Stocks
Low_1_month = 'http://www.aastocks.com/tc/stocks/market/high-low-stocks.aspx?catg=2&period=1&t=1&p='
Low_3_month = 'http://www.aastocks.com/tc/stocks/market/high-low-stocks.aspx?catg=2&period=2&t=1&p='
Low_6_month = 'http://www.aastocks.com/tc/stocks/market/high-low-stocks.aspx?catg=2&period=6&t=1&p='
Low_52_week = 'http://www.aastocks.com/tc/stocks/market/high-low-stocks.aspx?catg=2&period=3&t=1&p='
Low_3_year = 'http://www.aastocks.com/tc/stocks/market/high-low-stocks.aspx?catg=2&period=4&t=1&p='
All_time_low = 'http://www.aastocks.com/tc/stocks/market/high-low-stocks.aspx?catg=2&period=5&t=1&p='


High_1_month_ = OverviewExractor(High_1_month)
High_3_month_ = OverviewExractor(High_3_month)
High_6_month_ = OverviewExractor(High_6_month)
High_52_week_ = OverviewExractor(High_52_week)
High_3_year_ = OverviewExractor(High_3_year)
All_time_high_ = OverviewExractor(All_time_high)

Low_1_month_ = OverviewExractor(Low_1_month)
Low_3_month_ = OverviewExractor(Low_3_month)
Low_6_month_ = OverviewExractor(Low_6_month)
Low_52_week_ = OverviewExractor(Low_52_week)
Low_3_year_ = OverviewExractor(Low_3_year)
All_time_low_ = OverviewExractor(All_time_low)

request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, 
                range="1-month High!A2", valueInputOption="USER_ENTERED", body={"values": High_1_month_}).execute()

request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, 
                range="3-month High Stocks!A2", valueInputOption="USER_ENTERED", body={"values": High_3_month_}).execute()
request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, 
                range="6-month High Stocks!A2", valueInputOption="USER_ENTERED", body={"values": High_6_month_}).execute()
request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, 
                range="52-week High Stocks!A2", valueInputOption="USER_ENTERED", body={"values": High_52_week_}).execute()
request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, 
                range="3-year High Stocks!A2", valueInputOption="USER_ENTERED", body={"values": High_3_year_}).execute()
request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, 
                range="All-time High Stocks!A2", valueInputOption="USER_ENTERED", body={"values": All_time_high_}).execute()

request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, 
                range="1-month Low Stocks!A2", valueInputOption="USER_ENTERED", body={"values": Low_1_month_}).execute()
request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, 
                range="3-month Low Stocks!A2", valueInputOption="USER_ENTERED", body={"values": Low_3_month_}).execute()
request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, 
                range="6-month Low Stocks!A2", valueInputOption="USER_ENTERED", body={"values": Low_6_month_}).execute()
request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, 
                range="52-week Low Stocks!A2", valueInputOption="USER_ENTERED", body={"values": Low_52_week_}).execute()
request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, 
                range="3-year Low Stocks!A2", valueInputOption="USER_ENTERED", body={"values": Low_3_year_}).execute()
request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, 
                range="All-time Low Stocks!A2", valueInputOption="USER_ENTERED", body={"values": All_time_low_}).execute()

print(request)
