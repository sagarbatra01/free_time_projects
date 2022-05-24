def print_iter(iter):
    """Converts iterable to list and prints it."""
    print(list(iter))

def zip_test(*iterables):
    """Test function for the built-in 'zip' method.
    
    This function aims to teach me about how the 'zip' function works,
    and with which data types it is effective.

    Args:
        first, second: two random iterables used for testing.

    Returns:
        A zipped version of the two inputs.

    Raises:
        TypeError: An error occurred while zipping the given data type.
    """
    zipped = zip(*iterables)
    return zipped

def test_zip():
    """Tests the 'zip_test' function.""" 
    tpl = (1,2,3)
    lst = [4,5,6]
    string = "789"
    dct = {"10": 11, "12": 13, "14": 15}
    
    #print_iter(zip_test(tpl)) 
    #print_iter(zip_test(lst))
    #print_iter(zip_test(string))
    #print_iter(zip_test(dct))

    print_iter(zip_test(tpl, lst))
    print_iter(zip_test(dct, string))
    print_iter(zip_test(lst, dct))
    print_iter(zip_test(tpl, string))
    print_iter(zip_test(dct, dct))
    #print_iter(zip_test())
    


def main():
    test_zip()

if __name__ == "__main__":
    main()