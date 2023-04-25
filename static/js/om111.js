console.log("project4");
const fname = document.getElementById('fname');
const lname = document.getElementById('lname');
const fathername = document.getElementById('fathername');
const email = document.getElementById('email');
const phone = document.getElementById('phone');
let validFname = false;
let validLname = false;
let validFatherName = false;
let validEmail = false;
let validPhone = false;
$('#failure').hide();
$('#success').hide();
// 111
fname.addEventListener('blur', () => {
    let regex = /^[a-z A-Z]([ A-Z a-z]){1,20}$/;
    let str = fname.value;
    console.log(regex, str);

    if (regex.test(str)) {
        console.log('Your name is valid');
        fname.classList.remove('is-invalid');
        validFname = true;
    }
    else {
        console.log("Your name is not valid");
        fname.classList.add('is-invalid');
        validFname = false;
    }
})
// 222
lname.addEventListener('blur', () => {
    let regex = /^[a-z A-Z]([ A-Z a-z]){1,10}$/;
    let str = lname.value;
    console.log(regex, str);

    if (regex.test(str)) {
        console.log('Your name is valid');
        lname.classList.remove('is-invalid');
        validLname = true;
    }
    else {
        console.log("Your name is not valid");
        lname.classList.add('is-invalid');
        validLname = false;
    }
})
// 3333
fathername.addEventListener('blur', () => {
    let regex = /^[a-z A-Z]([ A-Z a-z]){1,20}$/;
    let str = fathername.value;
    console.log(regex, str);

    if (regex.test(str)) {
        console.log('Your name is valid');
        fathername.classList.remove('is-invalid');
        validFatherName = true;
    }
    else {
        console.log("Your name is not valid");
        fathername.classList.add('is-invalid');
        validFatherName = false;
    }
})


email.addEventListener('blur', () => {
    let regex = /^([_\-\.0-9a-zA-Z]+)@([_\-\.0-9a-zA-Z]+)\.([a-zA-Z]){2,10}$/;
    let str = email.value;
    console.log(regex, str);

    if (regex.test(str)) {
        console.log('Your email is valid');
        email.classList.remove('is-invalid');
        validEmail = true;
    }
    else {
        console.log("Your email is not valid");
        email.classList.add('is-invalid');
        validEmail = false;
    }
})

phone.addEventListener('blur', () => {
    let regex = /^([0-9]){10}$/;
    let str = phone.value;
    console.log(regex, str);

    if (regex.test(str)) {
        console.log('Your phone no is valid');
        phone.classList.remove('is-invalid');
        validPhone = true;
    }
    else {
        console.log("Your phone no is not valid");
        phone.classList.add('is-invalid');
        validPhone = false;
    }
})

let submit = document.getElementById('submit');
submit.addEventListener('click', (e) => {
    e.preventDefault();

    console.log('You clicked on submit');
    //Submit your form here 
    if (validEmail && validPhone && validFname && validFatherName && validLname) {
        let failure = document.getElementById('failure');

        console.log('Phone,email or fname ,lname fathername are valid. Submitting the form');
        let success = document.getElementById('success');
        success.classList.add('show');
        // failure.classList.remove('show');
        $('#failure').hide();
        $('#success').show();

    }
    else {
        console.log('Phone,email or fname ,lname fathername are not valid.. Hence not submitting the form.Please correct the errors and try again');
        let failure = document.getElementById('failure');
        failure.classList.add('show');
        // success.classList.remove('show');
        $('#success').hide();
        $('#failure').show();
    }

})

function checkRetype(form)
{
if(frm1.pass.value!==frm1.rpass.value)
{alert("Password not match...! Try Again!");}
}




