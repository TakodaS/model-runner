import sys,os,json

print("The script under /pyross/scripts/run-pyross will be run automatically by the docker image. Implement pyross model here. \n")
print(" inputted arguments were: " + str(sys.argv), "\n")



with open('/data/input/inputFile.json') as json_file: 
    data = json.load(json_file)

print("The input data will have a similar structure to /data/input/inputFile.json printed below: \n")
print(data)