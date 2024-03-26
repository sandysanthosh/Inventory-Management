from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('inventory_form.html')

@app.route('/submit_inventory', methods=['POST'])
def submit_inventory():
    material = request.form['material']
    date = request.form['date']
    timein = request.form['timein']
    timeout = request.form['timeout']
    location = request.form['location']
    personal_name = request.form['personal_name']
    brand = request.form['brand']
    client_details = request.form['client_details']

    # Create or load the Excel file
    try:
        inventory_df = pd.read_excel('inventory.xlsx')
    except FileNotFoundError:
        inventory_df = pd.DataFrame(columns=['Material', 'Date', 'Time In', 'Time Out', 'Location', 'Personal Name', 'Brand', 'Client Details Received'])

    # Append new data to the DataFrame
    new_data = pd.DataFrame([[material, date, timein, timeout, location, personal_name, brand, client_details]],
                            columns=['Material', 'Date', 'Time In', 'Time Out', 'Location', 'Personal Name', 'Brand', 'Client Details Received'])
    inventory_df = inventory_df._append(new_data, ignore_index=True)

    # Write DataFrame to Excel file
    inventory_df.to_excel('inventory.xlsx', index=False)

    return 'Data submitted successfully!'

if __name__ == '__main__':
    app.run(debug=True)
