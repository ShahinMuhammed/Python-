current_year=int(input("Enter current year"))
fut_year=int(input("Enter future year"))
for year in range(current_year,fut_year+1):
	if year%400==0 or year%100!=0 and year%4==0:
		print(year)
