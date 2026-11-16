#list
age=25
has_license=False
my_list=['Alice',25,age,True,has_license]
my_list[0]
age = my_list[1]
age
fruits = ['mango','strawberry','pineapple','banana']
fruits.append('kiwi')
fruits
fruits.insert(2,'papaya')
fruits.remove("mango")
fruits.reverse()
fruits




#Dictonaries
person = {
    'name':'Alice',
    'age':25,
    'city':'Bangalore'
}
person['phone']
print(person.get('phone'))
person
person['age']
person['name']='Dave'
person['name']
person['licence']=True
del person["licence"]
person
print(person.keys())
print(person.values())
print(person.items())

if ('name' in person):
    print("Name found")


#Tuples
empty=()
fruits=('mango','apple','Kiwi','banana')
fruits.append('mango')
fruits[0]='orange'


#sets
empty_set=()
numbers={1,2,3,4,5}
fruits = set(['apples','banana','pineapple','orange'])


scores=[85,90,85,90,99,87]
unique_scores=set(scores)
unique_scores

import string

def count_words(text):
    freq={}
    words = [word.strip(string.punctuation)for word in text.split()]
    for word in words:
        word = word.lower()
        if word=='':
            continue
        if word in freq:
            freq[word]+=1
        else:
            freq[word]=1
    return freq
count_words("The cat and the hat")
count_words("hello - hello")

assert count_words("Hello, hello!") == {"hello":2}, "Punctuation need to be removed"
assert count_words("") == {} , "empty text should give an empty dictionary"
assert count_words("hello - Hello") == {"hello":2}, "Key cannot be blank"

assert count_words("a A b") == {"a": 2, "b": 1}

def second_largest(numbers):
    first = float('-inf')
    second = float('-inf')
    for num in numbers:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    return second if second!=float('-inf') else None

assert(second_largest([-2,10,-9,-1,1])==1), "Code should evaluate negative numbers too"
assert(second_largest([1,1,1,1])==None), "Second largest is strictly smaller than the First"
assert(second_largest([0])==None), "Default value should be none"
            
def only_in_first(list_a, list_b):
    return set(list_a) - set(list_b)

def only_in_first(list_a, list_b):
    list_b = set(list_b)
    ans=[]
    for item in list_a:
        if item in list_b:
            continue
        else:
            ans.append(item)
    return ans

only_in_first([1,2,3],[3,2,1])

assert (only_in_first([],[1,2,3,5])==[]), "Input is empty"
assert (only_in_first([1,1,1],[2,1,1])==set()), "Each number should occur only once"
assert (only_in_first([1,2,3],[3,2,1])==set()), "No matching should return empty set"

a = [1, 2, 3, 4, 2]
b = [3, 4, 5]
print(only_in_first(a, b))

assert(1 == 2, "this should fail")
print("reached the end")

assert 2 + 2 == 4

assert 2 + 2 == 5, "Math is broken"



import time

numbers = list(range(200_000))
numbers_set = set(numbers)
target = 199_999   # the last item: the worst case for a list scan

start = time.perf_counter()          # start a stopwatch
for _ in range(200):                 # repeat 200 times, so the time is measurable
    target in numbers
list_time = time.perf_counter() - start

start = time.perf_counter()
for _ in range(200):
    target in numbers_set
set_time = time.perf_counter() - start

print("list:", list_time)
print("set: ", set_time)




assert 1 == 2, "this should fail"
print("reached the end")




