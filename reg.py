import re

# _________?_________
st1 = 'I am Batman'
st2 = 'I am Batwoman'
r = re.compile(r'Bat(wo)?man')
ot = r.search(st2)
print(ot.group(1))  # wo
print(ot.group())  # Batwoman
# _________*_________
st3 = 'I am Batwowowowoman'
r = re.compile(r'Bat(wo)*man')
ot = r.search(st3)
print(ot.group())  # Batwowowowoman
# _________+_________
r = re.compile(r'Bat(wo)+man')
ot = r.search(st3)
print(ot.group())

# _________{}_________
st4 = 'Ha' * 10
r = re.compile(r'(Ha){1,2}')  # жадный
ot = r.search(st4)
print(ot.group())

r = re.compile(r'(Ha){,15}')
ot = r.search(st4)
print(ot.group())

r = re.compile(r'(Ha){1,2}?')  # нежадный
ot = r.search(st4)
print(ot.group())

# _________findall_________
print('_________findall_________')
r = re.compile(r'wo')  # нежадный
print(r.findall(st3))  # ['wo', 'wo', 'wo', 'wo']

st1 = 'I am Batman, i have Batrang it is as rang'
r = re.compile(r'Bat(man|rang|woman|copter)')
print(r.findall(st1))  # ['man', 'rang']

st5 = 'I am Batman, she is Batwoman, it is Batrang'
r = re.compile(r'(Batwoman|Batman)')
print( r.findall(st5))  # ['Batman', 'Batwoman']

r = re.compile(r'(\b\w{2}\b)')  # Слова из двух символов
print(r.findall(st5))  # ['am', 'is', 'it', 'is']

# _________составное_________
st6 = 'You buy: 54 aples, 4 grapes, 8 oranges, i am Ostap'
r = re.compile(r'\d+\s\w+')
print(r.findall(st6))  # ['54 aples', '4 grapes', '8 oranges']
print(re.findall(r, st6))  # тоже самое
# _________[]_________
r = re.compile(r'[aeiouAEIOU]')
print(r.findall(st6))  # гласные

r = re.compile(r'[^aeiouAEIOU ]')
print(r.findall(st6))  # HE гласные и не пробел

st = 'Hello world!'
r = re.compile(r'^Hell')  # начинается с
r1 = r'world.$'  # заканчивается на
print(re.findall(r, st))
print(re.findall(r1, st))

st = 'Sum41 its u2 hi bebi3'
print(re.findall(r'(\w+\d)$', st ))
