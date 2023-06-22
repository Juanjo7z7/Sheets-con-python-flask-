from gspread import authorize
from oauth2client.service_account import ServiceAccountCredentials

# Configurar las credenciales de autenticación
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('key.json', scope)
gc = authorize(credentials)

sh = gc.open_by_key('1ops_YJi190u0AzZEv4Hbb5DTaRByk35VYWm1G76KWd4')
worksheet = sh.worksheet('Hoja 2')

records = worksheet.get_all_records()

data=["Rust","Teclado"]
i=0

worksheet.append_row(data)


headers = list(records[0].keys())

print("\t".join(headers))

for record in records:
    values = "\t".join(str(value) for value in record.values())
    print(values)

