/**
 * Created by patrick on 15/11/11.
 */
new Vue({
    el: '#todo',
    data: {
        newTodo: '',
        todos: [
            {text:"test"},
            {text:"test1"},
            {text:"test2"}
        ]
    },
    methods: {
        addTodo: function(){
            var text = this.newTodo.trim();
            if(text){
                this.todos.push({text:text});
                this.newTodo=''
            }
        },
        removeTodo: function(index){
            this.todos.splice(index,1);
        }
    }
});