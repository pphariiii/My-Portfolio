print("⏔⏔⏔ ꒰ ᧔ Calculator ᧓ ꒱ ⏔⏔⏔")
n1 = float(input("Insert a number : "))
sym = input("Choose a symbol (+, -, *, /) : ")
n2 = float(input("Insert a number : "))
if sym == "+" :
  result = n1+n2
elif sym == "-" :
  result = n1-n2
elif sym == "*" :
  result = n1*n2
elif sym == "/" :
  if n2 !=0 :
    result = "Can't divided by 0"
else:
  result = "Invalid symbol !!"

print("Result : ", result)
print("· · ─ ·ʚɞ· ─ · ·")

## Small project
- Calculator program 
โปรแกรมนี้เขียนด้วยภาษา Python 
และเขียนเพื่อฝึกการใช้ if-else และการรับค่า
