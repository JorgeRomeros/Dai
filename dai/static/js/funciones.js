$.ajax({
    url: base_url + 'marcaadd',
    dataType: "html",
    method: "GET",
    success: function(data){
        $("#marcaadd").html(data);
    }
  });

$.ajax({
    url: base_url + 'modeloadd',
    dataType: "html",
    method: "GET",
    success: function(data){
        $("#modeloadd").html(data);
    }
  });  
  