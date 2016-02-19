//Kata: Password Validation
//Problem Description
//Create a function passwordValidation() that receives a string and returns true when:
//the string contains at least one letter in uppercase
//the string contains at least 2 numbers (digits)
//the string contains at least one of these special characters: $ # % & - ! ?
//the string has 10 characters or more
//Otherwise the function should return true
//
//Stage 2 - config variable
//Modify the previous function to use a variable called config being this one an object with the rules to apply in the validation.
//This object should have the following structure:
//
//config = {
//    size : 10,
//    uppercase : 1,
//    numbers : 2,
//    special = "$#%&-!?"
//}
//Modify the function to read the "rules" from this object,
//After this modification the behaviour should be same (so the tests should pass the same)


function PasswordValidation ( password ) {

	// Configuration settings
	config = {
		size : 10,
		uppercase : 1,
		numbers : 2,
		special : "$#%&-!?"
	};

	// Construct the regHex using the values provided by the configuration object and escaping the characters
	function polulateRegHex(){
		var regHex='';
		for (i=0; i<config.special.length; i++){
			regHex += '\\'+config.special[i];
		}
		return '['+regHex+']';
	}

	// Object.prototype.toString.call() = "object RegHex"
	var regHex = new RegExp( polulateRegHex() );

	// Password can't be empty
	if ( password == undefined ){
		return false;

	// Check for any Uppercase present
	} else if ( password.match(/[A-Z]/g) == null ){
		return false;

	// Check for configired Uppercase present
	} else if ( password.match(/[A-Z]/g).length < config.uppercase ){
		return false;

	// At least any numbers present
	} else if ( password.match(/[0-9]/g).length == null ){
		return false;

	// At least configured numbers present
	} else if ( password.match(/[0-9]/g).length < config.numbers ){
		return false;

	// At least one of these symbols in config.special present
	} else if ( password.match(regHex) == null ){
		return false;

	// Check length
	} else if ( password.length < config.size ){
		return false;

	// Everything went well. Password valid.
	} else {
	return true;
	}

}
