

function getWaitingUsers(){

    var connection = new XMLHttpRequest();
    connection.onreadystatechange = function(){
        if (this.readyState == 4 && this.status == 200) {
            fillWaitingRoom(this.responseText.split(" "));
        }
    }
    connection.open("POST", "/getWaitingRoom");
    connection.send();
}




function fillWaitingRoom(waitingUsers){

    var waitingRoom = document.getElementById("waitingRoom");
    waitingRoom.innerHTML = "";
    
    if(waitingUsers.length == 0){
        waitingRoom.style.backgroundColor = "white";
        return;
    }

    var i;
    for(i = 0; i < waitingUsers.length; i++){

        var line = document.createElement("div");
        line.setAttribute("class", "openGame");
        if(i%2==0){
            line.style.backgroundColor = "skyblue";
        }
        else{
            line.style.backgroundColor = "white";
        }
        var anchor = document.createElement("a");
        anchor.setAttribute("href", "google.com");
        anchor.innerText = waitingUsers[i];

        line.appendChild(anchor);

        waitingRoom.appendChild(line);

    }
}


function createGame(){
    /*
    user clicks button. a game object is created, and a new game with the user's name is added to the list globally.
    as for the user, nothing happens??? besides some visual indicator.
    
    */

    alert("Game created. Now just wait, when someone joins you will automatically be taken into the game.");

    var connection = new XMLHttpRequest();
    connection.onreadystatechange = function(){
        if (this.readyState == 4 && this.status == 200) {
            fillWaitingRoom(this.responseText.split(" "));
        }
    }
    connection.open("POST", "/addToWaitingRoom");
    connection.send();

}