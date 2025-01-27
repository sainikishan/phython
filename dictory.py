dict={
    "name" :"kishan",
    "cgpa":6.0,
    "marks":[90,97,87],
}
print(dict)
info={
    "name" :"kishan",
    "cgpa":6.0,
    "marks":[90,97,87],
    "address":"kanpur",
    "age":27,
    "mobile":7905057839
}
print(info)
print(info["name"])
# nested dictionary
student={
    "name":"kishan",
    "subject":{
        "maths":90,
        "science":97,
        "english":87,  
    },
}
print(student.keys)
print(len(student))
print(list(student.keys()))
# values
print(student.values())
print(list(student.values()))
# items
print(student.items())
print(list(student.items()))