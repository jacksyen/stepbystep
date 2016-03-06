/**
 * Created by patrick on 15/11/11.
 */
new Vue({
    el: '#testresult',
    data: {
        testsuites: [
            {name:"Name1",cases:100,isPass:true,passed:100,failed:10,testCases:[{
                name: "test1",
                isPass: true,
                logs:["testlogging1","testlog2"],
                images:["add_1.jpg"]
            }]},
            {name:"Name2",cases:100,isPass:true,passed:100,failed:10,testCases:[{
                name: "test2",
                isPass: true,
                logs:["testlogging1","testlog2"],
                images:["add_1.jpg","add_2.jpg"]
            },{
                name: "test3",
                isPass: false,
                logs:["testlogging1","testlog2"],
                images:["add_1.jpg"]
            }]},
            {name:"Name3",cases:100,isPass: true ,passed:100,failed:10,testCases:[{
                name: "test3",
                isPass: false,
                logs:["testlogging1","testlog2"],
                images:["add_1.jpg","add_2.jpg","add_3.jpg","add_4.jpg"]
            }]},
            {name:"Name4",cases:100,isPass: true ,passed:100,failed:10,testCases:[{
                name: "test3",
                isPass: false,
                logs:["testlogging1","testlog2"],
                images:["add_1.jpg","add_2.jpg","add_3.jpg","add_4.jpg"]
            }]}
        ],
    },
    methods: {
    }
});