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

