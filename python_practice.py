"""
# check the given no. is even or odd

num=int(input("enter n0"))
if num%2==0:
    print(num,'is even no.')
else:
    print(num,"is a odd no")

#check factorial no



def factoral(n):
  fact = 1
    for i in range(1,n+1):
        fact= i*fact
    return fact

# check Armstrong no----pebding


num = str("n")
def is_armstrong_no(n):
    no_of_digit = len(n)
    power= no_of_digit
    [0]
#sun of a ist
def listsum():

list1 = [2,5.8,9]
lar_no=[0]
for i in list1:
    if i > lar_no:
        lar_no=i
return lar_no

#swap two string

s1=3
s2=4
temp=s1
s1=s2
s2=temp
print(s1)
print(s2)

x=2
y=4
x,y=y,x
print(x)
print(y)
#random
import random
import string
x=random.random()
print(x)
string = string.ascii_letters()+string.digits()
print(string())


#largest no. in list
a=4
b=5
c=7
if a>b and a>c:
    print("largest no",a)
elif b>c and b>a:
    print("largest no. is",c)

else:
    print("largest no is",c)




list=[4,8,9,5,1,-3]
largest =4
for i in list:
    if i > largest:
        largest=i
print(largest)

list=[6,8,9,7.2,2.4]
print(min(list))

list1=[3,6,7,9,2]
#sorted_list=sorted(list1)
#a2ndlargest=dd[-2]   #invalid decimal literal, TypeError
#print(a2ndlargest)
list_2=sorted(list1,reversed=True)
print(list_2)

#prime no/ sequence of prime no

# list of prime no
def is_prime_no(n):
    if n<2:
        return False
    if n==2:
        return True
    for i in range(2,int(n**.5+1)):
        if n%i==0:
            return False
    return True
list_prime=[]
for i in range(2,50):
    if is_prime_no(i):
        list_prime.append(i)
print(list_prime)











def num_is_prime(num):
    if num <= 1:
        return False
    if num >=2:
        for i in range(2,int(num**0.5+1)):
            if num%i == 0:
                return False
    return True
#NameError: name 'primr_no' is not defined-----name error

def sequence_of_prime_no(limit,end):
    for num in range(limit, end+1):
        if num_is_prime(num):
            print(num)
sequence_of_prime_no(208,800)


#vovel / consonent
def is_volel(var):
    if var== "a" or "e" or "i" or "o" or "u" or "A" or "E" or "I" or "O" or "U":
        print(var, "is a vovel")
    else:
        print(var, "is a conxonent")
is_volel("u")
#find volist



def num_is_prime(num):
    if num <= 1:
        return False
    if num >=2:
        for i in range(2,int(num**0.5+1)):
            if num%i == 0:
                return False
    return True

def prime_no_filter(number):
    prime_no_list = []
    for num in number:
        if num_is_prime(num):
            prime_no_list.append(num)

    return prime_no_list

number = [3,8,9,17,90,111,764,29,57,97]
list_prime = prime_no_filter(number)
print(list_prime)

#string slicing
list1="moh an "
# list2=list1[::-1]
# print(list2)
# print(list1.split("h"))
# print(list1.strip(" "))
#print(list1[0:-1])
new_list=[]
for i in list1:
    new_list.append(i)
print(new_list)





# Basic Python Questions
# Reverse a String:
str= "ajay"
#print(str[::-1])
#print("".join(reversed(str)))
rev_str=""
for i in str:
  rev_str = i+rev_str

print(rev_str)


#Write a function to reverse a given string.
#Palindrome Check:
def palindrome_check(n):
    if n==n[::-1]:
      return n, "is a Palindrome no"
    else:
      return n, "is not a Palindrome no"
print(palindrome_check("madam"))


#Write a function to check if a given string is a palindrome











#Implement a function to calculate the factorial of a given number.
#Fibonacci Sequence:

def factorial(num):
    fact_no=1
    if num == 1:
        fact_no = 1
    if num > 1:
        for i in range(1, num+1):
            fact_no=i*fact_no
    return fact_no


print(factorial(-5))


# Generate the Fibonacci sequence up to a given number.

#0,1,2,3,5,8,11
def fiboncci_sequence(num_start, num_end):
    a,b=0,1
    fib_sequence=[]
    for i in range(50): # i can also write i=_  to say i is not used in stement
        if num_start >=5:

            fib_sequence.append(a)

            a,b=b,a+b

            if a>20:
                break

    return fib_sequence
print(fiboncci_sequence(5,20))






#Find the Largest Element in a List:
list1 = [1,8,90,55]
#print(max(list1))
max_value = list1[0]
for i in list1:
  if i>max_value:
    max_value=i

print(i)
list1=[1,8,5,7,2,8]
sorted_list1=sorted(list1)
sh=sorted_list1[-2]
print(sh)


#sorted_list1[-2]

l1=[6,9.4,90]
#Write a function to find the largest element in a list.
def find_largest(num):

    return max(l1)
print(find_largest(l1))

list3=[3,7,8,9,3]
largest_no=list3[0]
for i in list3:
    if i > largest_no:

        largest_no = i
print(largest_no)
submition = 0
for i in list3:
    submition = submition+i
print(submition)

print(sum(list3))  #sum() function"


def sum1(nub):
    submition = 0
    for i in nub:
        submition = submition + i
    return submition

res=[1,2,4]
print(sum1(res))

Sum of List Elements:



Calculate the sum of all elements in a list.


#Count Vowels in a String:

def vowels(n):
    no_vowels=0
    for i in n:
        if i == a or e or i or u:
            no_vowels = no_vowels+1
        i=i+1
    return no_vowels
n= "ajay jha"
print(vowels(n))




Count the number of vowels in a given string.
Check Prime Number:

Write a function to check if a given number is prime.
Merge Two Lists:

Merge two lists into a single list.
Remove Duplicates from a List:

Remove duplicate elements from a list.
Find the Minimum Element in a List:

Write a function to find the minimum element in a list.
Check if a List is Sorted:

Write a function to check if a list is sorted in ascending order.
Find the Common Elements in Two Lists:

#Write a function to find common elements between two lists.
def common_elements(list1,list2):
    set1= set(list1)
    set2= set(list2)
    common_set= set1 & set2
    common_list = list(common_set)
    return common_list
list1= [1,2,3]
list2= [2,3,4]
print(common_elements(list1,list2))

"""
#Count the Frequency of Each Element in a List:
list1 = [1,3,8,3]
freq=dict{}
for i in list1:
    if i in freq:
        i=i+1


