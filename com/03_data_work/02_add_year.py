# year.txt를 읽어와서 map으로 만든다.
file = open("./year.txt")
lines = file.readlines()

headerYear = {}
for line in lines:
    line = line.split(",")
    key = line[0]
    year = line[1].replace("\n", "")
    headerYear[key] = year
print(headerYear)

# c_nt.fas에 year추가
# line을 돌다가 map의 key에 값이 존재하면 옆에 ,year를 찍음




