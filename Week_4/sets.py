# Create two sets of integers.
# Perform: Union
# Perform: Intersection
# Perform: Difference
# Add a new element to a set.
# Remove an element from a set.

def main():
    set_a = {0, 1, 2, 3, 4, 5}
    set_b = {0, 6, 7, 8, 9, 10}
    print(f"Set A: {set_a}")
    print(f"Set B: {set_b}")
    print(f"A Union B: {set_a.union(set_b)}")
    print(f"A Intersection B: {set_a.intersection(set_b)}")
    print(f"A Difference B: {set_a.difference(set_b)}")
    set_b.add(100)
    print(f"Add new Element in B: {set_b}")
    set_b.remove(100)
    print(f"Remove Element from B: {set_b}")

if __name__ == "__main__":
    main()