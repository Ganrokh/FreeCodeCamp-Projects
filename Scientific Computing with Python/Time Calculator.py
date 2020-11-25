def add_time(start, duration, day=''):
    week = [
        'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
        'Saturday'
    ]
    clock = start.replace(':', ' ').split()
    timeToAdd = duration.split(':')
    daysLater = 0
    # Adds new time to starting time
    clock[0] = int(clock[0]) + int(timeToAdd[0])
    clock[1] = int(clock[1]) + int(timeToAdd[1])
    # Formats for hourly changes, AM/PM
    if clock[1] > 60:
        clock[1] -= 60
        clock[0] += 1
    while clock[0] > 11:
        if clock[2] == 'AM':
            clock[2] = 'PM'
        else:
            clock[2] = 'AM'
            daysLater += 1
        if clock[0] > 12:
            clock[0] -= 12
        else:
            break
    # Converts list of values to proper 0:00 time format
    new_time = f'{clock[0]}:'
    if clock[1] < 10:
        new_time += f'0{clock[1]} {clock[2]}'
    else:
        new_time += f'{clock[1]} {clock[2]}'
    # Advances the day of the week if applicable
    if day != '':
        dayInd = week.index(day.title()) + daysLater
        while dayInd > 6:
            dayInd -= 7
        new_time += f', {week[dayInd]}'

    if daysLater == 1:
        new_time += ' (next day)'
    elif daysLater > 1:
        new_time += f' ({daysLater} days later)'

    return new_time