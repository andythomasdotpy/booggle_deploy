window.addEventListener("load", (event) => {
    console.log("page is fully loaded");
    document.querySelector('.mySpinnerDiv').classList.add('hidden')
    document.querySelector('.section-formatting').classList.toggle('hidden')
  });

  // onclick
    // hide main-div
    // unhide spinner

// document.querySelector('.trendingCard').addEventListener('click', exiting)
const cards = document.querySelectorAll('#aTagCard')
for (let i = 0; i < cards.length; i++) {
    console.log(cards[i]);
}

// document.querySelectorAll("#aTagCard").forEach(el => el.addEventListener("click", exiting));
Array.from(cards).forEach(element => element.addEventListener('click', exiting))


function exiting() {
    console.log("Testing")
    document.querySelector('.mySpinnerDiv').classList.remove('hidden')
    document.querySelector('.section-formatting').classList.add('hidden')
}