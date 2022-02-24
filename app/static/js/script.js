// get responses in json
let form = document.querySelector("#user-text-form");

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
	// add message user
	const parent = document.querySelector("ul");
	const user = document.createElement("p");
	user.id = "messageUser";
	user.classList.add("messageUser");
	parent.appendChild(user);
	let messageUser = user;
	messageUser.innerHTML = submit
}

function displayMessageRobo(mess) {
	// add message robot
	const parent = document.querySelector("ul");
	const robo = document.createElement("p");
	robo.id = "messageRobo";
	robo.classList.add("messageRobo");
	parent.appendChild(robo);
	let messageRobo = robo;
	messageRobo.innerHTML = mess
}

function displayWiki(extract) {
	// add wiki element
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

	// create class map
	maploc.id = "map";
	maploc.classList.add("map");
	parent.appendChild(maploc);

	// create and display image
	const img = document.createElement("img");
	img.src = "static/img/loader.gif";
	maploc.appendChild(img);
	img.className += "loader";
	maploc.classList.add("loader");
	
	// hide the loader when the map is displayed 
	var state = document.readyState;
	if (state == 'complete') {
		setTimeout(function(){
			img.className += ' hidden';
		},1000);
	}

    // Initialize the platform object
    var platform = new H.service.Platform({
		apikey: "ao5DPDJ3gGJCMBY8-Rwg_7FJBqRo4iAlKRtHAGl1hxY"
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
