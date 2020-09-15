days = ["Mon", "Tue", "Wed", "Thu", "Fri"]

# loop가 실행되면 day 생성
for day in days:
  print(day)

# day가 Wed일 때, loop 중단
for day in days:
  if day == "Wed":
    break

  else:
    print(day)