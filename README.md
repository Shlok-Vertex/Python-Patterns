# Python Patterns 🐍

A collection of common programming patterns implemented in Python. These patterns cover algorithmic, structural, and design pattern concepts.

## Table of Contents. 
1. [Star Patterns](#star-patterns)
2. [Number Patterns](#number-patterns)
3. [Design Patterns](#design-patterns)
4. [Algorithmic Patterns](#algorithmic-patterns)


## Star Patterns

### 1. Right-Angled Triangle
```python
for i in range(1, 6):
    print('*' * i)
```

 ### 2. Inverted Right-Angled Triangle
 ```python
for i in range(5, 0, -1):
    print('*' * i)
```

### 3. Pyramid Pattern
```python
n = 5
for i in range(1, n+1):
    print(' '*(n-i) + '*'*(2*i-1))
```

# Number Patterns

### 1. Simple Number Triangle
```python
for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end=' ')
    print()
```
### 2. Factory Pattern
```python
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

def get_pet(pet="dog"):
    pets = dict(dog=Dog(), cat=Cat())
    return pets[pet]
```

