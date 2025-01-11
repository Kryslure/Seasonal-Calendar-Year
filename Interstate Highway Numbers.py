# Primary U.S. interstate highways are numbered 1-99. Odd numbers (like the 5 or 95) go north/south,
# and evens (like the 10 or 90) go east/west. Auxiliary highways are numbered 100-999, and service
# the primary highway indicated by the rightmost two digits. Thus, I-405 services I-5, and I-290
# services I-90. Note: 200 is not a valid auxiliary highway because 00 is not a valid primary highway number.

# Given a highway number, indicate whether it is a primary or auxiliary highway. If auxiliary,
# indicate what primary highway it serves. Also indicate if the (primary) highway runs north/south or east/west.

# primary == 1 - 99
# odd = n / s
# even = e / w
# aux == 100-999
# aux services primary by indications: 405 = 05 ; 290 = 90 ; etc
# aux != 00

highway_number = int(input())

result = (
    (f"{highway_number} is not a valid interstate highway number.")
    if highway_number < 1 or highway_number > 999
    else (
        (f"I-{highway_number} is primary, going {'north/south' if highway_number % 2 else 'east/west'}.")
        if 1 <= highway_number <= 99
        else(f"I-{highway_number} is auxiliary, serving I-{highway_number % 100}, going {'north/south' if (highway_number % 100) % 2 else 'east/west'}.")
            if 100 <= highway_number <= 999 and highway_number % 100 != 0
            else(f"{highway_number} is not a valid interstate highway number.")
        )
)
print(result)
