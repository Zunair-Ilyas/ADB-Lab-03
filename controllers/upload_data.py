import os
from pathlib import Path
import pandas as pd
from pymongo import MongoClient, errors
from dotenv import load_dotenv

# Load environment variables from a .env file (optional)
load_dotenv()

# CSV file name relative to repository root (adjust if needed)
CSV_FILENAME = os.getenv('CRICKET_CSV', str(Path(__file__).resolve().parents[1] / 'Cricket.csv'))

# MongoDB connection string should be set in environment variable MONGO_URI
# Example .env entry: MONGO_URI="mongodb+srv://<user>:<pass>@cluster.mongodb.net/?retryWrites=true&w=majority"
MONGO_URI = os.getenv('MONGO_URI')
DB_NAME = os.getenv('DB_NAME', 'task_manager_db')
COLLECTION_NAME = os.getenv('COLLECTION_NAME', 'cricket')


def load_csv(path: str) -> pd.DataFrame:
    """Load CSV into a pandas DataFrame. Raises FileNotFoundError if not present."""
    csv_path = Path(path)
    if not csv_path.exists():
        raise FileNotFoundError(f"CSV file not found at: {csv_path}")

    # Try reading; allow pandas to infer encoding/engine
    df = pd.read_csv(csv_path)

    # If the CSV contains a header row that's actually metadata, drop the first row
    # This mirrors previous behavior but is safer (only drop if header-like)
    if df.shape[0] > 0 and all(isinstance(x, str) for x in df.columns):
        # Keep as-is. If you really want to drop a metadata row, uncomment next line:
        # df = df.iloc[1:]
        pass

    return df


def get_mongo_client(uri: str) -> MongoClient:
    if not uri:
        raise ValueError('MONGO_URI is not set. Please configure it in environment or .env file.')
    client = MongoClient(uri)
    # Ping to verify connection
    client.admin.command('ping')
    return client


def upload_dataframe_to_mongo(df: pd.DataFrame, client: MongoClient, db_name: str, collection_name: str):
    db = client[db_name]
    collection = db[collection_name]

    # Convert DataFrame to dictionary records
    list_of_dict = df.to_dict(orient='records')

    if not list_of_dict:
        print('No records to insert.')
        return

    try:
        result = collection.insert_many(list_of_dict, ordered=False)
        print(f'Inserted {len(result.inserted_ids)} documents into {db_name}.{collection_name}')
    except errors.BulkWriteError as bwe:
        # Some documents may have failed; report summary
        print('Bulk write error occurred while inserting documents:')
        print(bwe.details)
    except Exception as e:
        print(f'Unexpected error while inserting documents: {e}')


def main():
    try:
        print(f'Loading CSV from: {CSV_FILENAME}')
        df = load_csv(CSV_FILENAME)
        print('CSV loaded. Preview:')
        print(df.head().to_string())

        client = get_mongo_client(MONGO_URI)
        print('Successfully connected to MongoDB Atlas!')

        upload_dataframe_to_mongo(df, client, DB_NAME, COLLECTION_NAME)
    except Exception as e:
        print(f'Error: {e}')


if __name__ == '__main__':
    main()
