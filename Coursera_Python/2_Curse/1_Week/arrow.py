import arrow
date = arrow.get('2022-11-12', 'YYYY-MM-DD')
date.shift(days=+3).format('DD MMM YYYY')

print(date)