Write a function to count the occurrences of each element in a list.
Flatten a Nested List:

Write a function to flatten a nested list into a single list.
Intermediate Python Questions
List Comprehension:

Use list comprehension to create a list of squares of numbers from 1 to 10.
Dictionary Merge:

Merge two dictionaries into one.
Find the Intersection of Two Sets:

Find the common elements between two sets.
Sort a List of Tuples by the Second Element:

Sort a list of tuples based on the second element of each tuple.
Read and Write to a File:

Write a script to read from a file and write to another file.
Parse JSON Data:

Write a function to parse JSON data and extract specific values.
Generate Random Numbers:

Generate a list of random numbers within a given range.
Count Words in a String:

Count the frequency of each word in a given string.
Find the Unique Elements in a List:

Write a function to find unique elements in a list.
Transpose a Matrix:

Write a function to transpose a given 2D matrix.
Check if Two Strings are Anagrams:

Write a function to check if two strings are anagrams of each other.
Check for Balanced Parentheses:

Write a function to check if parentheses in a string are balanced.
Count Distinct Elements in a List:

Write a function to count distinct elements in a list.
Find the Longest Substring Without Repeating Characters:

Write a function to find the longest substring with all unique characters.
Reverse Words in a String:

Write a function to reverse the words in a given string.
Advanced Python Questions
Implement a Stack:

Implement a stack using a list with push and pop operations.
Implement a Queue:

Implement a queue using a list with enqueue and dequeue operations.
Sort a List Using Merge Sort:

Implement the merge sort algorithm to sort a list.
Binary Search Algorithm:

Write a function to perform binary search on a sorted list.
Depth-First Search (DFS) in a Graph:

