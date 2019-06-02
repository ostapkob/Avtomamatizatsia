#  https://habr.com/ru/post/141411/
def shout(word='yes'):
    return word.capitalize() + '!'


def talk():
    def whisper(word="да"):
        return word.lower() + "...";

    print(whisper())


# ========================

print(shout('rrrrrr'))
scream = shout('uuuuu')

# del shout  # try
print(scream)
print(shout('eeeeeee'))
# ========================
talk()


# =========================
print('==============================')
def getTalk(type='f1'):
    def f1(word='yes'):
        return word.capitalize() + '!'

    def f2(word='yes'):
        return word.lower() + '...'

    if type == 'f1':
        return f1()
    else:
        return f2()

print(getTalk('f2'))

def ramka(fun):
    def wrapper():
        print('▬'*10)
        fun()
        print('▬'*10)
    return wrapper

@ramka # simple = ramka(simple)
def simple():
    print('TEST')


simple()

