def main():
    fruits = {"apple", "banana", "orange"}
    more_fruits = {"banana", "grape", "kiwi"}

    print("Fruits:", fruits)
    print("More fruits:", more_fruits)
    print("Union:", fruits | more_fruits)
    print("Intersection:", fruits & more_fruits)
    print("Difference:", fruits - more_fruits)

if __name__ == "__main__":
    main()
