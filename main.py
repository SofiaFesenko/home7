import csv
from copy import deepcopy, copy
import pickle


with open('products.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['name', 'date', 'end_date', 'pieces', 'country'], delimiter=',')
    writer.writeheader()
    writer.writerow({'name': 'ananas', 'date': ' 03.11', 'end_date': ' 03.12', 'pieces': ' 7', 'country': ' Africa'})
    writer.writerow({'name': 'bread', 'date': ' 03.11', 'end_date': ' 08.11', 'pieces': ' 10', 'country': ' Ukraine'})
    writer.writerow({'name': 'some nonsense', 'date': ' 01.10', 'end_date': ' no', 'pieces': ' 5', 'country': ' China'})


class Copy:
    def __init__(self, x):
        self.x = x

    def __copy__(self):
        copy_obj = Copy(self.x)
        copy_obj.__dict__.update(self.__dict__)
        return copy_obj

    def __deepcopy__(self):
        copy_obj = Copy(self.x)
        copy_obj.data = deepcopy(self.x)
        return copy_obj


my_copy = Copy
my_copy.x = [1, 2, 5, 9]
my_copy.x[2] = 65

print(my_copy.x)


my_copy.x = [1, 3, 5, 7]

my_object_copy = deepcopy(my_copy.x)
my_copy.x[2] = 65
print(my_object_copy)


class SomeClass:
    def __init__(self, filename):
        self.name = filename
        self.file = open(filename)

    def __getstate__(self):
        odict = self.__dict__.copy()
        del odict['file']
        return odict

    def __setstate__(self, dict):
        fh = open(dict['name'])
        self.name = dict['name']
        self.file = fh


obj = SomeClass('test.txt')


res = pickle.loads(pickle.dumps(obj))
res.file.read()
