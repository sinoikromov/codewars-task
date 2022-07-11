'''
Эта проблема получила свое название от, пожалуй, самого важного события в жизни древнего историка Иосифа Флавия: 
согласно его рассказу, он и его 40 солдат были заперты в пещере римлянами во время осады.

Отказавшись сдаться врагу, они вместо этого выбрали массовое самоубийство с изюминкой: они образовали круг и продолжали
убивать одного человека каждые три, пока не остался последний человек (и что он должен был убить себя, чтобы закончить действие). ) .

Что ж, Иосиф Флавий и еще один человек были последними двумя, и, поскольку мы теперь знаем каждую деталь этой истории,
вы, возможно, правильно догадались, что они не совсем следовали первоначальной идее.

Теперь вам нужно создать функцию, которая возвращает перестановку Иосифа Флавия, принимая в качестве параметров исходный
массив/список элементов , подлежащих перестановке, как если бы они были в круге, и подсчитывая каждые k мест, 
пока не останется ни одного.

Советы и примечания: помогает начать считать от 1 до n вместо обычного диапазона 0..n-1; k всегда будет >=1.

Например, при n=7 и k=3 josephus(7,3)следует поступать так.

[1,2,3,4,5,6,7] - initial sequence
[1,2,4,5,6,7] => 3 is counted out and goes into the result [3]
[1,2,4,5,7] => 6 is counted out and goes into the result [3,6]
[1,4,5,7] => 2 is counted out and goes into the result [3,6,2]
[1,4,5] => 7 is counted out and goes into the result [3,6,2,7]
[1,4] => 5 is counted out and goes into the result [3,6,2,7,5]
[4] => 1 is counted out and goes into the result [3,6,2,7,5,1]
[] => 4 is counted out and goes into the result [3,6,2,7,5,1,4]
Итак, наш окончательный результат:

josephus([1,2,3,4,5,6,7],3)==[3,6,2,7,5,1,4]
'''
def josephus(items, k):
    counter = 0
    dead = []
    while items:
        counter = (counter + k - 1) % len(items)
        dead.append(items.pop(counter))
    return dead


if __name__ == '__main__':
    print(josephus([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2))

'''
[1,2,3,4,5,6,7] - initial sequence
[1,2,4,5,6,7] => 3 is counted out and goes into the result [3]
[1,2,4,5,7] => 6 is counted out and goes into the result [3,6]
[1,4,5,7] => 2 is counted out and goes into the result [3,6,2]
[1,4,5] => 7 is counted out and goes into the result [3,6,2,7]
[1,4] => 5 is counted out and goes into the result [3,6,2,7,5]
[4] => 1 is counted out and goes into the result [3,6,2,7,5,1]
[] => 4 is counted out and goes into the result [3,6,2,7,5,1,4]
'''
