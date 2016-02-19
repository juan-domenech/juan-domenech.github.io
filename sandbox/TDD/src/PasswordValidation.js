//Kata: Password Validation
//Problem Description
//Create a function passwordValidation() that receives a string and returns true when:
//the string contains at least one letter in uppercase
//the string contains at least 2 numbers (digits)
//the string contains at least one of these special characters: $ # % & - ! ?
//the string has 10 characters or more
//Otherwise the function should return true


function PasswordValidation ( password ) {

	// Password can't be empty
	if ( password == undefined ){
		return false;

	// At least one uppercase
	} else if ( password.match(/[A-Z]/g) == null ){
		return false;

	// At least 2 numbers
	} else if ( password.match(/[0-9]/g).length < 2 ){
		return false;

	// At least one of these symbols: $ # % & - ! ?
	} else if ( password.match(/[\$\#\%\&\-\!\?]/g) == null ){
		return false;

	// At least 10 characters long
	} else if ( password.length < 10 ){
		return false;

	// Everything went well. Password valid.
	} else {
	return true;
	}

}
