# from js import document
from datetime import datetime, timedelta

#
#
# def run(*ags, **kws):
#     tag_name = document.getElementById('tag_name').value;
#     day = document.getElementById('day').value;
#     month = document.getElementById('month').value;
#     year = document.getElementById('year').value;
#
#     date = datetime.date(day=int(day), month=int(month), year=int(year))
#
#     new_date = date + datetime.timedelta(day + 45)
#     due_date = f'{due_date.day}/{due_date.month}/{due_date.year} -/{tag_name}'
#
#     pyscript.write("due_date", due_date)

tag_name = input("ENTER YOUR TAG NAME: ")


# print("Insert date day/month/year")


day = int(input("Input day: "))
month = int(input("Input month: "))
year = 2022
date = datetime(day=day, month=month, year=year)

due_date = date + timedelta(days=45)

print(f"DUE DATE IS: {due_date.day}/{due_date.month}/{due_date.year} -/{tag_name}")

# def date(day, month, year):
#     date_day = datetime.date(day=int(day))
#     month = datetime.date(month=int(month))
#     year = datetime.datetime(year=int(year))
#     return datetime.date


# def count_date(value):
#     value = datetime.timedelta(value)
#     return f'{value}'
