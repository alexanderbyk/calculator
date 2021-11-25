def summa(number_1,number_2):
  return number_1 + number_2

def raznost(number_1,number_2):
  return number_1 - number_2

def umnojeniye(number_1,number_2):
  return number_1 * number_2

def deleniye(number_1,number_2):
  if number_2 == 0:
    return 'На ноль делить нельзя!'
  else:
    return number_1 / number_2


if __name__ == '__main__':
  print(summa(2,4))
  print(raznost(2,4))
  print(umnojeniye(2,4))
  print(deleniye(2,4))
ggkgkg
