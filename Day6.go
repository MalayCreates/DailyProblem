///////////////////////////////////////////
// Author: Malay Agarwal
// Problem: 
// Determine whether an integer is a
// palindrome. An integer is a palindrome
// when it reads the same backward as
// forward.
//////////////////////////////////////////
package palindromeint

import "fmt"
/*
This is the very first file I have coded in GoLang,
trying to learn it
*/

func palindromeInt() {
	var num, remainder, temp int
	var reverse = 0
	fmt.Println("Enter non-zero positive number : ")
	fmt.Scan(&num)

	temp = num

	for {
		remainder = num % 10
		reverse = reverse*10 + remainder
		num = num / 10

		if num == 0 {
			break
		}
	}

	if temp == reverse {
		fmt.Printf("%d is a Palindrome\n", temp)
	} else{
		fmt.Printf("%d is not a Palindrome:\n", temp)
	}
}
