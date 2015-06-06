# bulbul
Bulbul: A fat-free Python3 to Javascript/ES6 compiler attempt. ![alt tag](https://raw.githubusercontent.com/ahmedaliadeel/bulbul/master/_website/bulbul.png)

Introduction
==============
Bulbul is a Python3 like language.

This is an experimental project not currently ready for production use. Bulbul is a very simple compiler, as long as its valid python3 like syntax it will work. The current code miss several python constructs but the examples really work.

Mission
=======
The aim of this project is to provide best support for AngularJS both 1.X and 2.X series, React 0.13 (ES6) and Aurelia and some other essential javascript stack libraries (basically to rule the world).

Buil Instructions
=================

Command: bulbul.py [inputpython.py] > [output.js]

Just run this command on example python files.

Examples
========

Convert this AngularJs 1.4 python code
```python

def main_controller():
    
    todoList = this
    todoList.todos = [
      {'text':'learn angular', 'done':True},
      {'text':'build an angular app', 'done':False}]
    
    def  addTodo():
        todoList.todos.push({'text':todoList.todoText, 'done':False})
        todoList.todoText = ''
    todoList.addTodo = addTodo
    
    def remaining():
        count = todoList.todos.reduce(lambda p,c :  p+(1 if c.done == True else 0), 0)
        return count
    todoList.remaining = remaining
    
    def archive():
        todoList.todos.length = 0
    todoList.archive = archive    
  
      
angular.module('todoApp', []).controller('TodoListController', main_controller)
 
```
