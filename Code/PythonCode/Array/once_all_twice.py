def find_single_element(elements):

    res = elements[0]
    for item in elements[1:]:
        res^=item
    return res


if __name__ == '__main__':

    elements = [1,3,3,4,4,5,5]
    print(find_single_element(elements))

