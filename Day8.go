///////////////////////////////////////////
// Author: Malay Agarwal
// Problem:
// Given a non-negative integer num,
// repeatedly add all its digits until the
// result has only one digit.
//////////////////////////////////////////
package judgeCircle

import (
	"fmt"
)

func addDigits(num int) int {
	for num > 9 {
		temp := 0
		for num > 0 {
			temp += num % 10
			num /= 10
		}
		num = temp
	}
	return num
}

func main() {
	inNum := 39
	fmt.Println(addDigits(inNum))
}