Implement the DFS algorithm for a graph.
Breadth-First Search (BFS) in a Graph:

Implement the BFS algorithm for a graph.
Find the Greatest Common Divisor (GCD):

Write a function to compute the GCD of two numbers.
Generate Permutations of a String:

Write a function to generate all permutations of a given string.
Find the Longest Common Subsequence:

Write a function to find the longest common subsequence between two strings.
Calculate the Power of a Number:

Write a function to calculate
𝑥
𝑦
x
y
  where x and y are integers.
Find the Kth Largest Element in an Array:

Write a function to find the Kth largest element in an array.
Rotate a Matrix 90 Degrees:

Write a function to rotate a given 2D matrix 90 degrees clockwise.
Find the Missing Number in a List:

Given a list of integers from 1 to n with one number missing, find the missing number.
Detect a Cycle in a Linked List:

Write a function to detect if a linked list has a cycle.
Merge Two Sorted Lists:

Write a function to merge two sorted linked lists into a single sorted list.
Python for Automation Testing
Basic Selenium WebDriver Actions:

Write a script to open a browser, navigate to a website, and perform basic actions like clicking a button.
Handle Dynamic Web Elements with Selenium:

Write code to interact with dynamic web elements using explicit waits in Selenium.
Data-Driven Testing Using CSV:

Implement data-driven testing by reading test data from a CSV file.
Take a Screenshot with Selenium:

Write a script to capture and save screenshots of a webpage using Selenium.
Automate Form Submission:

Write a Selenium script to fill out and submit a form on a webpage.
Handle Alerts and Popups with Selenium:

Write code to handle JavaScript alerts, prompts, and confirmation dialogs using Selenium.
Extract Data from Web Tables:

Write a script to extract data from web tables and print or save it.
Use Selenium with Headless Browsers:

Write a script to run Selenium tests in a headless browser environment.
Perform Basic Web Scraping:

Use BeautifulSoup with Selenium to scrape data from a webpage.
Manage Browser Cookies with Selenium:

Write a script to manage and manipulate browser cookies using Selenium.
Verify Page Titles and Content:

Write a script to verify the page title and specific content on a webpage.
Handle Multiple Browser Windows/Tabs:

Write code to switch between multiple browser windows or tabs using Selenium.
Run Tests in Parallel:

Implement parallel test execution using Selenium Grid or similar tools.
Automate Login and Logout Processes:

Write a script to automate user login and logout processes on a website.
Use JavaScript with Selenium:

Execute JavaScript code on a webpage using Selenium’s execute_script method.
Testing and Debugging
Unit Test with unittest:

Write a unit test for a function using the unittest framework.
Mocking with unittest.mock:

Use unittest.mock to mock objects and methods in your tests.
Parameterized Tests with pytest:

Write parameterized tests using the pytest framework to run tests with multiple sets of data.
Test Assertions:

Write assertions to verify expected results in your tests.
Test Fixtures with pytest:

Use fixtures in pytest to set up and tear down test environments.
Debugging with pdb:

Use the pdb module to debug and step through your Python code.
Test Reporting:

Implement test reporting to generate reports in formats like HTML or XML.
Test Case Prioritization:

Write code to prioritize and manage test cases based on various criteria.
Handling Test Data:

Write a script to manage test data and ensure it is correctly set up before tests.
Continuous Integration for Testing:

Set up a CI pipeline (e.g., Jenkins, GitHub Actions) to automate test execution and reporting.
Intermediate and Advanced Python Topics
Context Manager:

Implement a custom context manager using the __enter__ and __exit__ methods.
Custom Exception Handling:

Define and use a custom exception class in your code.
Decorators:

Write a decorator function that modifies the behavior of another function.
Generators and Yield:

Create a generator function that uses yield to produce a sequence of values.
Asynchronous Programming with asyncio:

Write an asynchronous function using asyncio to perform non-blocking operations.
Coroutines:

Implement coroutines in Python and use await to handle asynchronous tasks.
Threading and Multiprocessing:

Write code to perform concurrent operations using threading or multiprocessing.
**Data Manipulation with pandas



**

Continue generating



"""














