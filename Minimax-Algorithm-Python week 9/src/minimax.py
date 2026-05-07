"""Minimax algorithm implementation.

This module provides a reference implementation of the classic minimax recursion
for a complete binary game tree.

The tree is represented implicitly by an array of leaf scores. Internal nodes
are evaluated recursively using:
- Maximizing player: takes max of children
- Minimizing player: takes min of children

Lab 8
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Sequence


@dataclass(frozen=True)
class MinimaxResult:
    """Result of a minimax computation."""

    value: float
    target_depth: int


def minimax(cur_depth: int, node_index: int, max_turn: bool, scores: Sequence[float], target_depth: int) -> float:
    """Compute minimax value recursively.

    Parameters
    ----------
    cur_depth:
        Current depth in the tree.
    node_index:
        Index of the current node in the implicit array-based binary tree.
    max_turn:
        True if the current player is maximizing, else minimizing.
    scores:
        Leaf node scores stored in an array representing the bottom level.
    target_depth:
        Depth at which leaf nodes are reached.

    Returns
    -------
    float
        The minimax value for the subtree rooted at (cur_depth, node_index).
    """

    # Base case: reached leaf level
    if cur_depth == target_depth:
        return float(scores[node_index])

    left = minimax(cur_depth + 1, node_index * 2, False, scores, target_depth)
    right = minimax(cur_depth + 1, node_index * 2 + 1, False, scores, target_depth)

    if max_turn:
        return max(left, right)
    return min(left, right)


def compute_optimal_value(scores: Sequence[float]) -> MinimaxResult:
    """Compute the optimal minimax value for a complete binary tree.

    The tree depth is derived from the number of leaf scores.
    For a full binary tree with leaf count N, N must be a power of 2.
    """

    if len(scores) == 0:
        raise ValueError("scores must be non-empty")

    # target_depth such that 2**target_depth == len(scores)
    tree_depth = math.log(len(scores), 2)
    if not tree_depth.is_integer():
        raise ValueError(
            "scores length must be a power of 2 for a complete binary minimax tree "
            f"(got {len(scores)})"
        )

    target_depth = int(tree_depth)
    value = minimax(0, 0, True, scores, target_depth)
    return MinimaxResult(value=value, target_depth=target_depth)


def main() -> None:
    """Run the lab example."""

    scores = [3, 5, 2, 9, 3, 5, 2, 9]
    result = compute_optimal_value(scores)

    print("The optimal value is : ", end="")
    print(result.value)

    # Also write a deterministic output file if running from this module.
    # (Kept lightweight for GitHub use.)
    try:
        from pathlib import Path

        out_path = Path(__file__).resolve().parents[1] / "outputs" / "output_example.txt"
        out_path.write_text(
            f"scores = {scores}\n"
            f"target_depth = {result.target_depth}\n"
            f"optimal_value = {result.value}\n",
            encoding="utf-8",
        )
    except Exception:
        # Non-fatal: the main algorithm output is already printed.
        pass


if __name__ == "__main__":
    main()

