def main():
 n = int(input('Enter number: '))
 if is_even(n):
  print('Even')
 else:
  print('Odd')

def is_even(n):
  # return True if n%2 == 0 else False
 return n % 2 == 0
 
main()