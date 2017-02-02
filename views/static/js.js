$(document).ready(function(){
  $("#nav-button").on('click',function(){
    $("#dropdown").toggleClass("show");
  });
  if($("#organization-data").attr("data")!="None"){
    $("#organization").val($("#organization-data").attr("data"));
  }
  var pathname = window.location.pathname;
  $("#form").attr("action", pathname)
});
