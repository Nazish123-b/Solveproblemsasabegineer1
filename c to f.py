def f_to_c(f):
  return 5* (f-32)/9
f = int(input("Enter value in farenhite: "))
c = f_to_c(f)
print(f"{round(c,2)}°C")

#print("Temperature in Celsius:", f_to_c(f))