# Set up

## Install dependencies

### python

`cd backend`

`pip install -r requirements.txt`
`pip install greenlet`
`pip install mysqlclient`

### Angular

`npm install`


### Prepare the database

Run the local mysql service on your machine. Update the connection string in the backend/config.py file.

Copy paste the database/table_creation into the mysql console. (This step is only needed once)

### Prepare the Google Calendar

Go to the GCP Console and create a new user secret credential file for your gmail address.

Copy paste the content into the file backend/client_secret_GoogleCloudDemo.json


# Run the code

## python

`cd backend`

`python main.py`

## Angular

`npm run start`

# Access the Web App

Navigate to http://localhost:4200