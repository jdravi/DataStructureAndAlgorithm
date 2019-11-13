from Cython.Utils import OrderedSet

class DuplicateRemoval:

    def remove_duplicate(self,string):
        """

        :param string:
        :return: return uniques string char with using set
        """

        set = OrderedSet(string)

        for each_char in string:
            set.add(each_char)
        return "".join(set)

    def remove_duplicate_char(self,string):
        """
        :param string: request string
        :return: unique character string
        """
        char_array = [0]*26
        char_list = list(string)
        end_index = 0
        for index in range(len(char_list)):
            asc = ord(char_list[index])-97
            if( char_array[asc]== 0):
                char_array[asc] = 1
                char_list[end_index] = char_list[index]
                end_index = end_index+1
        return  "".join(char_list[0:end_index])


if __name__=='__main__':

    string = "geekks"
    d = DuplicateRemoval()
    print(d.remove_duplicate_char(string))
    print(d.remove_duplicate(string))


