# Template for Assignment 1 - T3 2023

def is_float(inStr): 
    """
    Checks if the given string inStr is a float (saved in string format) or not

    Input: A string
    Output: True if it is a float (saved in string format), False otherwise
    """
    test_float = inStr.split('.')
    if len(test_float)==2 and test_float[0].isnumeric() and test_float[1].isnumeric():
        return True
    return False
lst = []

def read_data(filename):
    """
    Input: The name of the data file (filename)
    Output: A table with all the rows of data in the given file. 

    For example: 
    >>> laptops_data = read_data('laptop_dataset.txt')
    >>> laptops_data[:2] # The first two rows of the table
    [[1, 'Apple', 'MacBook Pro', 'Ultrabook', 13.3, 'IPS Panel Retina Display 2560x1600', 'Intel Core i5 2.3GHz', '8GB', '128GB SSD', 'Intel Iris Plus Graphics 640', 'macOS', '1.37kg', 2175.25], [2, 'Apple', 'Macbook Air', 'Ultrabook', 13.3, '1440x900', 'Intel Core i5 1.8GHz', '8GB', '128GB Flash Storage', 'Intel HD Graphics 6000', 'macOS', '1.34kg', 1459.61]]
    """
    pass
    file = open(filename, 'r')
    file.readline()
    lst = []
    for i in file:
        line = i.strip().split(",")
        for j in range(len(line)):
            if line[j].isnumeric():
                line[j] = int(line[j])
            elif is_float(line[j]):
                line[j] = float(line[j])
            elif line[j].isalpha():
                line[j] = str(line[j])
        lst.append(line)
    return lst
    file.close()

lst = read_data('laptop_dataset.txt')

# Task 2
def largest_screen(table):
    """
    Input: A table containing all the data that is available in the given data file (table) 
    Output: Details of laptop/s with the largest screen displayed on the screen.

    For example:
    >>> laptops_data = read_data('laptop_dataset.txt')
    >>> largest_screen(laptops_data)
    Largest Screen Size: 18.4
    [156, 'MSI', 'GE73VR 7RE', 'Gaming', 18.4, 'Full HD 1920x1080', 'Intel Core i7 7700HQ 2.8GHz', '16GB', '256GB SSD +  1TB HDD', 'Nvidia GeForce GTX 1060', 'Windows 10', '2.8kg', 3068.79]
    [181, 'MSI', 'GT80S 6QF-074US', 'Gaming', 18.4, 'Full HD 1920x1080', 'Intel Core i7 6920HQ 2.9GHz', '32GB', '512GB SSD +  1TB HDD', 'Nvidia GTX 980 SLI', 'Windows 10', '4.4kg', 4544.74]
    """
    pass
    maximum_size = 0
    for i in range(len(lst)):
        if lst[i][4] > maximum_size:
            maximum_size = lst[i][4]
    print( "Largest Screen Size: " + str(maximum_size))
    for i in range(len(lst)):
        if lst[i][4] == maximum_size:
            print(lst[i])
    return None


# Task 3
def number_of_laptops(table,company):
    """
    Input: A table containing all the data that is available in the given data file and the company name.
    Output: The number of laptops for each company.

    For example: 
    >>> laptops_data = read_data('laptop_dataset.txt')
    >>> number_of_laptops(laptops_data,"Apple")
    21
    >>> laptops_data = read_data('laptop_dataset.txt')
    >>> number_of_laptops(laptops_data,"Dell")
    297
    """
    pass
    laptop_number = 0
    for i in range(len(lst)):
        if lst[i][1] == company:
            laptop_number += 1
    return laptop_number

# Task 4
def in_range(table,row,lowerbound,upperbound):
    """
    Input: A table containing all the data that is available in the given data file, a minimum price and a maximum  price.
    Output: True if the price of the laptop is within the range, and False otherwise.

    For example: 
    >>> laptops_data = read_data('laptop_dataset.txt')
    >>> laptops_data = read_data('laptop_dataset.txt')
    >>> in_range(laptops_data,2,800,1200)
    True
    >>> in_range(laptops_data,2,1000,1200)
    False
    >>> in_range(laptops_data,267,800,1200)
    False
    >>> in_range(laptops_data,2,800,0)
    False
    """
    pass
    if row >= 0 and row < len(table):
        if table[row][12] >= lowerbound and table[row][12] <= upperbound:
            return True
        else:
            return False
    else:
        return False


# Task 5
def unique_field_values(table,field):
    """
    Input: A table containing all the data that is available in the given data file and a field name (column heading). Only acceptable fields are company and type name.
    Output: The list of all the laptop companies (unique) without repition.

    For example: 
    >>> laptops_data = read_data('laptop_dataset.txt')
    >>> unique_field_values(laptops_data,'company')
    ['Apple', 'HP', 'Acer', 'Asus', 'Dell', 'Lenovo', 'Chuwi', 'MSI', 'Microsoft', 'Toshiba', 'Huawei', 'Xiaomi', 'Vero', 'Razer', 'Mediacom', 'Samsung', 'Google', 'Fujitsu', 'LG']
    >>> unique_field_values(laptops_data,'type name')
    ['Ultrabook', 'Notebook', 'Netbook', 'Gaming', '2 in 1 Convertible', 'Workstation']
    >>> print(unique_field_values(laptops_data,'abc'))
    Invalid field
    None
    """
    pass

    field = field.lower()
    if field == "company":
        companies = []
        for row in table:
            if row[1] not in companies:
                companies.append(row[1])
        return companies
    elif field == "type name":
        type_names = []
        for row in table:
            if row[3] not in type_names:
                type_names.append(row[3])
        return type_names
    else:
        print("Invalid field")
        return None

# Task 6
def preferred_laptops(table):
    """
    Input: A table containing all the data that is available in the given data file.
    Output: The same table with a new column added stating if each job role is ‘preferred’ or ‘not’.

    For example: 
    >>> laptops_data = read_data('laptop_dataset.txt')
    >>> preferred_laptops(laptops_data)
    >>> laptops_data[2]
    [3, 'HP', '250 G6', 'Notebook', 15.6, 'Full HD 1920x1080', 'Intel Core i5 7200U 2.5GHz', '8GB', '256GB SSD', 'Intel HD Graphics 620', 'No OS', '1.86kg', 933.63, 'preferred']
    >>> laptops_data[:2]
    [[1, 'Apple', 'MacBook Pro', 'Ultrabook', 13.3, 'IPS Panel Retina Display 2560x1600', 'Intel Core i5 2.3GHz', '8GB', '128GB SSD', 'Intel Iris Plus Graphics 640', 'macOS', '1.37kg', 2175.25, 'not'], [2, 'Apple', 'Macbook Air', 'Ultrabook', 13.3, '1440x900', 'Intel Core i5 1.8GHz', '8GB', '128GB Flash Storage', 'Intel HD Graphics 6000', 'macOS', '1.34kg', 1459.61, 'not']]
    """
    pass


#Task 7
def record_preferred(table, output_filename='preferred_laptops.txt'):
    """
    Input: A table containing all the data that is available in the given data file with the preferred column  appended.
    Output: The given file updated with the details of the preferred laptops.

    For example: 
    >>> laptops_data = read_data('laptop_dataset.txt')
    >>> preferred_laptops(laptops_data)
    >>> record_preferred(laptops_data, 'preferred_laptops.txt')
    """
    pass