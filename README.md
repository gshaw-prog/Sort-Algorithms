# IB Computer Science Project: Sorting Algorithms (B2.4.3)

This repository contains implementations and theoretical evaluations of two fundamental sorting algorithms: Bubble Sort and Selection Sort. This project aligns directly with the **IB Diploma Programme Computer Science** curriculum, specifically focusing on Theme B: Computational thinking and problem-solving.

---

## 📚 Syllabus Alignment: B2 Programming Algorithms

This project addresses syllabus understanding **B2.4.3: Construct and trace algorithms to implement bubble sort and selection sort, evaluating their time and space complexities**.

The core task involves sorting data efficiently, simulating a **Leaderboard Manager Problem** which requires scores to be placed in the correct order.

---

## 🛠️ Algorithms Implemented

Both algorithms demonstrate solutions for sorting data structures (lists/arrays). Pseudocode and Python implementations (for ascending order demonstration) are included.

### 1. Bubble Sort

| Concept | Description |
| :--- | :--- |
| **Mechanics** | The Bubble Sort algorithm repeatedly steps through the list, comparing **pairs of adjacent elements** and **swapping** them if they are in the wrong order. 
| **Characteristics** | It is simple to implement but requires frequent swapping. |
| **Complexity** | Time Complexity: **$O(n^2)$ (Quadratic)**. Space Complexity: **Minimal**, as elements are swapped in place, requiring minimal additional storage. |

### 2. Selection Sort

| Concept | Description |
| :--- | :--- |
| **Mechanics** | Selection Sort finds the highest (or lowest) element in the unsorted portion of the list and places it at the start of the sorted portion. |
| **Characteristics** | It utilizes indexing to sort data. It **minimizes the number of swaps** required compared to Bubble Sort. |
| **Complexity** | Time Complexity: **$O(n^2)$ (Quadratic)**. Space Complexity: **Minimal**, as elements are swapped in place. |

---

## 📈 Complexity Analysis ($O(n)$ Notation)

Evaluating the efficiency of algorithms involves calculating their **Big O notation** ($O$).

| Metric | Bubble Sort | Selection Sort | Evaluation |
| :--- | :--- | :--- | :--- |
| **Time Complexity** | $O(n^2)$ (Quadratic) | $O(n^2)$ (Quadratic) | The quadratic time complexity arises due to the use of **nested loops** in both algorithms. This makes both algorithms **inefficient** for large data sets (such as leaderboards with millions of scores) because performance time increases exponentially with the input size ($n$). |
| **Space Complexity** | Minimal/In Place | Minimal/In Place | Both are memory efficient as they require minimal additional storage outside the data structure itself. |

### Tracing and Verification
To verify the logic and functionality of the algorithms, especially for educational tracing, techniques like a **trace table** are essential to follow and record the actions of the algorithm and verify variable values at each step.

---

## 💻 Getting Started (Version Control)

This repository is designed to practice programming skills, as well as version control practices (Git/GitHub).

### Setting Up the Project

1.  **Clone the Repository:** Download the project files to your local machine.
2.  **Open in IDE:** Use a suitable Integrated Development Environment (IDE) like Visual Studio Code (VS Code) to review the Python code and pseudocode implementations.
3.  **Testing:** Run the Python scripts to observe how the data set is sorted.

### Version Control Best Practices

When making changes or attempting the corresponding coding challenge:

*   **Commit Frequently:** Commit your changes frequently with descriptive messages (e.g., "**Implemented string slicing for first/last characters**" or "**Added input function**").
*   **Stage Changes:** Use the Source Control view in VS Code to stage your changes before committing.
*   **Push to GitHub:** Click the "Synchronize Changes" or "Push" button to upload changes to the GitHub repository. For personal learning projects, choosing a **private repository is usually a good starting point**.
*   **Resilience:** Practice is key, and mistakes are a valuable part of the learning process. Version control allows you to revert if necessary, fostering resilience.

---
