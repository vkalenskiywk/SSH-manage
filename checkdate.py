import datetime
c_y = int(datetime.datetime.now().year)


def checkdate_d(day):
    if len(day) > 0:
        day = int(day)
        if (day > 0) & (day <= 9):
            return 2
        elif (day > 9) & (day <= 31):
            return 0
        else:
            return 1
    else:
        return 1

def checkdate_m(month):
    if len(month) > 0:
        month = int(month)
        if (month > 0) & (month <= 9):
            return 2
        elif (month > 9) & (month <= 12):
            return 0
        else:
            return 1
    else:
        return 1

def checkdate_y(yr):
    if len(yr) > 0:
        yr = int(yr)
        if (yr >1900) & (yr <= c_y):
            return 0
        else:
            return 1
    else:
        return 1