DaysA = set(["Mon", "Tue", "Wed"])
DaysB = set(["Wed","Thu","Fri","Sat","Sun"])
AllDays = DaysA.union(DaysB)
print("Union Operation", AllDays)

AllDays = DaysA.intersection(DaysB)
print("Intersection Operation", AllDays)

AllDays = DaysA.difference(DaysB)
print("Difference Operation", AllDays)


DaysA = set(["Mon", "Tue", "Wed"])
DaysB = set(["Mon", "Tue", "Wed","Thu","Fri","Sat","Sun"])


AllDays = DaysA.issubset(DaysB)
print("Is Subset Operation Operation", AllDays)

AllDays = DaysB.issuperset(DaysA)
print("Is Superset Operation", AllDays)
