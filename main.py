from datetime import datetime, timedelta

tag_name = input("ENTER YOUR TAG NAME: ")

# print("Insert date day/month/year")


day = int(input("Input day: "))
month = int(input("Input month: "))
year = 2022
date = datetime(day=day, month=month, year=year)

due_date = date + timedelta(days=45)

print(f"DUE DATE IS: {due_date.day}/{due_date.month}/{due_date.year} -/{tag_name}")
