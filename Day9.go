///////////////////////////////////////////
// Author: Malay Agarwal
// Problem:
// We are given two strings, A and B.
// A shift on A consists of taking string
// A and moving the leftmost character to
// the rightmost position.
//////////////////////////////////////////

package judgeCircle

import (
	"fmt"
)

func rotateString(A string, B string) bool {
	var temp string
	isIt := false
	for i, _ := range A {
		temp = A[i:]
		temp = temp + A[0:i]
		if temp == B {
			isIt = true
		}
	}
	return isIt
}

func main() {
	strA := "abcde"
	strB := "cdeab"
	fmt.Println(rotateString(strA, strB))
}
