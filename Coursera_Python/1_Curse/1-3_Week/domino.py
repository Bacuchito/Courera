for left in range(7):
    for rigth in range(7):
        print('[' + str(left) + '|' + str(rigth) + ']', end = '' )
print()

########################################
team = ['Skt1', 'RNG', 'Cloud 9', 'SW', 'DRX' ]
for home_team in team:
    for away_team in team:
        if home_team != away_team:
            print(home_team + ' vs ' + away_team)