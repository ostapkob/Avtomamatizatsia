import re

o1 = 'iiiii444-4242it'
o2 = 'my number (123)-444-4242 22'
rr = re.compile(r'\d{3}-\d{3}-\d{4}')
rr = re.compile(r'(\(\d\d\d\)-)?(\d\d\d-\d\d\d\d)')
mo = rr.search(o1)
r1, r2 = mo.groups()
print(r1, r2)

mo = rr.search(o2)
r1, r2 = mo.groups()
print(r1, r2)

batRegex = re.compile(r'Bat(mobile|man|copter)')
mo = batRegex.search('i have Batcopter, I am Batman, ')
print(mo.group())

batRegex = re.compile(r'Bat(wo)?man')
mo = batRegex.search('I am Batman, i have Batcopter')
print(mo.group())
mo = batRegex.search('I am Batwoman, i have Batcopter')
print(mo.group())

#____________.*_________________
ss = '''В Донбассе 2020 пропал итальянский журналист. В 2019 об этом сообщили в генпрокуратуре ЛНР. Об исчезновении военного фотографа и корреспондента Роберто Травана там узнали от его знакомой — жительницы Мариуполя.
По ее словам,  в середине декабря 2018 года журналист прибыл в город, чтобы снять серию репортажей о вооруженном конфликте в регионе. К нему были приставлены несколько украинских пограничников, передает телеканал "Россия 24". Но Траван жаловался, что они не дают ему снимать то, что он считает нужным.'''
ot = re.search( r'20\d\d (.*) 20\d\d (.*)', ss)
print(ot.group(1), ot.group(2), sep = ' || ')

st = 'I am Batwoman, i have batcopter'
r = re.compile(r'bat\w+', re.I)
print(re.findall(r, st))  # ['Batwoman', 'batcopter']
print(re.search(r, st).group())  # Batwoman

#____________sub_________________
st = 'Agent Alice gave the secret documents to Agent Bob from agent Eve'
r = re.compile(r'Agent (\w)\w*', re.I) #не чувствительны к регистру
new = r.sub(r'\1****', st)  # A**** gave the secret documents to B**** from E****
print(new)
