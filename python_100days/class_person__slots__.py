# coding = utf-8


class Person(object):
    
    # 限制Person只能绑定 _name,_age,_gender 属性
    __slots__ = ('_name','_age','_gender')

    def __init__(self,name,age):
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
        if self._age < 18:
            print('%s is playing video game' % self._name)
        else:
            print('%s is working' % self._name)

def main():
    person = Person('zzm',12)
    person.play()
    person._age = 18
    person.play()
    person._gender = 'man'

if __name__ == '__main__':
    main()