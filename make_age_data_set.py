import csv
import datetime as dt

def age(year, month, day):
    ToDay = dt.date.today()
    birthday = dt.date(year, month, day)
    return (int(ToDay.strftime("%Y%m%d")) - int(birthday.strftime("%Y%m%d"))) // 10000

member = []
i = 0
with open('Book1.csv', 'r') as f:
    reader = csv.reader(f)
    for line in reader:
        member.append(line)

all_age = []
all_name = []
for i in range(len(member)):
    try:
        one_age = age(int(member[i][1]), int(member[i][2]), int(member[i][3]))
        all_age.append(one_age)
        all_name.append(member[i][0])
        
    except ValueError as e:
        pass

all_data = []

for j in range(len(all_age)):
    data = []
    data.append(all_name[j])
    data.append(all_age[j])
    all_data.append(data)

sorted_all_data = sorted(all_data, key=lambda x: x[1])

for k in range(len(all_age)):
    sorted_all_data[k].insert(0, (k+1))

header = ["番号", "名前", "年齢"]
total = len(all_name)
totaldata = '計' + str(total) + '名'
header.append(totaldata)
ToDay = dt.date.today()
DayData = ToDay.strftime('%Y/%m/%d') + '現在'
header.append(DayData)

with open("sorted_age.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(sorted_all_data)

f.close()
