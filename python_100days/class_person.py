# coding = utf-8

class Person(object):
    def __init__(self,name,age):
        # 将属性以单下划线命名，表示属性是受保护的
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self,age):
        self._age = age

    def play(self):
        if self._age < 16:
            print('%s is watching anime' % self._name)
        else :
            print('%s is watching pron' % self._name)


def main():
    person = Person('zzm',12)
    person.play()
    person._age = 18
    person.play()

if __name__ == '__main__':
    main()