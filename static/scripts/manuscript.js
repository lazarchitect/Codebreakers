var waitingUsers = ["Eddie", "Sean", "Chris", "Mike"];


function fillWaitingRoom(){

    var waitingRoom = document.getElementById("waitingRoom");

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
        line.setAttribute("class", "openGame");
        var anchor = document.createElement("a");
        anchor.setAttribute("href", "google.com");
        anchor.innerText = waitingUsers[i];

        line.appendChild(anchor);

        waitingRoom.appendChild(line);

    }
}
