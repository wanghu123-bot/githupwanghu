hero=['安琪拉','妲己','韩信','典韦','吕布']
hero.extend(['小乔','貂蝉'])
hero.index('妲己')
del hero[2]
hero[6]='白起'
hero.insert(4,'白起')
print(hero)
from pip._internal import index

scores=[88,76,90]
scores.insert(3,85)
scores[0]=82
del scores[1]
scores.insert(2,95)
pop=scores.index(82)
print(pop)
top=len(scores)
print(f'当前人数为:{top}')
scores.clear()
print(len(scores))# scores.clear()
print(scores)
