import random

pitchers = ['Taylor', 'Jackson', 'Anderson', 'Thomas']
batter = ['Smith', 'Jones', 'Johnson', 'Williams', 'Jones', 'Davis', 'Wilson', 'Miller', 'Moore']

log = open('batting.log', 'w+')

for x in range(10):
  for pitcher in pitchers:
    for batter in batters:
      r = random.random()
      result = ''
      if r < 0.5:
        result = 'SO'
      elif r < 0.7:
        result = 'O'
      elif r < 0.82:
        result = 'BB'
      elif r < 0.88:
        result = '1B'
      elif r < 0.92:
        result = '2B'
      elif r < 0.96:
        result = '3B'
      else:
        result = 'HR'
      log.write(f'{batter} {result} v {pitcher}')
