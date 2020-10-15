def age_check(age):
  print(f"you are {age}")

  if age < 18:
    print("You can't drink")
  
  # 두 조건이 모두 true가 아니여도 실행
  elif age == 18 or age == 19:
    print("You are new to this")
  
  # 두 조건이 모두 true 여야 실행
  elif age > 20 and age < 25:
    print("You are still kind of young")
  else:
    print("enjoy your drink")

age_check(18)
age_check(23)
age_check(19)