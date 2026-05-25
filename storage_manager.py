import csv
import json

team_data = [
    {"ID": "1", "Name": "Yousef Botros", "Role": "Penetration Tester"},
    {"ID": "2", "Name": "Mohamed Ahmed", "Role": "Frontend Developer"},
    {"ID": "3", "Name": "Ramy Malak", "Role": "Backend Developer"},
    {"ID": "4", "Name": "Mina Keroulous", "Role": "Hardware Engineer"},
    {"ID": "5", "Name": "Ahmed Kamal", "Role": "Embedded Systems"}
]

csv_file = "team_data.csv"
fields = ["ID", "Name", "Role"]

print("Creating CSV file...")
with open(csv_file, "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=fields)
    writer.writeheader()
    writer.writerows(team_data)
print("CSV file created successfully.")

json_file = "team_data.json"

print("Creating JSON file...")
with open(json_file, "w", encoding="utf-8") as file:
    json.dump(team_data, file, indent=4)
print("JSON file created successfully.")

print("\nReading data back to verify:")
print("\n--- Reading CSV ---")
with open(csv_file, "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

print("\n--- Reading JSON ---")
with open(json_file, "r", encoding="utf-8") as file:
    data = json.load(file)
    print(json.dumps(data, indent=2))