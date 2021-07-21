function playName(form){
	//declares variables for the input name and for the voice version selected
	var name = document.getElementById('name').value
	var vcheck = document.getElementById('voice_1').checked
	
	//if voice 1 was chosen, plays Nikhil's recordings, if not, plays Varun's
	if (vcheck) {
		avers = '-1.m4a';
	} else {
		avers = '-3.m4a';
	}
	
	//calls and plays the corresponding audio recording
	var audiopath = './recordings/' + name + avers;
	const nameaudio = new Audio(audiopath);
	return nameaudio.play();
}
	