from queue import Queue

olympics = Queue(5)

print(olympics.empty())

print('\n###########################################################\n')

olympics.put('United States(USA)')
olympics.put('Great Britain(GBR)')

print(olympics.empty())
print(olympics.full())
print(olympics.qsize())
print(olympics.maxsize)

print('\n###########################################################\n')

olympics.put('China(CHN)')
olympics.put('Ukraine(UA)')
olympics.put('Poland(PL)')

print(olympics.empty())
print(olympics.full())
print(olympics.qsize())
print(olympics.maxsize)

print('\n###########################################################\n')


while not olympics.empty():
    print(olympics.get())
    print(olympics.qsize())

