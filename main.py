'''Prepro'''
def main():
    '''input'''
    mon = int(input())
    water = int(input())
    snum1 = int(input())
    snum2 = int(input())
    snum3 = int(input())
    total = mon - water
    if mon > water:
        if total % 3 == 0:
            price = 10*snum1
        elif total % 3 == 2:
            price = 15*snum1
        

main()
