import xlrd , xlwt
from sys import argv
# 
filename, group, current_week , today = argv

readbook = xlrd.open_workbook("ras.xlsx")

sheet = readbook.sheet_by_index(0)

week = [] # расписание на всю неделю
#сканирование расписания , нахождение столбца группы , вытаскивание столбца группы
for i in range(sheet.ncols):
    data = sheet.cell_value(1,i)
    if data == group:
        for j in range(3,77):
            week.append(sheet.cell_value(j,i))
# из расписания недели вытаскиеваем расписание конкретного дня.

day = week[12*(int(today)-1):(12*int(today))] # расписание дня

# вводим дни согласно с четностью недели ( от 0 до 5)
print(f"сейчас {current_week} неделя\nРасписание на сегодня: " )
# звполнение недочетов расписания
if (int(today) == 6) and (int(current_week)%2 == 0):
    print("""1) День
2) самостоятельных
3) занятий
4)
5)
6)""")
# вводим расписание, ориентируясь на четность
else:
    for step in range(6):
        print(f"{step+1}) {day[int(current_week)%2+step*2]}")