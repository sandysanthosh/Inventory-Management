# Inventory-Management
Inventory Management

To store the data submitted from the HTML form into a local Excel file, you would typically need some server-side scripting, like Python with a web framework such as Flask or Django. Below is a simple example using Flask to handle the form submission and store the data in an Excel file named "inventory.xlsx":

```python
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
    inventory_df = inventory_df.append(new_data, ignore_index=True)

    # Write DataFrame to Excel file
    inventory_df.to_excel('inventory.xlsx', index=False)

    return 'Data submitted successfully!'

if __name__ == '__main__':
    app.run(debug=True)
```

You also need to create an HTML file named "inventory_form.html" with the form code provided in the previous response and place it in the same directory as your Python script.

Make sure you have Flask and pandas installed (`pip install flask pandas`) before running the script. This code will start a Flask web server that listens for form submissions, stores the data in an Excel file, and displays a success message.
