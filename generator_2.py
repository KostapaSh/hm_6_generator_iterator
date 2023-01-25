import types


def flat_generator(list_of_list):
    list_yield = []

    for lists in list_of_list:

        for value_list in lists:
            list_yield.append(value_list)

    for value1_to_yield in list_yield:

        if isinstance(value1_to_yield, list) == True and value1_to_yield != []:

            for value1 in value1_to_yield:
                value2_to_yield = value1

                while isinstance(value2_to_yield, list) == True:
                    for temporary in value2_to_yield:
                        value2_to_yield = temporary

                yield value2_to_yield

        elif isinstance(value1_to_yield, list) == False and value1_to_yield != []:

            yield value1_to_yield

def test_4():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    assert isinstance(flat_generator(list_of_lists_2), types.GeneratorType)


if __name__ == '__main__':
    test_4()