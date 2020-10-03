n,x = input().split()

scores = [input().split() for _ in range(int(x))]
#scores = [map(float, input().split() for _ in range(int(x)))]


for score in zip(*scores):
    score = list(map(float, score))
    print(sum(score) / int(x))
