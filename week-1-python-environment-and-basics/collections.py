# list
name = ["Mahfuz", "Hasan", "Reza"]

print(name)
print(type(name))
print(name[0])  # Accessing first element
print(name[-1])  # Accessing last element
print(name[1:3])  # Slicing
name.append("MHR")  # Adding an element
print(name)
name[1] = "Learn"  # Modifying an element
print(name)
name.remove("Reza")  # Removing an element
print(name)

print(len(name))  # Length of the list
print(sum([1, 2, 3, 4, 5]))  # Sum of numbers in a list
print(sorted([3, 1, 4, 2, 5]))  # Sorted list
print(max([3, 1, 4, 2, 5]))  # Maximum value
print(min([3, 1, 4, 2, 5]))  # Minimum value

number_list = [5, 2, 9, 1, 5, 6]
number_list.sort()  # Sorting the list in place
print(number_list)

# tuple
coordinates = (10.0, 20.0)
print(coordinates)

# coordinates[0] = 15.0  # This will raise an error since tuples are immutable

# dictionary
student = {
    "name": "Mahfuz",
    "age": 22,
    "courses": ["Math", "Science"]
}
print(student)
print(student["name"])  # Accessing value by key
student["age"] = 23  # Modifying value
student["grade"] = "A"  # Adding new key-value pair
print(student)
del student["courses"]  # Removing key-value pair
print(student)
print(student.keys())  # Getting all keys
print(student.values())  # Getting all values
print(student.items())  # Getting all key-value pairs

# set
names_set = {"Mahfuz", "Hasan", "Reza"}
print(names_set)

names_set.add("MHR")  # Adding an element
print(names_set)
names_set.remove("Hasan")  # Removing an element
print(names_set)
print("Mahfuz" in names_set)  # Membership test
print(len(names_set))  # Length of the set

another_set = {"Reza", "Khan", "Ali"}
print(names_set.union(another_set))  # Union
print(names_set.intersection(another_set))  # Intersection
print(names_set.difference(another_set))  # Difference
print(names_set.symmetric_difference(another_set))  # Symmetric Difference

# frozenset
frozen_names = frozenset(["Mahfuz", "Hasan", "Reza"])
print(frozen_names)
# frozen_names.add("MHR")  # This will raise an error since frozensets are immutable

print("Mahfuz" in frozen_names)  # Membership test
print(len(frozen_names))  # Length of the frozenset
print(frozen_names.union(another_set))  # Union
print(frozen_names.intersection(another_set))  # intersection
print(frozen_names.difference(another_set))  # Difference
print(frozen_names.symmetric_difference(another_set))  # Symmetric Difference