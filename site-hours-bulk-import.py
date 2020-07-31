import pandas as pd, xlrd, json
from itertools import count

# input_default_mode = str(input("Confirm: run default mode (upload template named \"HoursChange_BulkUpload\" and script are in the same folder, Y / N)? "))
# if input_default_mode.lower() == "n":
#     input_new = input("Enter the full path to the Excel upload template, including the filename with \".xlsx\" (no quotation marks): ")
#     excel_file = input_new
# else:
excel_file = 'HoursChanges_BulkUpload.xlsx'

# excel_file = r'C:/Users/sg185393/Potbelly/HoursChanges_BulkUpload.xlsx' # set the path to the upload template (when in the right folder, right-click and copy the filepath)
hours_sheet = 0 # set the sheet number with the hours on it, left to right counting from 0
AO_Site_ID = 0 # set the column number with the AO Site IDs in it, counting from 0
import_items = pd.read_excel(excel_file, sheet_name=hours_sheet, usecols="C:AS", index_col=AO_Site_ID)
df = pd.DataFrame(data=import_items)

sites = { "Sites": [] } # this creates the container for all the sites
days = [ "SUNDAY", "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY"] # simple list for changing the day of the week dynamically

for i, site in enumerate(import_items):
    if i < len(import_items.index):
        sites['Sites'].append( { "SiteID": int(import_items.index.values[i]), "StoreHours": [], "DeliveryHours": [] }) # creates a single site and puts it in Sites container
        for j, day in zip(count(step=6), days): # loops thru the site's store hours for each day of week and adds it to a single site
            sites['Sites'][i]['StoreHours'].append( {"DayOfWeek": day, "IsClosed": str(df.iloc[i,j+2]), "OpeningTime": str(df.iloc[i,j]), "ClosingTime": str(df.iloc[i,j+1]) } ) # site hours
            sites['Sites'][i]['DeliveryHours'].append( {"DayOfWeek": day, "IsClosed": str(df.iloc[i,j+5]), "Delivery1Start": str(df.iloc[i,j+3]), "Delivery1End": str(df.iloc[i,j+4]) } ) # delivery hours

with open("JSON-call.txt", "w") as file: # creates & writes the JSON call to a text file
    file.write(json.dumps(sites, indent=4))

"""
# DEBUGGING TOOLS

# columns
columns= ['AO Site ID',
    'Sun Open','Sun Close','IsClosed','Sun Open','Sun Close','IsClosedForDelivery',
    'Mon Open','Mon Close','IsClosed','Mon Open','Mon Close','IsClosedForDelivery',
    'Tues Open','Tues Close','IsClosed','Tues Open','Tues Close','IsClosedForDelivery',
    'Wed Open','Wed Close','IsClosed','Wed Open','Wed Close','IsClosedForDelivery',
    'Thurs Open','Thurs Close','IsClosed','Thurs Open','Thurs Close','IsClosedForDelivery',
    'Fri Open','Fri Close','IsClosed','Fri Open','Fri Close','IsClosedForDelivery',
    'Sat Open','Sat Close','IsClosed','Sat Open','Sat Close','IsClosedForDelivery'])

# single site, single day call
sites['Sites'].append( { "SiteID": int(import_items.index.values[0]), "StoreHours": [], "DeliveryHours": [] })
sites['Sites'][0]['StoreHours'].append( {"DayOfWeek": "SUNDAY", "IsClosed": "false", "OpeningTime": str(df.iloc[0,1]), "ClosingTime": str(df.iloc[0,2]) } )
sites['Sites'][0]['DeliveryHours'].append( {"DayOfWeek": "SUNDAY", "IsClosed": "false", "Delivery1Start": str(df.iloc[0,1]), "Delivery1End": str(df.iloc[0,2]) } )

# prints the JSON formatting of python object(s)
print(json.dumps(sites, indent=4))

# full-length prtotoype JSON call, for comparison
{
    "Sites": [
        {
            "SiteId": "{{SiteId}}",
            "StoreHours": [
            	{
            		"DayOfWeek": "SUNDAY",
                    "IsClosed": "false",
                    "OpeningTime": "00:00:00",
                    "ClosingTime": "00:00:00",
            	},
            	{
            		"DayOfWeek": "MONDAY",
                    "IsClosed": "false",
                    "OpeningTime": "00:00:00",
                    "ClosingTime": "00:00:00",
            	},
            	{
            		"DayOfWeek": "TUESDAY",
                    "IsClosed": "false",
                    "OpeningTime": "00:00:00",
                    "ClosingTime": "00:00:00",
            	},
            	{
            		"DayOfWeek": "WEDNESDAY",
                    "IsClosed": "false",
                    "OpeningTime": "00:00:00",
                    "ClosingTime": "00:00:00",
            	},
            	{
            		"DayOfWeek": "THURSDAY",
                    "IsClosed": "false",
                    "OpeningTime": "00:00:00",
                    "ClosingTime": "00:00:00",
            	},
            	{
            		"DayOfWeek": "FRIDAY",
                    "IsClosed": "false",
                    "OpeningTime": "00:00:00",
                    "ClosingTime": "00:00:00",
            	},
            	{
            		"DayOfWeek": "SATURDAY",
                    "IsClosed": "false",
                    "OpeningTime": "00:00:00",
                    "ClosingTime": "00:00:00",
            	}
            ],
            "DeliveryHours": [
                {
                    "DayOfWeek": "SUNDAY",
                    "IsDeliveryClosed": "false",
                    "Delivery1Start": "01:23:45",
                    "Delivery1End": "06:07:08",
                    "Delivery2Start": "02:34:56",
                    "Delivery2End": "07:08:09"
                },
                {
                    "DayOfWeek": "MONDAY",
                    "IsDeliveryClosed": "false",
                    "Delivery1Start": "01:23:45",
                    "Delivery1End": "06:07:08",
                    "Delivery2Start": "02:34:56",
                    "Delivery2End": "07:08:09"
                },
                {
                    "DayOfWeek": "TUESDAY",
                    "IsDeliveryClosed": "false",
                    "Delivery1Start": "01:23:45",
                    "Delivery1End": "06:07:08",
                    "Delivery2Start": "02:34:56",
                    "Delivery2End": "07:08:09"
                },
                {
                    "DayOfWeek": "WEDNESDAY",
                    "IsDeliveryClosed": "false",
                    "Delivery1Start": "01:23:45",
                    "Delivery1End": "06:07:08",
                    "Delivery2Start": "02:34:56",
                    "Delivery2End": "07:08:09"
                },
                {
                    "DayOfWeek": "THURSDAY",
                    "IsDeliveryClosed": "false",
                    "Delivery1Start": "01:23:45",
                    "Delivery1End": "06:07:08",
                    "Delivery2Start": "02:34:56",
                    "Delivery2End": "07:08:09"
                },
                {
                    "DayOfWeek": "FRIDAY",
                    "IsDeliveryClosed": "false",
                    "Delivery1Start": "01:23:45",
                    "Delivery1End": "06:07:08",
                    "Delivery2Start": "02:34:56",
                    "Delivery2End": "07:08:09"
                },
                {
                    "DayOfWeek": "SATURDAY",
                    "IsDeliveryClosed": "false",
                    "Delivery1Start": "01:23:45",
                    "Delivery1End": "06:07:08",
                    "Delivery2Start": "02:34:56",
                    "Delivery2End": "07:08:09"
                }
            ]
        }
    ]
}
"""