"""
- buat summary caption video bar race
- Bar Race
- Cari masa2 krisis dalam 10 tahun terkahir
- Find growth YOY di masa2 krisis
- Temukan company paling baik dlm revenue in time of crisis
- compare jumlah properti dan efesiensi dalam menghasilkan revenue
- important event of company in last 10 years
"""



import requests
from bs4 import BeautifulSoup
import pandas as pd

company = ['Wyndham Hotel & Resorts, Inc', 'Marriott International, Inc', 'Choice Hotels International, Inc', 'Hilton Worldwide Holdings, Inc', 'InterContinental Hotels Group', 'Red Lion Hotels Corporation', 'Hyatt Hotels Corporation']


def get_data(url, num1, num2):
    raw_html_page = requests.get(url).content
    soup = BeautifulSoup(raw_html_page, 'html.parser')
    table_data = soup.find_all("td")

    quarter_series = []
    revenue = []

    for i in range(num1, num2):
        #print(table_data[i], '\n', type(table_data[i]))
        #print(table_data[i].get_text())
        if len(table_data[i].get_text()) > 8 :
            quarter_series.append(table_data[i].get_text())
        elif '$' in table_data[i].get_text():
            if ',' in table_data[i].get_text():
                a = table_data[i].get_text().replace(',', '')
                revenue.append(int(a.strip('$')))
            elif table_data[i].get_text() == None:
                print(1)
                revenue.append(0)    
            else:    
                revenue.append(int(table_data[i].get_text().strip('$')))
        #print(quarter_series, '\n', revenue)
    quarter_series.reverse()
    revenue.reverse()
    #print(len(quarter_series), len(revenue), 1)
    result = [quarter_series, revenue]
    return result

Wyndham_Hotel = get_data('https://www.macrotrends.net/stocks/charts/WH/wyndham-hotels-resorts/revenue', 12, 44)
#print(Wyndham_Hotel)

Marriott_Hotel = get_data('https://www.macrotrends.net/stocks/charts/MAR/marriott/revenue', 30, 116)
#print(Marriott_Hotel)

Choice_Hotel = get_data('https://www.macrotrends.net/stocks/charts/CHH/choice-hotels/revenue', 30, 116)
#print(Choice_Hotel)

Hilton_Hotel = get_data('https://www.macrotrends.net/stocks/charts/HLT/hilton-worldwide-holdings/revenue', 24, 86)
#print(Hilton_Hotel)

Intercon_Hotel = get_data('https://www.macrotrends.net/stocks/charts/IHG/intercontinental-hotels-group/revenue', 30, 82)
for i in range(14):
    Intercon_Hotel[1].append(0)
#print(Intercon_Hotel)


Red_Lion_Hotel = get_data('https://www.macrotrends.net/stocks/charts/RLH/red-lion-hotels/revenue', 30, 116)
# print(Red_Lion_Hotel)

Hyat_Hotel = get_data('https://www.macrotrends.net/stocks/charts/H/hyatt-hotels/revenue', 28, 114)
#print(Hyat_Hotel)

df = {'Hotel Brand': company}

for date in Hyat_Hotel[0]:
    df[date] = [] 
#print(df)

#input for wyndham hotel
for i in range(len(Wyndham_Hotel[0])):
    if Wyndham_Hotel[0][i] in df:
        df[Wyndham_Hotel[0][i]].append(Wyndham_Hotel[1][i])
for i in df:
    if df[i] == []:
        df[i].append(0)  

#input for marriott
for i in range(len(Marriott_Hotel[0])):
    if Marriott_Hotel[0][i] in df:
        df[Marriott_Hotel[0][i]].append(Marriott_Hotel[1][i])

#input for choice hotel
for i in range(len(Choice_Hotel[0])):
    if Choice_Hotel[0][i] in df:
        df[Choice_Hotel[0][i]].append(Choice_Hotel[1][i])
for i in df:
    if len(df[i]) != 3 and i not in 'Hotel Brand':
        df[i].append(0)  

#input for Hilton
for i in range(len(Hilton_Hotel[0])):
    if Hilton_Hotel[0][i] in df:
        df[Hilton_Hotel[0][i]].append(Hilton_Hotel[1][i])
for i in df:
    if len(df[i]) != 4 and i not in 'Hotel Brand':
        df[i].append(0)  

#input for intercon
for i in range(len(Intercon_Hotel[0])):
    if Intercon_Hotel[0][i] in df:
        df[Intercon_Hotel[0][i]].append(Intercon_Hotel[1][i])
for i in df:
    if len(df[i]) != 5 and i not in 'Hotel Brand':
        df[i].append(0)  

#input for red lion
for i in range(len(Red_Lion_Hotel[0])):
    if Red_Lion_Hotel[0][i] in df:
        df[Red_Lion_Hotel[0][i]].append(Red_Lion_Hotel[1][i])
for i in df:
    if len(df[i]) != 6 and i not in 'Hotel Brand':
        df[i].append(0)       

#input for hyat
for i in range(len(Hyat_Hotel[0])):
    if Hyat_Hotel[0][i] in df:
        df[Hyat_Hotel[0][i]].append(Hyat_Hotel[1][i])
for i in df:
    if len(df[i]) != 7 and i not in 'Hotel Brand':
        df[i].append(0) 

data_frame = pd.DataFrame.from_dict(df)
print(data_frame) 

with open('hotel.csv', 'w') as hotel_csv:
    data_frame.to_csv(path_or_buf=hotel_csv)