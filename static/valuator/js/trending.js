window.addEventListener("load", (event) => {
    console.log("page is fully loaded");
    document.querySelector('.mySpinnerDiv').classList.add('hidden')
    document.querySelector('.section-formatting').classList.toggle('hidden')
  });

  // onclick
    // hide main-div
    // unhide spinner

document.querySelector('.aTagCard').addEventListener('click', exiting)

function exiting() {
    document.querySelector('.mySpinnerDiv').classList.toggle('hidden')
    document.querySelector('.section-formatting').classList.toggle('hidden')
}