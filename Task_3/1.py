
# 1.changing the key from city to location 
skillsanta_Dict ={"name": "Sachin", "age": 22, "salary": 60000, "city": "New Delhi"}
print("Before:",skillsanta_Dict)
x=skillsanta_Dict.pop("city")
skillsanta_Dict["location"]=x
print("after:",skillsanta_Dict)