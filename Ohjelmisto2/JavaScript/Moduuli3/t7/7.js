 let kuva = document.getElementById('target')
document.getElementById('trigger').onmouseover=function(){
   kuva.src="img/picB.jpg";
};
document.getElementById('trigger').onmouseout=function(){
   kuva.src="img/picA.jpg";
};