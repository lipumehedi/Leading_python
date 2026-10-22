from datetime import datetime

d = datetime.strptime("2026-10-22", "%Y-%m-%d")
print(d.date())
print(d.strftime("%Y-%m"))

#An easy way to remember: strpp = parse (read), strff = format (write).

datetime.strptime("2026-02-30", "%Y-%m-%d") 
# ValueError: day is out of range for month