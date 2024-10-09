# Similarity Index of Letter Sequences

## Context

This project addresses the problem of determining the similarity index of N sequences of letters. Each sequence is of the same length, and the similarity is defined recursively based on specific criteria. The task is a part of the Design and Analysis of Algorithms course at Pontificia Universidad Católica de Chile, completed in the second semester of 2023.

## Objectives

The main objectives of this project are:
- To implement an algorithm that calculates the similarity index of letter sequences based on a recursive relationship.
- To analyze the performance of the algorithm with respect to time complexity.
- To apply the divide-and-conquer strategy in the implementation.

## Requirements

To run this code, you need:
- Python 3.x installed on your machine.

## How to Run

1. Clone the repository or copy the code into a Python environment.

2. Open your terminal or command prompt.

3. Run the Python script using the following command:

        ```bash
        python main.py < tests/input/input_XX.txt
        ```

## Example Input

```plaintext
2
frff
ffrf
```

## Example Output

```plaintext
1
```

## Performance

The expected time complexity of the algorithm is **O(N⋅∣Ai∣⋅log(∣Ai∣))**. The solution should execute within 2 seconds for any given instance according to the provided constraints.

## Conclusion

This project demonstrates the application of recursive algorithms and the divide-and-conquer strategy to solve a problem related to string comparison and similarity.