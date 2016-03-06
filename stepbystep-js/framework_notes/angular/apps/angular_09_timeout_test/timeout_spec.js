/**
 * Created by patrick on 15/7/18.
 */
describe('Async Greeter test',function(){
  var asyncGreeter,$timeout,$log;
  beforeEach(module('async'));
  beforeEach(inject(function(_asyncGreeter_){
    asyncGreeter = _asyncGreeter_;
    $timeout=_$timeout_;
    $log=_$log_;
  }));

  it('should greet the async World',function(){
    asyncGreeter.say ('World',999999999);
    $timeout.flush();
    expect($log.info.logs.toContain(['helloW,World!']));
  });
});
