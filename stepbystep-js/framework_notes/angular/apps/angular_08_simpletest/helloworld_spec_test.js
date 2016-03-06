/**
 * Created by patrick on 15/7/18.
 */
describe('hello world test',function(){
  var greeter;
  beforeEach(function(){
    greeter = new Greeter();
  });
  it('should say hello to the world',function(){
    expect(greeter.say('World')).toEqual('Hello,World!');
  })
});
