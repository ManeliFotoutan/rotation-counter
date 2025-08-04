# rotation-counter

This project contains Python implementations of two self-balancing binary search trees: **AVL Tree** and **Red-Black Tree (RB Tree)**. The code inserts a dataset into both trees and counts the total number of rotations performed during insertions. This allows comparison of the balancing effort between the two tree types.


##  Features

- **AVL Tree**
  - Maintains strict balance using node heights.
  - Performs left and right rotations to rebalance.
  - Counts single and double rotations during insertion.

- **Red-Black Tree**
  - Maintains balance by enforcing color properties.
  - Uses rotations and recoloring during insertions.
  - Counts rotations performed to fix violations.

- Insert arbitrary datasets into either tree and track rotation counts.


##  Files

- `main.py` – Main script implementing both AVL and Red-Black trees.
- [`problem.pdf`](./problem.pdf) – Detailed description of the algorithm, design decisions, and complexity analysis.


##  Dependencies

Make sure you have Python 3.6+ installed. Then install any required libraries:

> 🔹 This project only uses standard Python libraries (`random`, `time`, etc.).  
> 🔹 No external packages are required for running the code.

 Usage
Clone the repository or copy the code into a Python file:

```bash
git clone https://github.com/your-username/rotation-counter.git
cd rotation-counter
```
Open main.py and modify the dataset if needed.
Run the script:
```bash
python main.py
```
The output will display the total number of rotations for both trees.

## Code Explanation
AVLNode and AVLTree classes:

Implements an AVL tree with node heights.

Automatically balances after insertion using rotations.

RBNode and RBTree classes:

Implements a Red-Black tree with color and parent pointers.

Enforces red-black properties with rotations and recoloring.

Each tree maintains a rotations counter to track the number of balancing operations.

Example datasets are included to demonstrate functionality.

You can also uncomment the large dataset block to evaluate performance under more data.

## Example Output
mathematica
```bash
Total rotations in AVL Tree: 12
Total rotations in Red-Black Tree: 7
```
## Notes
The large dataset section is commented out to prevent long execution times.

Red-Black Tree implementation uses sentinel TNULL nodes for simplification.

Rotations are tracked separately in both trees and compared at the end.

For full algorithm explanation and theoretical background, refer to:

problem.pdf

If you plan to extend functionality (e.g. visualization), you might optionally install:

```bash
pip install matplotlib
```
