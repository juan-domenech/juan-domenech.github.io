//Fibonacci Challenge
//The fibonacci sequence is a mathematical sequence of integers. By definition, the first two numbers in the Fibonacci sequence are 0 and 1, and each subsequent number is the sum of the previous two.
//0, 1, 1, 2, 3, 5, 8, 13, ..
//Define a function called 'fibonacci' with a single argument n. The function should return the nth number of the fibonacci sequence.

function fibonacci( n ){

var serie=[0,1];

		for (i=2; i<=n; i++){

			serie[i] = serie[i-1] + serie[i-2];

		}

	return serie[n];

}
