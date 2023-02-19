import json
indian_state = {
   "Andhra Pradesh": "Amaravati",
    "Bihar": "Patna",
    "Gujarat": "Gandhinagar",
    "Karnataka": "Bengaluru",
    "Maharashtra": "Mumbai",
    "Tamil Nadu": "Chennai",
    "Uttar Pradesh": "Lucknow"
}

with open("indian_state.json", "w") as f:
     json.dump(indian_state,f)
print(indian_state)
