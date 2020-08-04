///////////////////////////////////////////
// Author: Malay Agarwal
// Problem:
// Given N, calculate Fib(N)
///////////////////////////////////////////

package main

import (
	"fmt"
)

func fib(N int) int {
	//recursively go through fib func
	if N <= 1 {
		return N
	}
	return fib(N-1) + fib(N-2)
}

func main() {
	fmt.Println(fib(10))
}
