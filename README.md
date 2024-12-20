# Matrix-Operations-Tool-using-numpy
The Matrix Operations Tool is a Python application that allows users to perform matrix operations like addition, subtraction, multiplication, transpose, and determinant calculation using NumPy. It features an interactive interface for matrix input, with validation for consistent row lengths and error handling for invalid inputs.


## Overview

The **Matrix Operations Tool** is a Python application that enables users to perform various matrix operations such as addition, subtraction, multiplication, transpose, and determinant calculation using the powerful **NumPy** library. This tool features an interactive interface, where users can input matrices and see the results in a structured format.

## Features

- **Matrix Addition**: Adds two matrices if they have the same dimensions.
- **Matrix Subtraction**: Subtracts one matrix from another if they have the same dimensions.
- **Matrix Multiplication**: Multiplies two matrices when the number of columns in the first matrix equals the number of rows in the second.
- **Transpose Matrix**: Computes the transpose of a matrix.
- **Determinant**: Calculates the determinant of square matrices.
- **Input Validation**: Ensures that all rows have the correct number of elements and handles invalid input gracefully.

## Requirements

- Python 3.x
- NumPy library

To install NumPy, run:

```bash
pip install numpy
```

## Usage

1. Clone or download the repository.
2. Run the program:

```bash
python app.py
```

3. Follow the on-screen prompts to input matrices and select the desired operation.
4. View the results for the selected matrix operation.

## Example

### Sample Operation: Matrix Addition

```text
Matrix Operations Tool
------------------------
Choose an operation:
1. Add Matrices
2. Subtract Matrices
3. Multiply Matrices
4. Transpose Matrix
5. Determinant of Matrix
6. Exit
Enter your choice: 1
Matrix Addition
---------------
Enter the number of rows: 2
Enter the number of columns: 2
Enter the elements of the 2x2 matrix:
Row 1: 1 2
Row 2: 3 4
Enter the number of rows: 2
Enter the number of columns: 2
Enter the elements of the 2x2 matrix:
Row 1: 5 6
Row 2: 7 8
Result of Matrix Addition:
[6 8]
[10 12]
```

## Contribution

Feel free to fork the repository and submit pull requests. Any suggestions or improvements are welcome.

## License

This project is open-source and available under the MIT License.

---

This README provides an overview of the tool, its features, requirements, and usage, along with an example of how the program works.
