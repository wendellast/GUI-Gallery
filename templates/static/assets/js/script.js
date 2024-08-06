var images = document.querySelector(".wrapper");


var isTouch = false;
var prevX = 50;
var prevY = 60;
var currentX = images.offsetWidth / -2;
var currentY = images.offsetHeight / -2;

var currentXtmp = 0;
var currentYtmp = 0;

var images = document.querySelector(".images");

var isDown = false;
var startX;
var scrollLeft;


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




