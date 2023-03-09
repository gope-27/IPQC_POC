

from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# Load data from CSV file
df = pd.read_csv('Final_IPQC_POC.csv')


# Define a route for the home page
@app.route('/')
def index():
    # Get unique values of K55 CNC column
    k55_cnc_values = df['K55 CNC'].unique()
    # Render the home page template and pass the data and unique values as parameters
    return render_template('index.html', data=df.to_dict('records'), k55_cnc_values=k55_cnc_values)


# Run the application
if __name__ == '__main__':
    app.run(debug=True)
