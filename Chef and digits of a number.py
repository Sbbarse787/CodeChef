T = int(input())
for i in range(T):
    string = input()
    count_zero=0
    count_one=0

    for i in string:
        if i == '0':
            count_zero = count_zero+1
        else:
            count_one = count_one+1

    len_string = len(string)-1
    if len_string == count_one or len_string == count_zero:
        print('Yes')
    else:
        print('No')