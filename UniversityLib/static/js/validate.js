function validateForm() {
let password = document.forms["signupForm"]["password"].value;
let confirmPassword = document.forms["signupForm"]["confirmPassword"].value;
let username = document.forms["signupForm"]["username"].value;

  if (password!=confirmPassword) {
    alert("passwords does not match");
    document.forms["signupForm"]["confirmPassword"].focus();
    return false;
  }

  if(password.length<6){
    alert("password must contain at least 6 characters");
    document.forms["signupForm"]["password"].focus();
    return false;
  }
  re=/[0-9]/
  if(!re.test(password)){
    alert("password must contain at least one numbers (0-9)!");
    document.forms["signupForm"]["password"].focus();
    return false;
  }


};

function validateEdit(){

  let password = document.forms["EditForm"]["password"].value;

  if(password.length<6){
    alert("password must contain at least 6 characters");
    document.forms["EditForm"]["password"].focus();
    return false;
  }

  re=/[0-9]/
  if(!re.test(password)){
    alert("password must contain at least one numbers (0-9)!");
    document.forms["EditForm"]["password"].focus();
    return false;
  }
};
