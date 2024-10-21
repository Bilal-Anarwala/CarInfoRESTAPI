from flask import Flask, request
from flask_restful import Api, Resource
import sqlite3

app = Flask(__name__)
api = Api(app)

# Database setup
def car_db():
    conn = sqlite3.connect('cars.db')
    c = conn.cursor()
    
    # Create table if it doesn't exist
    c.execute('''CREATE TABLE IF NOT EXISTS cars
                 (url TEXT PRIMARY KEY, CarName TEXT, ModelYears TEXT, 
                  EngineVariants TEXT, TransmissionVariants TEXT, Drivetrain TEXT)''')
    
    # Pre-add the three cars
    cars_to_add = [
        {
            "url": "mk4supra",
            "CarName": "A80 Toyota Supra MK4",
            "ModelYears": "1993 - 2002",
            "EngineVariants": "2JZ-GTE or 2JZ-GE",
            "TransmissionVariants": "6-Speed Manual, 5-Speed Manual, 4-Speed Auto",
            "Drivetrain": "RWD"
        },
        {
            "url": "r32gtr",
            "CarName": "Nissan Skyline GT-R",
            "ModelYears": "1989 - 1994",
            "EngineVariants": "RB26-DETT",
            "TransmissionVariants": "5-Speed Manual",
            "Drivetrain": "Smart AWD(ATTESA)"
        },
        {
            "url": "rx7fd",
            "CarName": "Mazda RX-7 FD",
            "ModelYears": "1992 - 2002",
            "EngineVariants": "13B-REW",
            "TransmissionVariants": "5-Speed Manual, 4-Speed Automatic",
            "Drivetrain": "RWD"
        }
    ]
    
    # Add each car to the database
    for car in cars_to_add:
        c.execute('''INSERT OR REPLACE INTO cars 
                     (url, CarName, ModelYears, EngineVariants, TransmissionVariants, Drivetrain)
                     VALUES (:url, :CarName, :ModelYears, :EngineVariants, :TransmissionVariants, :Drivetrain)''', 
                     car)
    
    conn.commit()
    conn.close()

car_db()

class Car(Resource):
    def get(self, url):
        conn = sqlite3.connect('cars.db')
        c = conn.cursor()
        c.execute("SELECT * FROM cars WHERE url=?", (url,))
        row = c.fetchone()
        conn.close()

        if row:
            return {
                "CarName": row[1],
                "Model Years": row[2],
                "Engine Variants": row[3],
                "Transmission Variants": row[4],
                "Drivetrain": row[5]
            }
        return {"message": "Car not found"}, 404

    def put(self, url):
        conn = sqlite3.connect('cars.db')
        c = conn.cursor()
        
        # Check if URL already exists
        c.execute("SELECT * FROM cars WHERE url=?", (url,))
        if c.fetchone():
            conn.close()
            return {"message": "URL already in use. Please try a different URL."}, 400

        data = request.json
        required_fields = ["CarName", "Model Years", "Engine Variants", "Transmission Variants", "Drivetrain"]
        
        if not all(field in data for field in required_fields):
            conn.close()
            return {"message": "Missing required fields"}, 400

        c.execute('''INSERT INTO cars (url, CarName, ModelYears, EngineVariants, TransmissionVariants, Drivetrain)
                     VALUES (?, ?, ?, ?, ?, ?)''',
                  (url, data["CarName"], data["Model Years"], data["Engine Variants"],
                   data["Transmission Variants"], data["Drivetrain"]))
        conn.commit()
        conn.close()
        return {"message": "Car data added successfully"}, 201

    def delete(self, url):
        conn = sqlite3.connect('cars.db')
        c = conn.cursor()
        c.execute("DELETE FROM cars WHERE url=?", (url,))
        if c.rowcount > 0:
            conn.commit()
            conn.close()
            return {"message": "Car data deleted successfully"}, 200
        conn.close()
        return {"message": "Car not found"}, 404

api.add_resource(Car, "/<string:url>")

if __name__ == "__main__":
    app.run(debug=True)