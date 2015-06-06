
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
 
def runon():
    alert('yelllow')
 
jQuery(document).ready(runon)
