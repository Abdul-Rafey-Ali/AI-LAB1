## Minimax Algorithm Explanation

Minimax is a recursive algorithm used to decide the best move for a player assuming the opponent also plays optimally.

### Game model (tree)
- Each node represents a game state.
- Children of a node represent possible next states.
- Levels alternate between:
  - **Max** node (player tries to maximize the score)
  - **Min** node (opponent tries to minimize the score)

### Recurrence
Let `minimax(curDepth, nodeIndex, maxTurn)` be the optimal value from a subtree.

- **Base case**: when `curDepth == targetDepth`, return the leaf score.
- **If it's Max's turn**: return the maximum of the two children values.
- **If it's Min's turn**: return the minimum of the two children values.

### Complexity
- Time complexity: **O(b^d)** where `b` is branching factor (2 for this binary tree) and `d` is depth.
- Space complexity: **O(d)** due to recursion stack.

### Notes about this implementation
This lab version treats the game tree as a **complete binary tree** encoded in an array of leaf scores.
Leaf scores are stored in `scores`, and internal node values are computed via minimax recursion.

