function zoom(e) {
  const zoomer = e.currentTarget;
  let offsetX, offsetY;

  if (e.offsetX) {
    offsetX = e.offsetX;
    offsetY = e.offsetY;
  } else {
    offsetX = e.touches[0].pageX;
    offsetY = e.touches[0].pageY;
  }

  const x = (offsetX / zoomer.offsetWidth) * 100;
  const y = (offsetY / zoomer.offsetHeight) * 100;

  zoomer.style.backgroundPosition = `${x}% ${y}%`;
}
