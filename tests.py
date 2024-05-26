<html>
 <head>
  <title>Spele</title>
 </head>

 <body>
  <canvas id=myCanvas width=600 height=600 style="background-color: rgb(43, 45, 78);">
 </canvas>

<script>
    var ctx = myCanvas.getContext("2d");

    var x = 100;             
    var y = 100;

    var vx = 5;              
    var vy = 5;

    var gravity = 0.70;      

    var box_width = 30;
var box_height = 10;            
var box_margin = 5;
var boxes_per_row = 1;
var num_boxes = 1;
var box_visible = []; 

    var MyImg = new Image();
    MyImg.src = "https://s2js.com/img/etc/bat.png";
 
    function MyDraw () {
       ctx.clearRect(0,0,600,600);       
       x = x + vx;                       
       y = y + vy;                          
                       
       if (y + MyImg.height >= myCanvas.height) {              
                overrun = y + MyImg.height - myCanvas.height; 
                y = y - overrun;                               
                vy = vy - (overrun / vy * gravity);            
                vy = Math.abs(vy) * -0.8   ;                   
                vx = vx * 0.8;                                 
                } 
           else vy = vy + gravity;                                

 
       if (x + MyImg.width > myCanvas.width) vx = Math.abs(vx) * -1;  
       if (x < 0) vx = Math.abs(vx);                                  

       ctx.drawImage(MyImg, x, y);  
       }


  function mypress (event) {
     vy= vy-15;                   
     }

  window.addEventListener('keypress', mypress, false);

  setInterval(MyDraw, 30);  


</script> 
 
 </body>
</html>
