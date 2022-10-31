var goalx = 24;
var goaly = 6;
var lastClicked;
var selected = [];
var find = false;

var grid = clickableGrid(31,31,function(el,row,col,i){
   console.log("You clicked on element:",el);
    console.log("You clicked on row:",row);
    console.log("You clicked on col:",col);
    console.log("You clicked on item #:",i);
    // writing element on file:
       
    find=false
    el.className='clicked';
    for (var k =0;k<selected.length;k++){
        if (row==selected[k][1] && col==selected[k][2]){
            selected[k][0].className='';
            selected.splice(k,1);
            find=true;
        }
    }
    if(find==false) selected.push([el,row,col]);
    
    
});

var buttonvar = buttongrid();
document.body.appendChild(buttonvar);
document.body.appendChild(grid);


function buttongrid(){
    var p = document.createElement('p');
    var div = p.appendChild(document.createElement('div'));
    div.setAttribute('id','buttons');
    div.setAttribute('align','center');
    return p;
}
function clickableGrid( rows, cols, callback ){
    var i=0;
    var grid = document.createElement('table');
    grid.className = 'grid';
    for (var r=1;r<rows;++r){
        var tr = grid.appendChild(document.createElement('tr'));
        for (var c=1;c<cols;++c){
            var cell = tr.appendChild(document.createElement('td'));
            if(r==parseInt(goalx) && c==parseInt(goaly)){
                cell.style.backgroundColor = "green";
            }
            else{
                cell.addEventListener('click',(function(el,r,c,i){
                    return function(){
                        callback(el,r,c,i);
                    }
                })(cell,r,c,i),false);
            }

        }
    }
    
    return grid;
    
}

