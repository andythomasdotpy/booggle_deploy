// function showLoaderOnClick(url) {
//     showLoader();
//     window.location=url;
// }
// function showLoader(){
//     $('body').append('<div style="" id="loadingDiv"><div class="loader">Loading...</div></div>');
// }

window.addEventListener("load", (event) => {
    console.log("page is fully loaded");
    document.querySelector('.mySpinnerDiv').classList.add('hidden')
    document.querySelector('.section-formatting').classList.toggle('hidden')
  });

document.querySelector('.aTagButtonDiv').addEventListener('click', error)

function error() {
    const errorMsg = "Sorry, that functionality is currently under construction"

    document.querySelector(".errorMsg").innerText = errorMsg


    const showMessage = setTimeout(myMessage, 1500)
    function myMessage() {
        document.querySelector(".errorMsg").innerText = ""
    }
}