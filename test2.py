from datetime import datetime
import requests
import gzip
import json 

# URL of the FastAPI endpoint on the AWS EC2 instance
url = "http://localhost:8000/get-recipe"  # test

# JSON data representing user preferences
preferences = {
    "metadata": {
        "cusine": "italian",
        "level": "beginner-friendly",
        "health_n_wellness": "low-carb",
    },
    "items": ["tomato", "potato", "milk"],
}

# Serialize the JSON data to a string
json_data = json.dumps(preferences)

# Compress the JSON data using gzip
compressed_data = gzip.compress(json_data.encode("utf-8"))



# Set the "Content-Encoding" header to specify gzip compression
headers = {"Content-Encoding": "gzip"}

t1 = datetime.now()
# Send the POST request with compressed data and headers
response = requests.post(url, data=compressed_data,headers=headers)

# Check the response
if response.status_code == 200:
    data = response.json()
    print("Response:", data["response"])
else:
    print("Error:", response.status_code, response.text)
t2 = datetime.now()
print(t2-t1)