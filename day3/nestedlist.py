def main():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    print("Nested list (matrix):")
    for row in matrix:
        print(row)

    print("Item at row 2, col 3:", matrix[1][2])
    print("Second row:", matrix[1])
    print("Flattened list:", [value for row in matrix for value in row])

if __name__ == "__main__":
    main()
