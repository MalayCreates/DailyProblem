///////////////////////////////////////////
// Author: Malay Agarwal
// Problem:
// Given an array of unique integers salary
// where salary[i] is the salary of the
// employee i. Return the average salary
// of employees excluding the minimum and
// maximum salary.
//////////////////////////////////////////

package main

import (
	"fmt"
)

func average(salary []int) float64 {
	minValue := salary[0]
	maxVal := salary[0]
	totalValue := 0
	for _, val := range salary {
		if val < minValue {
			minValue = val
		} else if val > maxVal {
			maxVal = val
		}
	}
	for _, val := range salary {
		totalValue += val
	}
	totalValue -= minValue
	totalValue -= maxVal
	totalValue = totalValue / (len(salary) - 2)
	return float64(totalValue)
}

func main() {
	salarySlice := []int{100, 234, 86, 63, 96, 34, 110, 107, 82}
	fmt.Println(average(salarySlice), "k dollars")
}
