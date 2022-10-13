var figures  = ['&#9827', '&#9829', '&#9824', 
                     '&#9830', '&#9998', '&#10004', 
                     '&#9650;', '&#9724', '&#9827',
                     '&#9829', '&#9824', '&#9830', 
                     '&#9998', '&#10004', '&#9650;','&#9724'];

function shuffle(a) {
    var currentIndex = a.length;
    var temporaryValue, randomIndex;
  
    while (currentIndex !== 0) {
      randomIndex = Math.floor(Math.random() * currentIndex);
      currentIndex -= 1;
      temporaryValue = a[currentIndex];
      a[currentIndex] = a[randomIndex];
      a[randomIndex] = temporaryValue;
    }
    return a;
  }
  var interval;
    
  function startTimer(){
    var s = 0, m = 0,  h = 0;
    interval = setInterval(function(){
    timer.innerHTML = 'Time: ' + m + " min " + s + " sec";
      s++;
      if(s == 60){
        m++;
        s = 0;
      }
      if(m == 60){
        h++;
        m = 0;
      }
    },1000);
  }
  function startGame(){  

    var array = shuffle(figures);
  
    clearInterval(interval);
    compare = [];
  
    var lista = document.getElementById('griglia');
    while (lista.hasChildNodes()) {  
      lista.removeChild(lista.firstChild);
    }
  
     for(var i = 0; i < 16; i++){    
        var box = document.createElement('div');
        var element = document.createElement('div');
        element.className = 'icon';
        element.id = i;
        document.getElementById('griglia')
           .appendChild(box).appendChild(element);
        element.innerHTML = array[i];
      }
    
    startTimer();
  
    var icon = document.getElementsByClassName("icon");
    var icons = [...icon];
  
    for (var i = 0; i < icons.length; i++){
      icons[i].addEventListener("click", displayIcon);
      icons[i].addEventListener("click", openModal);
    }
  
  }
  document.body.onload = startGame();
  
  function displayIcon(){

    var iconsFind = document.getElementsByClassName("find");
  
    var icon = document.getElementsByClassName("icon");
    var icons = [...icon];
  
    this.classList.toggle("show");
    compare.push(this);

    var len = compare.length;
    if(len === 2){
      if(compare[0].innerHTML === compare[1].innerHTML ){
        if(compare[0].id !== compare[1].id){

          compare.forEach(function(elemento){
            elemento.classList.add("find","disabled");
        });
        }

        compare = [];               
      } else {
        icons.forEach(function(item){
          item.classList.add('disabled');
        });
        setTimeout(function(){
          compare.forEach(function(elemento){
              elemento.classList.remove("show");
          });
          icons.forEach(function(item){
            item.classList.remove('disabled');
            for(var i = 0; i < iconsFind.length; i++){
                iconsFind[i].classList.add("disabled");
              }
          });
          compare = [];
        },700); 
       }
    }
  }
  
  var modal = document.getElementById("modal");
  var timer = document.querySelector(".timer");
    
  function openModal(){  
    var iconsFind = document.getElementsByClassName("find");
    if (iconsFind.length == 16){
        clearInterval(interval);
        modal.classList.add("active");
        document.getElementById("totalTime").innerHTML = timer.innerHTML.substring(6,);
    }
  }
  

  function playAgain(){
    modal.classList.remove("active");
    startGame();
  }
          