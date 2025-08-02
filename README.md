# rotation-counter
This project contains Python implementations of two self-balancing binary search trees: **AVL Tree** and **Red-Black Tree (RB Tree)**. The code inserts a dataset into both trees and counts the total number of rotations performed during insertions. This allows comparison of the balancing effort between the two tree types.

---

## Features

- **AVL Tree**
  - Maintains strict balance using node heights.
  - Performs left and right rotations to rebalance.
  - Counts single and double rotations during insertion.

- **Red-Black Tree**
  - Maintains balance by enforcing color properties.
  - Uses rotations and recoloring during insertions.
  - Counts rotations performed to fix violations.

- Insert arbitrary datasets into either tree and track rotation counts.

---

## Files

- `main.py` (contains the code you see here)
- `problem.pdf` (detailed description of the algorithm, design decisions, and analysis)

---

## Usage

1. Import or copy the code into a Python file.
2. Modify the dataset in the script or use a large randomly generated dataset (commented out in code).
3. Run the script to insert the values into both trees.
4. View the output displaying total rotations performed by each tree.

---

## Code Explanation

- `AVLNode` and `AVLTree` classes implement the AVL tree with height tracking and balancing.
- `RBNode` and `RBTree` classes implement the Red-Black tree with color and parent pointers.
- Both trees keep a `rotations` counter to track how many rotations occurred during insertions.
- Example dataset is used to demonstrate functionality with small data.
- You can uncomment the large dataset block to test performance on large inputs.

---

## Example Output

Total rotations in AVL Tree: X
Total rotations in Red-Black Tree: Y

Where `X` and `Y` are the total rotation counts for AVL and Red-Black trees respectively.

---

## Notes

- The large dataset section is commented out to avoid long execution times.
- Red-Black Tree uses sentinel `TNULL` nodes to simplify boundary conditions.
- Rotations include single and double rotations where applicable.
- For detailed theoretical background and complexity analysis, please see the attached `problem.pdf` file.
