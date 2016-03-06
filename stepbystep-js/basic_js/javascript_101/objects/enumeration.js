/**
 * Created by patrick on 15/9/2.
 */
var fruit = {
        apple: 2,
        orange:5,
        pear:1
    },
    sentence = 'I have ',
    quantity;
for (kind in fruit){
    console.log(kind);
    quantity = fruit[kind];
    sentence += quantity+' '+kind+
        (quantity===1?'':'s')+
        ', ';
}
// The following line removes the trailing coma.
sentence = sentence.substr(0,sentence.length-2)+'.';
// I have 2 apples, 5 oranges, 1 pear.
console.log(sentence)