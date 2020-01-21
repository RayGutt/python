from datetime import date

date_1 = date(2010, 10, 30)
date_2 = date(2016, 1, 20)

delta = date_2 - date_1

print(f"Difference in days : {delta.days}")

