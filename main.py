
class FlatIterator:

    def __init__(self, list_of_list, n):
        self.n = -1
        self.list_of_list = list_of_list

    def __iter__(self):
        flat_list = []
        for group in self.list_of_list:
            flat_list.extend(group)
        return self

    def __next__(self):
        self.n += 1
        if self.n == len(flat_list):
            raise StopIteration

        return flat_list



list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
        ]

for item in FlatIterator(list_of_lists_1, 1):
    print(item)


# list_inter = iter(list_of_lists_1)
# in_list_iter = iter(list_inter.__next__())
# print(in_list_iter.__next__())


# flat_list = FlatIterator(list_of_lists_1)
#
# for item in flat_list:
#     print(item)

# def test_1():
#
#     list_of_lists_1 = [
#         ['a', 'b', 'c'],
#         ['d', 'e', 'f', 'h', False],
#         [1, 2, None]
#     ]
#
#     for flat_iterator_item, check_item in zip(
#             FlatIterator(list_of_lists_1),
#             ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
#     ):
#
#         assert flat_iterator_item == check_item
#
#     assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
#
#
# if __name__ == '__main__':
#     test_1()