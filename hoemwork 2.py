#1
n = 0
while n < 10:
    print(n)
    if n == 5:
        break
    n += 1
   
#2
n = 0
while n < 5:
    print(n)
    n = n + 1
else:
    print(n, 'is not less than 5')


#3
fruits = ['orange', 'peach', 'apple', 'bluberry', 'dragonfruit']
for fruit in fruits:
    if fruit == 'apple':
        print(fruit, 'is really a fruit?')
        break
    else:
        print('I like', fruit)
    
#4
x = 30
sum = 0
i = 1

while i <= x:
    sum = sum + i
    i = i + 1
print(sum)

#5
grade = 85
if grade >= 90:
    print('Your grade is A')
elif grade >= 80:
    print('Your grade is B')
elif grade >= 70:
    print('Your grade is C')
elif grade >= 60:
    print('Your grade is D')
else:
    print('Your grade is F')
    
#6
marks = {"Andy":88, "Amy":66, "James": 90, "Jules": 55, "Arthur": 77}
#6.1
for name, grade in marks.items():
    print(f'{name} got a {grade}')

#6.2
import statistics 
print(statistics.mean(marks.values()))
print(max(marks.values()))
print(min(marks.values()))

#6.3
for names in marks.keys():
    if 'J' in names:
        break
    print(names)

#6.4
for names in marks.keys():
    if 'J' in names:
        continue
    print(names)

