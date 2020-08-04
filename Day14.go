///////////////////////////////////////////
// Author: Malay Agarwal
// Problem:
//
// There is a robot starting at position
// (0, 0), the origin, on a 2D plane.
// Given a sequence of its moves, judge
// if this robot ends up at (0, 0) after
// it completes its moves.
//
// The move sequence is represented by a
// string, and the character moves[i]
// represents its ith move. Valid moves
// are R (right), L (left), U (up), and
// D (down). If the robot returns to the
// origin after it finishes all of its
// moves, return true. Otherwise,
// return false.
///////////////////////////////////////////
package main

import (
	"strings"
)

func judgeCircle(moves string) bool {
	x := 0
	y := 0
	moveList := strings.Split(moves, ",")
	for _, c := range moveList {
		if c == "U" {
			x++
		}
		if c == "D" {
			x--
		}
		if c == "R" {
			y++
		}
		if c == "L" {
			y--
		}
	}
	if (x != 0) || (y != 0) {
		return true
	} else {
		return false
	}
}
