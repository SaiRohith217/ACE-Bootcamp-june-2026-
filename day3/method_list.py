def main():
    numbers = [1, 2, 3, 4, 5]

    numbers.append(6)          # add to end
    numbers.insert(0, 0)       # add at position
    numbers.remove(3)          # remove value
    popped = numbers.pop()     # remove last item
    numbers.extend([7, 8])     # add multiple items
    count_five = numbers.count(5)
    index_four = numbers.index(4)
    numbers.sort(reverse=True) # sort descending

    print("Final list:", numbers)
    print("Popped item:", popped)
    print("Count of 5:", count_five)
    print("Index of 4:", index_four)

if __name__ == "__main__":
    main()
