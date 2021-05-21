def int_to_Roman( num):
        int_val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        rom_val = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        roman_num = ''
        i = 0
        while  num > 0:
            for q in range(num // int_val[i]):
                roman_num = roman_num+rom_val[i]
                num = num- int_val[i]
            i += 1
        return roman_num

print(int_to_Roman(1234))


