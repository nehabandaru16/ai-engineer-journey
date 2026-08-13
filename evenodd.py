#even/odd list comprehension script

# for n in numbers:
  #  if n % 2 == 0:
  #      evens.append(n)
  #  else:
   #     odds.append(n)
   
def split_even_odd(numbers):
    evens = [n for n in numbers if n % 2 == 0]
    odds = [n for n in numbers if n % 2 != 0]  
    return evens, odds

evens, odds = split_even_odd([1, 2, 3, 4, 5, 6, 7, 8])
print(evens)
print(odds)
