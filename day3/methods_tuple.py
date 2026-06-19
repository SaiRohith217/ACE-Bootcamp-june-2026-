def main():
    colors = ("red", "green", "blue", "green", "yellow")

    print("Tuple:", colors)
    print("\nTuple methods:")
    methods = [name for name in dir(tuple) if not name.startswith("__")]
    print(methods)

    print("\nCount of 'green':", colors.count("green"))
    print("Index of 'blue':", colors.index("blue"))
    print("Length:", len(colors))
    print("First item:", colors[0])
    print("Slice [1:4]:", colors[1:4])

if __name__ == "__main__":
    main()
