from collections import Counter
import csv
with open("HeigthWeight.csv",newline="") as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)
#print(file_data)
new_data = []
for i in range(len(file_data)):
    n_num = file_data[i][2]
    new_data.append(float(n_num))

data = Counter(new_data)
#print(data)
mode_data_for_range = {"85-95":0,"95-105":0,"105-115":0,"115-125":0,"125-135":0,"135-145":0,}

for height,occurence in data.items():
    if 85<float(height)<95 :
        mode_data_for_range["85-95"]+=occurence
    elif 95<float(height)<105 :
        mode_data_for_range["95-105"]+=occurence
    elif 105<float(height)<115 :
        mode_data_for_range["105-115"]+=occurence
    elif 115<float(height)<125 :
        mode_data_for_range["115-125"]+=occurence
    elif 125<float(height)<135 :
        mode_data_for_range["125-135"]+=occurence
    elif 135<float(height)<145 :
        mode_data_for_range["135-145"]+=occurence

mode_range,mode_occurence = 0,0
for range,occurence in mode_data_for_range.items():
    if occurence>mode_occurence:
        mode_range,mode_occurence = [int(range.split("-")[0]),int(range.split("-")[1])],occurence

mode = float((mode_range[0]+mode_range[1])/2)
print(f"mode is -> {mode:2f}")