from my_classes import Hitting

log = open('batting.log', 'r')
good_results = ['1B', '2B', '3B', 'HR']
# keys: batter's name
# values: Hitting object
batting_averages = {}

for line in log.readlines():
    parts = line.split()
    batter = parts[0]
    result = parts[1]
    hitting = batting_averages.get(batter, Hitting())
    if result in good_results:
        hitting.add_hit()
    else:
        hitting.add_out()
    batting_averages[batter] = hitting

output = open('averages.log', 'w')
for batter, hitting in batting_averages.items():
    temp = f'{batter} {hitting.bat_avg():.2f}'
    print(temp)
    output.write(temp + '\n')

    # print('{batter} {avg:.2f}'.format(batter=batter, avg=hitting.bat_avg()))
    # print('{} {:.2f}'.format(batter, hitting.bat_avg()))
