let form = document.querySelector("#user-text-form");
// get the message from the form 
function postFormData(url, data) {
	return fetch("/robot", {
		method: "POST",
		body: data
	})
	.then(response => response.json())
	.catch(error => console.log(error));
}

form.addEventListener("submit", function (event) {
	event.preventDefault();
	
    // rotates the image element
	let wait = document.getElementById("img");
	wait.style.display ='inline';
	wait.classList.toggle('flip')

    postFormData("/view", new FormData(form))
    .then(response => {
		if(response[3]) {
			const submit = response[0]
			displayMessageUser(submit);
			const mess = response[1]
			displayMessageRobo(mess);	
			const loc = response[2];
			displayMap(loc);
			const extract = response[3]
			displayWiki(extract);
	    }
	    else {
			const submit = response[0]
			displayMessageUser(submit);
			const mess = response[1]
			displayMessageRobo(mess);
	    }
    })
})

function displayMessageUser(submit) {
	// add and display message user
	const parent = document.querySelector("ul");
	const user = document.createElement("p");
	user.id = "messageUser";
	user.classList.add("messageUser");
	parent.appendChild(user);
	let messageUser = user;
	messageUser.innerHTML = submit
}

function displayMessageRobo(mess) {
	// add and display message robot
	const parent = document.querySelector("ul");
	const robo = document.createElement("p");
	robo.id = "messageRobo";
	robo.classList.add("messageRobo");
	parent.appendChild(robo);
	let messageRobo = robo;
	messageRobo.innerHTML = mess
}

function displayWiki(extract) {
	// add and display wiki element
	const parent = document.querySelector("ul");
	const wikextract = document.createElement("p");
	wikextract.id = "wiki";
	wikextract.classList.add("wiki");
	parent.appendChild(wikextract);
	let wiki = wikextract;
	wiki.innerHTML = extract
}

function displayMap(loc) {
    // create element div
	const parent = document.querySelector("ul");
	const maploc = document.createElement("div");
	maploc.id = "map";
	maploc.classList.add("map");
	parent.appendChild(maploc);

    // Initialize the platform object
    var platform = new H.service.Platform({
		apikey: "apikey"
		});
	   
	// Obtain the default map types from the platform object   
	var defaultLayers = platform.createDefaultLayers();
	// Instantiate (and display) a map object
	var map = new H.Map(
		maploc,
		defaultLayers.vector.normal.map,
		{
		  zoom: 16,
		  center: loc,
		});
    // add a resize listener to make sure that the map occupies the whole container
    window.addEventListener("resize", () => map.getViewPort().resize());

	const marker = new H.map.Marker(loc);
	map.addObject(marker);
}
