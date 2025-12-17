console.log("Script loaded successfully.");

const images = [
  "/static/images/snow/00.png",
  "/static/images/snow/01.png",
  "/static/images/snow/02.png",
  "/static/images/snow/03.png",
  "/static/images/snow/04.png",
  "/static/images/snow/05.png",
  "/static/images/snow/06.png",
  "/static/images/snow/07.png",
  "/static/images/snow/08.png"
];
const OPACITY_LEVELS = [0.3, 0.5, 0.7, 0.9];
const svg = document.getElementById("snow");
const flakes = [];
const NUM_OF_FLAKES = 80;

function getRandomImage() {
  return images[Math.floor(Math.random() * images.length)];
}

function getRandomOpcityLevels(){
  return OPACITY_LEVELS[Math.floor(Math.random()*OPACITY_LEVELS.length)];
}

function setSVGViewBox() {
  svg.setAttribute("viewBox", `0 0 ${window.innerWidth} ${window.innerHeight}`);
}
setSVGViewBox();
window.addEventListener("resize", setSVGViewBox);

// create snowflakes
for (let i = 0; i < NUM_OF_FLAKES; i++) {
  const flake = document.createElementNS(
    "http://www.w3.org/2000/svg",
    "image"
  );

  const size = Math.random() * 20 + 10;

  const f = {
    el: flake,
    x: Math.random() * window.innerWidth,
    y: Math.random() * window.innerHeight,
    size: size,
    speed: 0.2
};

  flake.setAttribute("href", getRandomImage());
  flake.setAttribute("x", f.x);
  flake.setAttribute("y", f.y);
  flake.setAttribute("width", f.size);
  flake.setAttribute("height", f.size);
  flake.setAttribute("opacity", getRandomOpcityLevels());

  svg.appendChild(flake);
  flakes.push(f);
}

// animate snowflakes
function animate() {
  flakes.forEach(f => {
    f.y += f.speed;
    f.x += Math.sin(f.y / 50) * 0.5;

    if (f.y > window.innerHeight) {
      f.y = -f.size;
      f.x = Math.random() * window.innerWidth;
    }

    f.el.setAttribute("x", f.x);
    f.el.setAttribute("y", f.y);
  });

  requestAnimationFrame(animate);
}

animate();



