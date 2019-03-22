import requests
r = requests.get("http://vcm-9094.vm.duke.edu:5000/name")
print("Prints my name")
print(r.json())

r = requests.get("http://vcm-9094.vm.duke.edu:5000/hello/drward")
print("Prints Dr.Ward")
print(r.json())

j = {"a": [0, 0],
     "b": [1, 1]}
r = requests.post("http://vcm-9094.vm.duke.edu:5000/distance", json=j)
print("Points distance")
print(r.json())
