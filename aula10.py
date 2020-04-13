from datetime import date, time, datetime, timedelta

def working_with_datetime():
    date_current = datetime.now()
    print(date_current)
    print(date_current.strftime('%d/%m/%y %H:%M:%S'))
    print(date_current.strftime('%c'))
    print(date_current.weekday())
    tupla = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo')
    print(tupla[date_current.weekday()])
    date_created = datetime(2018, 6, 20, 15, 30, 20)
    print(date_created)
    print(date_created.strftime('%c'))
    date_string = '01/01/2020 19:56:56'
    date_converted = datetime.strptime(date_string, '%d/%m/%Y %H:%M:%S')
    print(date_converted)
    new_date = date_converted - timedelta(days=365, hours=2, minutes=15)
    print(new_date)

def working_with_date():
    date_current = date.today()
    date_current_str = date_current.strftime('%A %B %Y')
    print(type(date_current))
    print(date_current_str)
    print(type(date_current_str))

def working_with_time():
    hour = time(hour=15, minute=18, second=30)
    print(hour)
    hour_str = hour.strftime('%H:%M:%S')
    print(hour_str)
    print(type(hour_str))

if __name__ == '__main__':
    #working_with_date()
    #working_with_time()
    working_with_datetime()
