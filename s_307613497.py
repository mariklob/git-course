"""
Python Quiz
4 functions.

scoring Per Function:
Total optional points 100.
each function can either receive a score of: 25 points (full points),
                                             OR 12.5 points (half of full points)
                                             OR 0 points (no points)

Point breakdown explained:

    25 points:
        function returns the expected values. With no Violations.

    12.5 points (one or the other)
        function returns an incorrect result (AssertError) without throwing other Exceptions.
        function returns a correct answer BUT disallowed builtin methods or modules were used.

    0 points: (one or the other)
        function throws Any exception other than Assertion error and "Breaks"
        function not answered (body remains empty of code".

RESTRICTIONS:
    DISALLOWED MODULES AND BUILTIN METHODS --> NOT ALLOWED IN ANY FUNCTION SOLUTION
    # min#()#
    # max#()#
    # sorted#()#
    #.# sort#()#
    #.# reverse#()#
    # reversed#()#
    # Numpy #

CHANGES:
        DO NOT CHANGE ANYTHING !!!
        Including the name of the function or the name of the return values.
        you need to fill the function body so the return is as requested
        This will result in disqualifying the function !!!
COMMENTS:
        DO NOT leave any comments of your own in the file you are turning in
        besides the doc string.

Good Luck

"""


def min_max_lst(list_var):
    """
        :param: list_var:
        :return: the smallest and largest value in the list - Result should be a tuple.
        RESTRICTED: See at the Main instruction at the top of the file under:DISALLOWED MODULES AND BUILTIN METHODS
        CHANGES See at the Main instruction at the top of the file Under CHAnGES
        SCORING:SEE See at the Main instruction at the top of the file under SCORING
        EXAMPLE:
            if you run the function with this example_list:
                example_list = [1,4,5,22,3,5,16,4,50,7,3,2,7]
            run:
                min_max_list(example_list)
            This should be your result - a tuple object
                (1, 50)

       DISALLOWED MODULES AND BUILTIN METHODS --> NOT ALLOWED IN ANY FUNCTION SOLUTION

        """

    return min_val, max_val


def reverse_lst(list_var):
    """
        :param: list_var:
        :return: the list in reversed order
        RESTRICTED: See at the Main instruction at the top of the file under:DISALLOWED MODULES AND BUILTIN METHODS
        CHANGES See at the Main instruction at the top of the file Under CHAnGES
        SCORING:SEE See at the Main instruction at the top of the file under SCORING
        EXAMPLE:
            if you run the function with this example_list:
                example_list = [1,4,5,22,3,5,16,4,50,7,3,2,7]
            run:
                reverse_lst(example_list)
           This should be your result - a list object
                [7, 2, 3, 7, 50, 4, 16, 5, 3, 22, 5, 4, 1]

        DISALLOWED MODULES AND BUILTIN METHODS --> NOT ALLOWED IN ANY FUNCTION SOLUTION
        """

    return list_rev


def sorting_lst(list_var):
    """
        :param: list_var:
        :return: the list in a numeric order small to large
        RESTRICTED: See at the Main instruction at the top of the file under:DISALLOWED MODULES AND BUILTIN METHODS
        CHANGES See at the Main instruction at the top of the file Under CHAnGES
        SCORING:SEE See at the Main instruction at the top of the file under SCORING
        EXAMPLE:
            if you run the function with this example_list:
                example_list = [1,4,5,22,3,5,16,4,50,7,3,2,7]
            run:
                sorting_lst(example_list)
            This should be your result - a list object
                [1, 2, 3, 3, 4, 4, 5, 5, 7, 7, 16, 22, 50]

        DISALLOWED MODULES AND BUILTIN METHODS --> NOT ALLOWED IN ANY FUNCTION SOLUTION
    """

    return sorted_list


def unique_values_lst(list_var):
    """
        :param: list_var:
        :return: a list of the unique values each occurring once in the order they appeared first.
        RESTRICTED: See at the Main instruction at the top of the file under:DISALLOWED MODULES AND BUILTIN METHODS
        CHANGES See at the Main instruction at the top of the file Under CHAnGES
        SCORING:SEE See at the Main instruction at the top of the file under SCORING
        EXAMPLE:
            if you run the function with this example_list:
            example_list = [1,4,5,22,3,5,16,4,50,7,3,2,7]
            run:
                unique_values_lst(example_list)
            This should be your result - a list object
                [1, 4, 5, 22, 3, 16, 50, 7, 2]

        DISALLOWED MODULES AND BUILTIN METHODS --> NOT ALLOWED IN ANY FUNCTION SOLUTION
        """
    return u_value