function run(){
  "use strict"

  let b = document.querySelector(".copy");
  b.addEventListener("click", () => {
    let c = document.querySelector(".input");
    c.select();
    document.execCommand("copy")
  })

  }
   run()
