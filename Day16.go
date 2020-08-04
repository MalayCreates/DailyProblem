///////////////////////////////////////////
// Author: Malay Agarwal
// Problem:
// Given N, calculate fib(N)
///////////////////////////////////////////

package main

import (
	"fmt"
)

func fib(N int) int {
	if N <= 1 {
		return N
	}
	return fib(N-1) + fib(N-2)
}
func main() {
	fmt.Println(fib(10))
}
