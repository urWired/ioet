# ioet interview problem

## Problem statement

The goal of this exercise is to determine whether a pair of employees coincide at the office by processing data corresponding to their workdays. A '.txt' record is given as input. 
---

## Requirements 

- Python 3.9+
- Cloning repo
---

## Usage

- After cloning project, cd into directory
- Open a terminal session
- Then:
``` python
python main.py [file path] 
```
---

## Approach 

The solution is developed using Object-Oriented programming paradigm with Python, taking advantage that it is an object oriented language and for it's readibility.
The solution is composed of two classes and one function's module.
Next, I describe each of the files in a constructive order with the purpose of building understanding of the whole program:

1. processingData.py: This file contains functions that are used to read, process and store in a dictionary the data parsed from a given file passed through the terminal/console. It contains a function that returns a dictionary that is subsequently used in the next class.
2. scheduleMatrix.py: This class receives the dictionary obtained in the previous step as an argument to instatiate it. Also, it initializes the next attributes:
   - list of days, where each value is conformed by the first two capitalized letters of a day.
   - list with the names of the employees, which is obtained from the dictionary.
   - an attribute that invokes a private method.

    I chose this representation because of different factors:
        1. I wanted to have a visual representation of the data in a tabular way, which is a good approach when working with tabular data.
        2. Take advantage of asymptotic time when trying to access the data with indexes.
        3. Although it is necessary to have a contiguous amount of space in memory when storing arrays or matrixes, I assumed that the amount of data is not a concern at the moment.

    - An illustration of the implemented data structure for clarification:
    
    ![matrix](https://user-images.githubusercontent.com/29549000/163325909-12b68cd5-837f-4f3e-9fc7-1da05e415e47.png)


