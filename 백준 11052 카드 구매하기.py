'''
문제
요즘 민규네 동네에서는 스타트링크에서 만든 PS카드를 모으는 것이 유행이다.
8가지가 있다.
카드는 카드팩의 형태로만 구매할 수 있고, 
카드팩의 종류는 카드 1개가 포함된 카드팩, 카드 2개가 포함된 카드팩, ... 카드 N개가 포함된 카드팩과 같이 
총 N가지가 존재한다.

민규는 카드의 개수가 적은 팩이더라도 가격이 비싸면 높은 등급의 카드가 많이 들어있을 것이라는 미신을 믿고 있다. 
따라서, 민규는 돈을 최대한 많이 지불해서 카드 N개 구매하려고 한다. 카드가 i개 포함된 카드팩의 가격은 Pi원이다.

카드 팩의 가격이 주어졌을 때, 
N개의 카드를 구매하기 위해 민규가 지불해야 하는 금액의 최댓값을 구하는 프로그램을 작성하시오.
N개보다 많은 개수의 카드를 산 다음, 나머지 카드를 버려서 N개를 만드는 것은 불가능하다. 
즉, 구매한 카드팩에 포함되어 있는 카드 개수의 합은 N과 같아야 한다.

입력
첫째 줄에 민규가 구매하려고 하는 카드의 개수 N이 주어진다. (1 ≤ N ≤ 1,000)

둘째 줄에는 Pi가 P1부터 PN까지 순서대로 주어진다. (1 ≤ Pi ≤ 10,000)

출력
첫째 줄에 민규가 카드 N개를 갖기 위해 지불해야 하는 금액의 최댓값을 출력한다.
'''

n = int(input())
p = [0] + list(map(int, input().split()))
d = [0] * (n+ 1)

'''
d[i] = 카드 i개를 구매하는 최대 가격
     =  p[1] + d[i - 1]
        p[2] + d[i - 2]
        p[3] + d[i - 3]
        .
        .
        .
        p[i] + d[0]
            중 최댓값

'''

for i in range(1, n + 1):
    for k in range(1, i + 1):
        d[i] = max(d[i], d[i - k] + p[k])
       
print(d[n])