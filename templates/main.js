document.addEventListener("DOMContentLoaded", () => {
  const container = document.getElementById("image-container");

  if (imageData && imageData.length > 0) {
    imageData.forEach(url => {
      const zoomDiv = document.createElement("div");
      zoomDiv.className = "zoom";
      zoomDiv.style.backgroundImage = `url(${url})`;
      zoomDiv.addEventListener("mousemove", zoom);
      zoomDiv.addEventListener("touchmove", zoom);
      container.appendChild(zoomDiv);
    });
  }
});
