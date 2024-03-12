# https://www.codewars.com/kata/59dd3ccdded72fc78b000b25
day = {
  1 : 'Sunday',
  2 : 'Monday',
  3 : 'Tuesday',
  4 : 'Wednesday',
  5 : 'Thursday',
  6 : 'Friday',
  7 : 'Saturday'
}
def whatday(num):
  return day[num] if num in day else 'Wrong, please enter a number between 1 and 7'

# test 
print(whatday(2))

# best clever
# WEEKDAY = {
#     1: 'Sunday',
#     2: 'Monday',
#     3: 'Tuesday',
#     4: 'Wednesday',
#     5: 'Thursday',
#     6: 'Friday',
#     7: 'Saturday' }
# ERROR = 'Wrong, please enter a number between 1 and 7'


# def whatday(n):
#     return WEEKDAY.get(n, ERROR)