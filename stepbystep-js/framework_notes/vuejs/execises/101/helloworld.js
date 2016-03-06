/**
 * Created by patrick on 16/2/4.
 */
var vm = new Vue({
    el: '#helloworld',
    data: {
        message:'this is testing',
        newTodo:{},
        checked:false,
        checkedNames:[],
        selected:'A',
        toggle:'',
        picked:'',
        todos: [
            { text: 'Learn JavaScript' },
            { text: 'Learn Vue.js' },
            { text: 'Build Something Awesome' }
        ],
        options: [
            { text: 'One', value: 'A' },
            { text: 'Two', value: 'B' },
            { text: 'Three', value: 'C' }
        ]
    },
    methods:{
        reverseMessage: function(){
            console.log(this.message);
            this.message = this.message.split('').reverse().join('')
        },
        removeTodo: function(index){
            this.todos.splice(index,1);
        },
        addTodo:function(){
            if(this.newTodo.text){
                this.todos.push(this.newTodo);
                this.newTodo='';
            }
        }
    }
});