import boto3
import csv

# Configure AWS credentials and region (if necessary)
# boto3.setup_default_session(profile_name='your_profile_name')  # Uncomment if using profiles
# dynamodb = boto3.resource('dynamodb', region_name='us-east-1')  # Uncomment if using a specific region

def upload_csv(table_name, csv_filepath):
  """
  Uploads data from a CSV file to a DynamoDB table.

  Args:
    table_name (str): Name of the DynamoDB table.
    csv_filepath (str): Path to the CSV file.
  """
  dynamodb = boto3.resource('dynamodb')
  table = dynamodb.Table(table_name)

  with open(csv_filepath, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
      table.put_item(Item=row)

  print(f"Uploaded data from {csv_filepath} to table {table_name}")

def clear_data(table_name):
  dynamodb = boto3.resource('dynamodb')
  table = dynamodb.Table(table_name)

if __name__ == "__main__":
  table_name = "lego-releases-data"
  csv_filepath = "lego.csv"
  upload_csv(table_name, csv_filepath)

