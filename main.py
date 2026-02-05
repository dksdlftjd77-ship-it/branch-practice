# fizzbuzz
# 1~n 까지 양의 정수에 대해,
# 3의 배수, 'fizz'
# 5의 배수, 'buzz'
# 15의 배수, 'fizzbuzz'
for i in range(1, 15+1):
    if i % 15 == 0:
        print('fizzbuzz')
    elif i % 3 == 0:
        print('fizz')
    elif i % 5 == 0:
        print('buzz')
    else:
        print(i)
