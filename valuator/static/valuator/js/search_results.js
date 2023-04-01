window.addEventListener("load", (event) => {
    console.log("page is fully loaded");
    document.querySelector('.mySpinnerDiv').classList.add('hidden')
    document.querySelector('.section-formatting').classList.toggle('hidden')
  });

  // onclick
    // hide main-div
    // unhide spinner

document.querySelector('.link-button').addEventListener('click', exiting)

function exiting() {
    console.log('exiting')
    document.querySelector('.mySpinnerDiv').classList.remove('hidden')
    document.querySelector('.section-formatting').classList.add('hidden')
}