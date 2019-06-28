import csv

txtInput = "saya pergi ke pasar dengan ayah saya tadi malam"
data = txtInput.split()
indo = []
ngapak = []
translate = []
strResult = ""

with open('datalang.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        indo.append(row[0])
        ngapak.append(row[1])

for a in data:
    stat = False
    for i, x in enumerate(indo):
        if a == x:
            translate.append(ngapak[i])
            stat = True
    if stat != True:
        translate.append(a)

for j, b in enumerate(translate):
    strResult += translate[j] + " "

print("Indo:")
print(txtInput)
print("Ngapak:")
print(strResult)
