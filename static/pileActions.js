var pilecounts = {
	"pile1": 0,
	"pile2": 0,
	"pile3": 0,
	"pile4": 0,
};

function startdrag(ev){
	ev.dataTransfer.setData("card", "true");
}

function drop (ev) {
	ev.preventDefault();
	if(ev.dataTransfer.getData("card") !== "true") return;
	ev.target.innerText = ++pilecounts[ev.target.id];
	var color;
	switch(ev.target.id){
		case "pile1": color = "red"; break;
		case "pile2": color = "blue"; break;
		case "pile3": color = "green"; break;
		case "pile4": color = "yellow"; break;
	}

	const Http = new XMLHttpRequest();
	const url = "http://localhost:5000/piledrop"

	Http.open("POST", url);
	Http.send(color);

	Http.onreadystatechange = function(){
		if(Http.readyState === 4) console.log(Http.responseText);
	}

}

function allowdrop(ev){
	ev.preventDefault();
}