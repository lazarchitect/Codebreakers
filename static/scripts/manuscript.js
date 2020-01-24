

function getWaitingUsers(){
    console.log("attempting to retrieve waiting room");
    var connection = new XMLHttpRequest();
    connection.onreadystatechange = function(){
        if (this.readyState == 4 && this.status == 200) {
            console.log("waiting room successfully retrieved");
            fillWaitingRoom(this.responseText.split(" "));
        }
    }
    connection.open("POST", "/getWaitingRoom");
    connection.send();
}

setInterval(getWaitingUsers, 3000);



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
        anchor.setAttribute("href", "/enterGame");
        // anchor.onclick = enterGame(waitingUsers[i]);
        anchor.innerText = waitingUsers[i];

        line.appendChild(anchor);

        waitingRoom.appendChild(line);

    }
}


function createGame(){
    /*user clicks button. a game object is created, and a new game with the user's name is added to the list globally.
    as for the user, nothing happens??? besides some visual indicator.*/

    var connection = new XMLHttpRequest();
    connection.onreadystatechange = function(){
        if (this.readyState == 4 && this.status == 200) {
            if(this.responseText=="NOPE"){
                alert("You cannot create more than one game. Wait for another player to join your existing game.");
            }
            else{
                fillWaitingRoom(this.responseText.split(" "));
            }
        }
    }
    connection.open("POST", "/addToWaitingRoom");
    connection.send();
}


function enterGame(username){
    console.log("sdfsf");
    // need to check if username param = current session username. which means sending to server 
    // if it is, do nothing.
    // else,
    // create game object and put current player AND that player into game page
    // need to tell server the name so it can reach out to them and redirect
}