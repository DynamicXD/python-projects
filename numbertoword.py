w = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
     "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty"]
wh = ["zz", "ttt", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety", "hundred"]
ww = ""

n = int(input("Enter an amount: "))

r = n % 100
if r != 0:
    ww = (w[r] if r <= 20 else wh[(r - r % 10) // 10] + " " + (w[r % 10] if r % 10 != 0 else "")) + " Rupees"

n = n - r
h = n % 1000
r = h // 100
if r != 0:
    ww = (w[r] if r <= 20 else wh[(r - r % 10) // 10] + " " + w[r % 10]) + " Hundred and " + ww

n = n - h
t = n % 100000
r = t // 1000
if r != 0:
    ww = (w[r] if r <= 20 else wh[(r - r % 10) // 10] + " " + w[r % 10]) + " Thousand " + ww

n = n - t
l = n % 10000000
r = l // 100000
if r != 0:
    ww = (w[r] if r <= 20 else wh[(r - r % 10) // 10] + " " + w[r % 10]) + " Lakhs " + ww

print(ww + " only.")
print(50 // 10)
