class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.list_of = []
        self.list_to_item = []
        self.index = 0

    def __iter__(self):
        for lists in self.list_of_list:
            for value_list in lists:
                self.list_of.append(value_list)

        for value1_to_item in self.list_of:
            if isinstance(value1_to_item, list) == True and value1_to_item != []:
                for value1 in value1_to_item:
                    value2_to_item = value1

                    while isinstance(value2_to_item, list) == True:
                        for temporary in value2_to_item:
                            value2_to_item = temporary

                    self.list_to_item.append(value2_to_item)

            elif isinstance(value1_to_item, list) == False and value1_to_item != []:
                self.list_to_item.append(value1_to_item)

        return self

    def __next__(self):
        if self.index == len(self.list_to_item):
            raise StopIteration
        item = self.list_to_item[self.index]
        self.index += 1
        return item


def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()