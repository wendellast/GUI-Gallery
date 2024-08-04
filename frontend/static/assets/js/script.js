var images = document.querySelector(".images");

var isDown = false;
var isTouch = false;
var prevX = 0;
var prevY = 0;
var currentX = images.offsetWidth / -2;
var currentY = images.offsetHeight / -2;

var currentXtmp = 0;
var currentYtmp = 0;

var ondown = (e) => {
    prevX = e.clientX;
    prevY = e.clientY;
    isDown = true;
}

var onmove = (e) => {
    if (!isDown) return;

    var deltaX = 
        Math.min(Math.max(e.clientX - prevX + 
            currentX, -images.offsetWidth), 0);

    var deltaY = 
        Math.min(Math.max(e.clientY - prevY + 
            currentY, -images.offsetHeight), 0);

    currentXtmp = deltaX;
    currentYtmp = deltaY;

    images.animate({
        transform: `translate(${deltaX}px, ${deltaY}px)`,
    }, { duration: isTouch ? 0 : 800, fill: "forwards"})
}

var onup = (e) => {
    currentX = currentXtmp;
    currentY = currentYtmp;
    isDown = false;
}

this.onmousedown = ondown;
this.onmousemove = onmove;
this.onmouseup = onup;

var images = document.querySelector(".images");

var isDown = false;
var startX;
var scrollLeft;

images.addEventListener('mousedown', function(e) {
    isDown = true;
    startX = e.pageX - images.offsetLeft;
    scrollLeft = images.scrollLeft;
});

images.addEventListener('mouseleave', function() {
    isDown = false;
});

images.addEventListener('mouseup', function() {
    isDown = false;
});

images.addEventListener('mousemove', function(e) {
    if(!isDown) return;
    e.preventDefault();
    var x = e.pageX - images.offsetLeft;
    var walk = (x - startX) * 3; // Adjust scrolling speed here
    images.scrollLeft = scrollLeft - walk;
});


const musicContainer = document.getElementById("music-container");
const playButton = document.getElementById("play");
const prevButton = document.getElementById("prev");
const nextButton = document.getElementById("next");
const audio = document.getElementById("audio");
const progress = document.getElementById("progress");
const progressContainer = document.getElementById("progress-container");
const title = document.getElementById("title");
const cover = document.getElementById("cover");

const songs = ["stellar", "Fall-down"];
let songIndex = 1;

function getSongTitle(song) {
  return song.charAt(0).toUpperCase() + song.slice(1);
}

function loadSong(song) {
  title.innerText = getSongTitle(song);
  audio.src = `https://github.com/wendellast/GUI-Gallery/blob/main/static/assets/music/${song}.mp3?raw=true`;
  cover.src = `https://github.com/wendellast/GUI-Gallery/blob/main/static/assets/img/${song}.jpg?raw=true`;
}

function playSong() {
  musicContainer.classList.add("play");
  playButton.querySelector("i.fas").classList.remove("fa-play");
  playButton.querySelector("i.fas").classList.add("fa-pause");
  audio.play();
}

function pauseSong() {
  musicContainer.classList.remove("play");
  playButton.querySelector("i.fas").classList.remove("fa-pause");
  playButton.querySelector("i.fas").classList.add("fa-play");
  audio.pause();
}

function prevSong() {
  songIndex--;
  if (songIndex < 0) songIndex = songs.length - 1;
  loadSong(songs[songIndex]);
  playSong();
}

function nextSong() {
  songIndex++;
  if (songIndex > songs.length - 1) songIndex = 0;
  loadSong(songs[songIndex]);
  playSong();
}

function updateProgress(e) {
  const { duration, currentTime } = e.srcElement;
  const progressPercent = (currentTime / duration) * 100;
  progress.style.width = `${progressPercent}%`;
}

function setProgress(e) {
  const width = this.clientWidth;
  const clickX = e.offsetX;
  const duration = audio.duration;
  audio.currentTime = (clickX / width) * duration;
}

// Event Listeners
playButton.addEventListener("click", () => {
  const isPlaying = musicContainer.classList.contains("play");
  isPlaying ? pauseSong() : playSong();
});

prevButton.addEventListener("click", prevSong);
nextButton.addEventListener("click", nextSong);

audio.addEventListener("timeupdate", updateProgress);
progressContainer.addEventListener("click", setProgress);

audio.addEventListener("ended", nextSong);

// Init
loadSong(songs[songIndex]);