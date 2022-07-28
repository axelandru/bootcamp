a = 1
print(f"NAME from module_1.py: {__name__}")
print(f"FILE from module_1.py: {__file__}")
print(f"module_1 -- a = {a}")

b = 2
c = 3



#1
print(merge(f1_teams,f1_more_teams))

#2
for  driver,team in f1_teams.items():
    if team == 'McLaren':
        print(driver)

#3
print(dict(zip(f1_drivers_numbers, f1_teams.item())))