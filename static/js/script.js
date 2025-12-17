console.log("Script loaded successfully.");

const svg = document.getElementById("snow");
const flakes = [];
const NUM_OF_FLAKES = 80;

function setSVGViewBox(){
    svg.setAttribute("viewBox", `0 0 ${window.innerWidth} ${window.innerHeight}`);
}
setSVGViewBox();
window.addEventListener("resize", setSVGViewBox);

//create snowflakes
for(let i = 0; i < NUM_OF_FLAKES; i++){
    const flake = document.createElementNS("http://www.w3.org/2000/svg", "circle");
  const f = {
    el: flake,
    x: Math.random() * window.innerWidth,
    y: Math.random() * window.innerHeight,
    r: Math.random() * 5 + 2,  
    speed: Math.random() * 2 + 0.5
  };
  flake.setAttribute("cx", f.x);
  flake.setAttribute("cy", f.y);
  flake.setAttribute("r", f.r);
  flake.setAttribute("fill", "white");
  svg.appendChild(flake);
  flakes.push(f);
}

//animate snowflakes
function animate(){
    flakes.forEach(f => {
    f.y += f.speed;
    f.x += Math.sin(f.y / 50) * 0.5;

    if (f.y > window.innerHeight) {
      f.y = -10;                   
      f.x = Math.random() * window.innerWidth; 
    }

    f.el.setAttribute("cx", f.x);
    f.el.setAttribute("cy", f.y);
  });
  requestAnimationFrame(animate);
}

animate();


