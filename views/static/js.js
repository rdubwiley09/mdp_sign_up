$(document).ready(function(){
  $("#nav-button").on('click',function(){
    $("#dropdown").toggleClass("show");
  });
  if($("#event-data").attr("data")!="None"){
    $("#event").val($("#event-data").attr("data"));
  }
  var pathname = window.location.pathname;
  $("#form").attr("action", pathname)
});
