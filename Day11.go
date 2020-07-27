///////////////////////////////////////////
// Author: Malay Agarwal
// Problem:
// Given a binary tree, each node has value
// 0 or 1.  Each root-to-leaf path
// represents a binary number starting with
// the most significant bit. For example,
// if the path is 0 -> 1 -> 1 -> 0 -> 1,
// then this could represent 01101 in
// binary, which is 13.
// For all leaves in the tree, consider
// the numbers represented by the path
// from the root to that leaf.
// Return the sum of these numbers.
//////////////////////////////////////////
package sumRootToLeaf
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func DFS(root *TreeNode, sum int, total *int) {
	if root == nil {
		return
	}
	sum += root.Val
	if root.Left == nil && root.Right == nil {
		*total += sum
	}
	DFS(root.Left, sum * 2, total)
	DFS(root.Right, sum * 2, total)
}
func sumRootToLeaf(root *TreeNode) int {
	total := 0
	DFS(root, 0, &total)
	return total
}