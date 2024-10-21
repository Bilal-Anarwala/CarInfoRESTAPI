# CarInfoRESTAPI

This project creates a simple REST API for managing information about JDM (Japanese Domestic Market) cars. It's built using Flask, Flask-RESTful, and SQLite, providing a straightforward way to interact with car data. It combines my interest for coding and my passion for cars. 

## Features

- Store and retrieve information about JDM cars using the built in Python SQLite database
- Get information about pre-defined JDM cars (Toyota Supra MK4, Nissan Skyline GT-R R32, Mazda RX-7 FD)
- Add new car data with custom URLs
- Retrieve car data by URL
- Delete car data by URL

## API Endpoints

- `/mk4supra` - GET: Retrieve information about the A80 Toyota Supra MK4 (pre-loaded)
- `/r32gtr` - GET: Retrieve information about the Nissan Skyline GT-R R32 (pre-loaded)
- `/rx7fd` - GET: Retrieve information about the Mazda RX-7 FD (pre-loaded)
  
- `/<string:url>` - GET: Retrieve car data by custom URL
- `/<string:url>` - PUT: Add new car data with a custom URL
- `/<string:url>` - DELETE: Delete car data by URL

## Usage

1. Install the required dependencies:
   ```
   pip install flask
   pip install flask_restful
   ```
2. Run the application:
   ```
   python API.py
   ```
   If you are on a Mac try running it like this:
   ```
   python3 API.py
   ```
3. Once running, the API will be available at `http://localhost:5000`

## Adding New Car Data

To add new car data, send a PUT request to `/<string:url>` with the following JSON structure:

```json
{
  "CarName": "Car Name",
  "Model Years": "Year Range",
  "Engine Variants": "Engine Types",
  "Transmission Variants": "Transmission Types",
  "Drivetrain": "Drivetrain Type"
}
```
A sample PUT command on the terminal will look like this:

```bash
curl -X PUT -H "Content-Type: application/json" -d '{
  "CarName": "Nissan 350Z",
  "Model Years": "2002-2009",
  "Engine Variants": "VQ35DE, VQ35HR",
  "Transmission Variants": "6-Speed Manual, 5-Speed Automatic",
  "Drivetrain": "RWD"
}' http://127.0.0.1:5000/350z
```

## Viewing Car Data

To view car data, execute a curl command for the car you are looking for. A sample command and output will look like the following:

```
curl http://127.0.0.1:5000/rx7fd
{
    "CarName": "Mazda RX-7 FD",
    "Model Years": "1992 - 2002",
    "Engine Variants": "13B-REW",
    "Transmission Variants": "5-Speed Manual, 4-Speed Automatic",
    "Drivetrain": "RWD"
}
```
You can also browse to URL of the car on your browser to view the data as well.

## Deleting Car Data

To delete existing car data, send a DELETE request to the URL of the car:

```bash
curl -X DELETE http://127.0.0.1:5000/350z
```

Note: The pre-loaded cars (mk4supra, r32gtr, rx7fd) will be re-added automatically when the application restarts, even if deleted.

## Database

The application uses a SQLite database named `cars.db` to store the car information. This file is created automatically when you run the application for the first time, and it's pre-loaded with 3 JDM cars to start.

## Learning Outcomes

This project serves as an introduction to creating and using REST APIs with persistent storage. It demonstrates my ability to:

- Create a simple API using Flask
- Define API resources and endpoints
- Handle different HTTP methods (GET, PUT, DELETE)
- Implement basic error handling in API responses
- Implement a SQLite database for data persistence
