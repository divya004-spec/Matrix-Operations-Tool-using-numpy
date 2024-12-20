import numpy as np

def print_matrix(matrix):
    """Print matrix in a structured format"""
    for row in matrix:
        print(row)

def input_matrix():
    """Input a matrix from the user"""
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    matrix = []
    print(f"Enter the elements of the {rows}x{cols} matrix:")
    for i in range(rows):
        row = list(map(int, input(f"Row {i + 1}: ").split()))
        matrix.append(row)
    return np.array(matrix)

def matrix_operations():
    print("Matrix Operations Tool")
    print("------------------------")
    print("Choose an operation:")
    print("1. Add Matrices")
    print("2. Subtract Matrices")
    print("3. Multiply Matrices")
    print("4. Transpose Matrix")
    print("5. Determinant of Matrix")
    print("6. Exit")

    while True:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            print("Matrix Addition")
            print("---------------")
            matrix1 = input_matrix()
            matrix2 = input_matrix()
            if matrix1.shape == matrix2.shape:
                result = np.add(matrix1, matrix2)
                print("Result of Matrix Addition:")
                print_matrix(result)
            else:
                print("Matrices must have the same dimensions for addition.")
        
        elif choice == 2:
            print("Matrix Subtraction")
            print("--------------------")
            matrix1 = input_matrix()
            matrix2 = input_matrix()
            if matrix1.shape == matrix2.shape:
                result = np.subtract(matrix1, matrix2)
                print("Result of Matrix Subtraction:")
                print_matrix(result)
            else:
                print("Matrices must have the same dimensions for subtraction.")
        
        elif choice == 3:
            print("Matrix Multiplication")
            print("----------------------")
            matrix1 = input_matrix()
            matrix2 = input_matrix()
            if matrix1.shape[1] == matrix2.shape[0]:
                result = np.dot(matrix1, matrix2)
                print("Result of Matrix Multiplication:")
                print_matrix(result)
            else:
                print("The number of columns in the first matrix must be equal to the number of rows in the second matrix.")
        
        elif choice == 4:
            print("Transpose Matrix")
            print("----------------")
            matrix = input_matrix()
            result = np.transpose(matrix)
            print("Transpose of the Matrix:")
            print_matrix(result)
        
        elif choice == 5:
            print("Determinant of Matrix")
            print("---------------------")
            matrix = input_matrix()
            if matrix.shape[0] == matrix.shape[1]:  # Only square matrices have determinants
                result = np.linalg.det(matrix)
                print(f"Determinant of the matrix: {result}")
            else:
                print("Determinant can only be calculated for square matrices.")
        
        elif choice == 6:
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    matrix_operations()
