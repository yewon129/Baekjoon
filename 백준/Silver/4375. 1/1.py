while 1:
    try:
        n = int(input())
    except:
        break
    num = 1
    order = 1
    while 1:
        if num % n == 0:
            print(order)
            break
        num += 10**order
        order += 1