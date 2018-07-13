#!/usr/bin/python3
import datetime


class Arris:
    def __init__(self):
        pass

    def build_list1(self):
        day_of_week = datetime.datetime.today().weekday()  # Monday-sunday 0-6
        list1 = []
        TABLE1 = [
            [15, 15, 24, 20, 24],
            [13, 14, 27, 32, 10],
            [29, 14, 32, 29, 24],
            [23, 32, 24, 29, 29],
            [14, 29, 10, 21, 29],
            [34, 27, 16, 23, 30],
            [14, 22, 24, 17, 13]
        ]
        for i in range(4+1):
            list1.append(TABLE1[day_of_week][i])
        day_of_month = datetime.datetime.today().day # 1-31
        list1.append(day_of_month)

        month = datetime.datetime.today().month  # jan-dec 1-12
        year = datetime.datetime.today().year  # 2018
        last_two_year_digits = int(str(year)[-2:])

        # The month number + the last 2 digits of the year minus the day date (YY+MM - DD)
        if ((last_two_year_digits + month) - day_of_month < 0):
            list1.append((((last_two_year_digits + month) - day_of_month) + 36) % 36)
        else:
            list1.append(((last_two_year_digits + month) - day_of_month) % 36)

        list1.append( (((3 + ((last_two_year_digits + month) % 12)) * day_of_month) % 37) % 36 )

        return list1

    def build_list2(self, seed='MPSJKMDHAI'):
        list2 = []
        # Get the utf16 code mod 36 for the first 8 letters in the seed
        for i in range(7+1):
            list2.append( ord(seed[i]) % 36)

        return list2

    def build_list3(self, list1, list2):
        list3 = []
        for i in range(7+1):
            list3.append(((list1[i] + list2[i])) % 36)

        list3.append(sum(list3) % 36)

        magic_number = list3[8] % 6  # one of many magic numbers really

        list3.append(magic_number ** 2)

        return list3

    def build_list4(self, list3):
        list4 = []
        TABLE2 = [
            [0, 1, 2, 9, 3, 4, 5, 6, 7, 8],
            [1, 4, 3, 9, 0, 7, 8, 2, 5, 6],
            [7, 2, 8, 9, 4, 1, 6, 0, 3, 5],
            [6, 3, 5, 9, 1, 8, 2, 7, 4, 0],
            [4, 7, 0, 9, 5, 2, 3, 1, 8, 6],
            [5, 6, 1, 9, 8, 0, 4, 3, 2, 7]
        ]
        for i in range(9+1):
            magic_number = list3[8] % 6  # one of many magic numbers really
            list4.append(list3[TABLE2[magic_number][i]])

        return list4

    def build_list5(self, list4, seed='MPSJKMDHAI'):
        list5 = []
        for i in range(9+1):
            list5.append((ord(seed[i]) + list4[i]) % 36)

        return list5

    def build_all(self):
        return self.build_list5(self.build_list4(self.build_list3(self.build_list1(), self.build_list2())))

    def generate_password(self):
        idx = self.build_all()
        idx_len = len(idx)
        ALPHANUM = [
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D',
            'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
            'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
        ]
        password_of_the_day = ""
        for i in range(idx_len):
            password_of_the_day += ALPHANUM[idx[i]]
        return password_of_the_day


pwn = Arris()
password = pwn.generate_password()
print(f'Password: {password}\nhttp://192.168.100.1/cgi-bin/tech_support_cgi\nhttp://192.168.100.1/\nhttp://192.168.100.1/cgi-bin/adv_pwd_cgi\nMake sure your local time is synced up with the modem\'s reported time')
