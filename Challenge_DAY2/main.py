days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

def is_on_list(days, day):
  if day in days:
    return True
  else:
    return False

def get_x(days, index):
  return days[index]

def add_x(days, day):
  days.append(day)

def remove_x(days, day):
  days.remove(day)

print("Is Wed on 'days' list?", is_on_list(days, "Wed"))

print("The fourth item in 'days' is:", get_x(days, 3))

add_x(days, "Sat")
print(days)

remove_x(days, "Mon")
print(days)