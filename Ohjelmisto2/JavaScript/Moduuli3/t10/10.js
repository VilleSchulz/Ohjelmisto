let form = document.getElementById('source');
let target = document.getElementById('target');
console.log(name)

form.addEventListener("submit", function (evt) {
    evt.preventDefault()
    let firstName = form.elements.firstname.value;
    let lastName = form.elements.lastname.value;
    let fullName = `${firstName} ${lastName}`;
    target.innerText  = fullName;
})