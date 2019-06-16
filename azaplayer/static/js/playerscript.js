function loadSong(elt, e) {
	if(!e) var e = window.event;
	document.getElementById("player").src=elt.href;
	document.getElementById("player").load();
	document.getElementById("player").play();
	return false;
}
window.onload = function() {
	links = document.getElementById("playlist").getElementsByTagName("a");
	for(var i = 0; i<links.length; i++) {
		links[i].onclick=function(e) { return loadSong(this, e); };
	}
}