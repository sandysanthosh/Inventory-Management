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


Here's the HTML code for the inventory form:

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Inventory Form</title>
</head>
<body>

<h2>Inventory Form</h2>

<form action="/submit_inventory" method="post">
  <label for="material">Material:</label><br>
  <input type="text" id="material" name="material"><br>
  
  <label for="date">Date:</label><br>
  <input type="date" id="date" name="date"><br>
  
  <label for="timein">Time In:</label><br>
  <input type="time" id="timein" name="timein"><br>
  
  <label for="timeout">Time Out:</label><br>
  <input type="time" id="timeout" name="timeout"><br>
  
  <label for="location">Location:</label><br>
  <input type="text" id="location" name="location"><br>
  
  <label for="personal_name">Personal Name:</label><br>
  <input type="text" id="personal_name" name="personal_name"><br>
  
  <label for="brand">Brand:</label><br>
  <input type="text" id="brand" name="brand"><br>
  
  <label for="client_details">Client Details Received:</label><br>
  <input type="text" id="client_details" name="client_details"><br><br>
  
  <input type="submit" value="Submit">
</form> 

</body>
</html>
```

You can save this code in a file named "inventory_form.html". When the form is submitted, it sends a POST request to the "/submit_inventory" route of your Flask application, which is responsible for processing the form data and storing it in the Excel file.
