document.querySelector('.search-button').addEventListener('click', exiting)

function exiting() {
    console.log("Testing")
    document.querySelector('.mySpinnerDiv').classList.remove('hidden')
    document.querySelector('.form-div').classList.add('hidden')
}