document.getElementById('chart').innerHTML = '';

let bar = document.createElement('div');
bar.className = 'bar';
bar.style.height = '83px';
bar.style.backgroundColor = '#005F73';
document.getElementById('chart').appendChild(bar);

function showSix() {

            var element = document.getElementById("info");
             
            if(element.style.visibility == "hidden"){
                element.style.visibility = "visible";
            } 

            else {
                element.style.visibility = "hidden";
            }   
        }
