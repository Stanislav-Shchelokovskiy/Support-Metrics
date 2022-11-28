from datetime import date, datetime
from dateutil.relativedelta import relativedelta

if __name__ == '__main__':
    print(date.today() + relativedelta(days=1))