import pygsheets
import pandas as pd
#authorization
gc = pygsheets.authorize(service_file='/Users/drmom/Dropbox/Dev/Python Programs/Google Sheets/creds.json')

# Create empty dataframe
# df = pd.DataFrame()

# Create a column
# df['CLASS'] = ['Freshmen', 'Sophomores', 'Juniors', 'Seniors']
# df['VOTES'] = [20,30,40,50]

#open the google spreadsheet (where 'PY to Gsheet Test' is the name of my sheet)
sh = gc.open('Python-Test-Sheet')

#select the first sheet 
wks = sh[0]

#votes_drange = wks.get_named_range('VOTES')

sheet_df = wks.get_as_df(has_header=True, index_column=1,  end='B5')

print(sheet_df)
sheet_df.loc['Freshmen', 'VOTES'] += 1
print(sheet_df)

#update the first sheet with df, starting at cell B2. 
wks.set_dataframe(sheet_df,(1,2))
