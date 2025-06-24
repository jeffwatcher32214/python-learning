# Create a list of 10 random integers.
# Append an item to the list.
# Insert an item at a specific index.
# Remove an item from the list.
# Sort the list in ascending order.
# Reverse the list.

def main():
    my_list = [5, 6, 7, 8, 9, 10, 1, 2, 3, 4]
    print(f"List Creataion: {my_list}")
    
    my_list.append(11)
    print(f"Append: {my_list}")
    
    my_list.insert(6,0)
    print(f"Insert: {my_list}")
    
    my_list.remove(11)
    print(f"Remove: {my_list}")
    
    my_list.sort()
    print(f"Sort: {my_list}")
    
    my_list.reverse()
    print(f"Reverse: {my_list}")

if __name__ == "__main__":
    main()