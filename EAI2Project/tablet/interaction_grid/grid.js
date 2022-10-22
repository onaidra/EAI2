var lastClicked;
var selected = [];
var find = false;
var grid = clickableGrid(30,30,function(el,row,col,i){
    console.log("You clicked on element:",el);
    console.log("You clicked on row:",row);
    console.log("You clicked on col:",col);
    console.log("You clicked on item #:",i);
    // writing element on file:
    let header = document.querySelector("h1");
    header.innerHTML = row+','+col;
    
    
    for (var k =0;k<selected.length;k++){
        if (row==selected[k][1] && col==selected[k][2]){
            selected[k][0].className='';
            selected.splice(k,1);
            find=true;
        }
    }
    if(find==false) selected.push([el,row,col]);
    
    //if (lastClicked) lastClicked.className='';
    
});

document.body.appendChild(grid);
     
function clickableGrid( rows, cols, callback ){
    var i=0;
    var grid = document.createElement('table');
    grid.className = 'grid';
    for (var r=0;r<rows;++r){
        var tr = grid.appendChild(document.createElement('tr'));
        for (var c=0;c<cols;++c){
            var cell = tr.appendChild(document.createElement('td'));
            //cell.innerHTML = ++i;
            cell.addEventListener('click',(function(el,r,c,i){
                return function(){
                    callback(el,r,c,i);
                }
            })(cell,r,c,i),false);
        }
    }
    
    return grid;
    
}

