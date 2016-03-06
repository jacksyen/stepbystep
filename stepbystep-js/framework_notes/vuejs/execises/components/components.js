/**
 * Created by patrick on 16/2/4.
 */
// 注册子组件
// 将当前消息派发出去
Vue.component('child', {
    template: '#child-template',
    data: function () {
        return { msg: 'hello' }
    },
    methods: {
        notify: function () {
            if (this.msg.trim()) {
                this.$dispatch('child-msg', this.msg) //dispatch the events
                this.msg = ''
            }
        }
    }
});

// 启动父组件
// 将收到消息时将事件推入一个数组
var parent = new Vue({
    el: '#events-example',
    data: {
        messages: []
    },
    // 在创建实例时 `events` 选项简单地调用 `$on`
    events: {
        'child-msg': function (msg) {
            // 事件回调内的 `this` 自动绑定到注册它的实例上
            this.messages.push(msg) //push to parent
        }
    }
});