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

Bulbul converts this AngularJs 1.4 python code
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
Into this Javscript ES5 Code
```javascript
function main_controller()  { 
   var todoList = this ;

   todoList.todos = [{"text":"learn angular","done":true},{"text":"build an angular app","done":false}] ;

   function addTodo()  { 
   todoList.todos.push({"text":todoList.todoText,"done":false})

   todoList.todoText = "" ;
}

   todoList.addTodo = addTodo ;

   function remaining()  { 
   var count = todoList.todos.reduce(function (p,c)  { 
  return p+((c.done==true) ? 1:0);
},0) ;

   return count;
}

   todoList.remaining = remaining ;

   function archive()  { 
   todoList.todos.length = 0 ;
}

   todoList.archive = archive ;
}
angular.module("todoApp",[]).controller("TodoListController",main_controller)

```


Bulbul converts this React 0.13.X python code
```python
'use strict'

from react import React 


class HelloWorld(React.Component):
    def render():
        elapsed = this.props.elapsed  / 100.0
        seconds = elapsed / 10.0
        message ='React has been successfully running for ' + seconds + ' seconds.'

        return bb_jsx('<p>{message}</p>')
bb_export('default HelloWorld')      


    
start = Date.now()
setInterval(lambda : React.render(bb_jsx('<HelloWorld elapsed={new Date().getTime() - start} />'), document.getElementById('body') ), 50)

```
Into this ES6 Code
```javascript
"use strict"
import React from 'react';
class HelloWorld { 
render()  { 
   var elapsed = this.props.elapsed/100.0 ;

   var seconds = elapsed/10.0 ;

   var message = "React has been successfully running for "+seconds+" seconds." ;

   return <p>{message}</p>;
}
}
export default HelloWorld;
var start = Date.now() ;
setInterval(function ()  { 
  return React.render(<HelloWorld elapsed={new Date().getTime() - start} />,document.getElementById("body"));
},50)


```
