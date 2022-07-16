def add(a,b):
  p=int(a)
  q=int(b)
  sum=p+q
  return sum
def main():
  a=input('Enter 1st number?')
  b=input('Enter 2nd number?')
  sum=add(a,b)
  print('Sum of',a,'and',b,'is',sum)

main()
  