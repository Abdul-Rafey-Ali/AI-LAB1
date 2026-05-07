# Minimax Algorithm (Python)

This project implements the **Minimax algorithm** in Python (the classic approach used for game-tree search when players alternate turns).

## Features
- Clean, production-style implementation in `src/minimax.py`
- Optional recursion depth target derived from the number of leaf scores
- Example run and output stored in `outputs/output_example.txt`
- Basic documentation in `docs/algorithm_explanation.md`

## Lab 8
Implements the standard minimax recursion:
- **Maximizing player** picks the maximum value among children
- **Minimizing player** picks the minimum value among children
- Base case returns the value at leaf nodes

## How to run
From the repository root:

```bash
python -m src.minimax
```

Or run the file directly:

```bash
python src/minimax.py
```

## Requirements
See `requirements.txt`.

## License
See `LICENSE`.

