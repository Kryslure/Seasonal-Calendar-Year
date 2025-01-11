# april 11 = spring
# Spring: March 20 - June 20

input_month = input()
input_day = int(input())

# Spring: March 20 - June 20
if input_month == 'March' and 20 <= input_day <= 31:
    print("Spring")
elif input_month in ('April', 'May') and 1 <= input_day <= 31:
    print("Spring")
elif input_month == 'June' and 1 <= input_day <= 20:
    print("Spring")

# Summer: June 21 - September 21
elif input_month == 'June' and 21 <= input_day <= 31:
    print("Summer")
elif input_month in ('July', 'August') and 1 <= input_day <= 31:
    print("Summer")
elif input_month == 'September' and 1 <= input_day <= 21:
    print("Summer")

# Autumn: September 22 - December 20
elif input_month == 'September' and 22 <= input_day <= 31:
    print("Spring")
elif input_month in ('October', 'November') and 1 <= input_day <= 31:
    print("Spring")
elif input_month == 'December' and 1 <= input_day <= 20:
    print("Spring")

# Winter: December 21 - March 19
elif input_month == 'December' and 21 <= input_day <= 31:
    print("Winter")
elif input_month in ('January', 'February') and 1 <= input_day <= 31:
    print("Winter")
elif input_month == 'March' and 1 <= input_day <= 19:
    print("Winter")

# If user results are out of bounds, print Invalid
else:
    print("Invalid")

