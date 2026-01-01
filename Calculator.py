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
  else:
    reseult = "Can't divided by 0"
else:
  result = "Invalid symbol !!"

print("Result : ", result)
print("· · ─ ·ʚɞ· ─ · ·")

