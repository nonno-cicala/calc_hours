#!/usr/bin/env python3

from sys import argv
from datetime import timedelta
from functools import reduce

def timedelta_from_arg(arg):
  time_array = arg.split(':')
  is_sum = not time_array[0][0] == '-'

  if len(time_array) == 2:
    return timedelta(
      hours=int(time_array[0]),
      minutes=(int(time_array[1]) if is_sum else -int(time_array[1]))
    )
  else:
    return timedelta(minutes=int(time_array[0]))

if len(argv) < 2:
  print('Usage: ' + argv[0] + ' [-][hours:]minutes ...')
else:
  times = argv[slice(1, len(argv))]
  td = list(map(timedelta_from_arg, times))
  total = reduce(lambda td1, td2: td1 + td2, td)

  print(round(total / timedelta(hours=1), 2))