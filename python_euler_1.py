sum=0
count=1
def is_multiple(n):
    if ( ( n % 3 ) == 0 ) or ( ( n %5 ) == 0 ):
        return True
    else:
        return False

while count < 1000:
    if is_multiple(count):
        sum = sum + count 
    count = count + 1

print(sum)
