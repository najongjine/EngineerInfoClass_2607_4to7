a = ['한국', '중국', '일본',"일본"]
a.append('베트남')
a.extend(["한국","일본","중국","호주"])
a.remove('일본')
a=set(a)
a.update({'한국'})
print(a)

