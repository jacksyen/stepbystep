/**
 * Created by patrick on 15/7/18.
 */
describe('archive service testing',function(){
  var notificationsArchive;
  beforeEach(module('archive'));
  beforeEach(inject(function(_notificationsArchive_){
    notificationsArchive=_notificationsArchive_;
  }));
  it('should give access to the archived items',function(){
    var notification={msg:'old message'};
    notificationsArchive.archive(notification);
    notificationsArchive.archive(notification);
    expect(notificationsArchive.getArchived().toContain(notification));
  })
});
