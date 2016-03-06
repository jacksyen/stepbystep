/**
 * Created by patrick on 15/11/11.
 */
new Vue({
    el: '#todo',
    data: {
        message: 'Hello Vue.js!',
        logs: [
            {result:"test"},
            {result:"test1"},
            {result:"test2"}
        ]
    },
    methods: {
        reverseMessage : function(){
            this.message = this.message.split('').reverse().join('')
        }
    }
});