#Task 1 — Build a JSON Structure
import json

user_profile = {
    "name": "Raju",
    "age": 30,
    "email": "raju.kpr2@gmail.com",
    "is_active": True,
    "skills": ["Python", "SQL", "ETL","AI/ML","Azure"]
}

json_data = json.dumps(user_profile, indent=4)

print(json_data)


#Task 2 — Parse an API Response

api_response = '{"status": "success", "data": {"user_id": 101, "username": "alex99", "score": 87.5}}'

data = json.loads(api_response)

username = data["data"]["username"]
score = data["data"]["score"]

print("Username:", username)
print("Score:", score)
print(f"User {username} scored {score} points")



#Task 3 — Handle Nested JSON

user = {
    "name": "Priya",
    "address": {
        "city": "Bengaluru",
        "state": "Karnataka",
        "zip": "560001"
    }
}

city = user["address"]["city"]
zip_code = user["address"]["zip"]

print("City:", city)
print("Zip Code:", zip_code)

# Add new key
user["address"]["country"] = "India"

print(json.dumps(user, indent=4))