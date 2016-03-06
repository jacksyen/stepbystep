/**
 * Created by patrick on 15/7/14.
 */
(function(){
  function manu(){
    document.getElementById('main1').onclick()
  };
  function showToday(){
    var today = new Date();
    alert(today);
  }

  var e = document.getElementById('button');
  e.addEventListener('click',manu,true);

  //e.removeEventListener();
})();


