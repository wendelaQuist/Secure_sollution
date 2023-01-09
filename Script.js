const dropArea = document.querySelector(".drag-area");

let file;

dropArea.addEventListener("dragover", (event)=>{
  event.preventDefault();
});

dropArea.addEventListener("dragleave", ()=>{
  dropArea.classList.remove("active");
  console.log("It works");
});

dropArea.addEventListener("drop", (event)=>{
  event.preventDefault();
  console.log("It works again");
});

