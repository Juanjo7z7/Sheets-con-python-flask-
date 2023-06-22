from flask import Flask, render_template, request
import gspread
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__)

@app.route('/create.html') 
def register(): 
    return render_template('create.html')

# Configurar las credenciales de autenticación
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('key.json', scope)
gc = gspread.authorize(credentials)

@app.route('/')
def show_records():
    # Abrir la hoja de cálculo
    sh = gc.open_by_key('1ops_YJi190u0AzZEv4Hbb5DTaRByk35VYWm1G76KWd4')
    worksheet = sh.worksheet("Hoja 2")
    # Obtener todos los registros de la hoja de cálculo
    records = worksheet.get_all_records()
    print(records)  # Verificar los registros en la consola
    return render_template('records.html', records=records)

@app.route('/Registro', methods=['GET', 'POST'])
def create_record():
    if request.method == 'POST':
        data = list(request.form.values())
        # Abrir la hoja de cálculo
        sh = gc.open_by_key('1ops_YJi190u0AzZEv4Hbb5DTaRByk35VYWm1G76KWd4')
        worksheet = sh.worksheet("Hoja 2")  
        worksheet.append_row(data)  
        return 'Registro creado exitosamente'
    return render_template('create.html')





#@app.route('/update/<int:record_id>', methods=['GET', 'POST'])
#def update_record(record_id):
#    # Obtener el registro por su ID
#    records = worksheet.get_all_records()
#    record = records[record_id - 1] if record_id <= len(records) else None
#    
#    if request.method == 'POST':
#        if record:
#            # Obtener los datos enviados desde el formulario
#            data = request.form.to_dict()
#            
#            # Actualizar los datos en la hoja de cálculo
#            for key, value in data.items():
#                record[key] = value
#            
#            # Actualizar la fila correspondiente en la hoja de cálculo--
#            cell_list = worksheet.range(record_id + 1, 1, record_id + 1, len(record))
#            for i, cell in enumerate(cell_list):
#                cell.value = record[list(record.keys())[i]]
#            
#            worksheet.update_cells(cell_list)
#        
#        return redirect(url_for('show_records'))
#    
#    return render_template('public/update.html', record=record, record_id=record_id)

#@app.route('/delete/<int:record_id>', methods=['POST'])
#def delete_record(record_id):
#    # Eliminar el registro por su ID
#    worksheet.delete_rows(record_id + 1)
#    
#    return redirect(url_for('show_records'))

if __name__ == '__main__':
    app.run(port=666, debug=True)
