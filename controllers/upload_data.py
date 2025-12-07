import pandas as pd
import io

# Replace 'your_spreadsheet.csv' with the actual name of your uploaded file
file_name = 'Ananth_Test_DB_Tests.xlsx - Tests (1).csv'

try:
    df = pd.read_csv('../Cricket.csv')
    print("Spreadsheet successfully loaded!")
    display(df.head())
except KeyError:
    print(f"Error: File '{file_name}' not found. Please ensure you uploaded the correct file name.")
except Exception as e:
    print(f"An error occurred while loading the spreadsheet: {e}")
    print("Please ensure the file is a valid CSV and the name is correct.")

# Remove the first row
df = df.iloc[1:]

print("First row removed. Displaying the new head of the DataFrame:")
display(df.head())

from pymongo import MongoClient

# Replace the placeholder with your actual MongoDB Atlas connection string
# Example: 'mongodb+srv://<username>:<password>@<cluster-name>.<xxxxxx>.mongodb.net/?retryWrites=true&w=majority'
mongo_uri = 'mongodb+srv://Zunair:wE1ijCgy4unmamsX@task-manager.hendyep.mongodb.net/?retryWrites=true&w=majority&appName=Task-Manager'

try:
    client = MongoClient(mongo_uri)
    # The ping command is cheap and does not require auth. It will confirm that the connection is working.
    client.admin.command('ping')
    print("Successfully connected to MongoDB Atlas!")
    # You can now access your databases and collections, for example:
    # db = client['your_database_name']
    # collection = db['your_collection_name']
    # print(f"Connected to database: {db.name}")
except Exception as e:
    print(f"Could not connect to MongoDB Atlas: {e}")

list_of_dict = df.to_dict(orient='records')

collection = db.create_collection('cricket')

collection.insert_many(list_of_dict)