$(document).ready(function(){

    var socket = new WebSocket(
        'ws://127.0.0.1:8888/ws'
    );
   /*socket..binaryType = "arraybuffer";
   var wsStream = null;
   var client = BinaryClient('ws://192.168.198.163:8000/ws');
   client.on('open', function(){
   	wsStream = client.createStream("audio");

   	wsStream.on('data', function(data){
          	console.log(data);
    	});
    }); 

*/
   socket.onmessage = function (evt) {
       var json = JSON.parse(evt.data);
            $('#video').attr(
                'src',
                'data:image/jpg;base64,' + json.frame
            );
        };

        // Controls
        $('#enable_streamin').click(function() {
            socket.emit('control', 'enable_streamin');
        });

        $('#disable_streamin').click(function() {
            socket.emit('control', 'disable_streamin');
        });
});
/*
  var blob  = new Blob([image],{type: "image/png"});
  var img = new Image();
  img.onload = function (e) {
    console.log("PNG Loaded");
    ctx.drawImage(img, left, top);
    window.URL.revokeObjectURL(img.src);    
    img = null;  
  };

  img.onerror = img.onabort = function () {         
    img = null;
  };
  img.src = window.URL.createObjectURL(blob);
*/
