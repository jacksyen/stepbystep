/**
 * Created by patrick on 15/12/27.
 */
try {
    var foo = 'hehe';
    throw new Error('just throw.');
} catch (ex) {
    console.log(foo);
}
