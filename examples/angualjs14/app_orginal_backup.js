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
function runon()  { 
   alert("yelllow")
}
jQuery(document).ready(runon)
