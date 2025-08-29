import sys

def ft_filter(function, iterable):
    """
    Reimplementation of built-in filter() function
    
    Args:
        function: A function that returns True or False.
        iterable: A list, tuple, string, etc.
        
    If function is filter(None, iterable) keeps only truthy elements.

    Returns:
        iterator: yields only the elements where function(element) is True.
    
    """
    if function is not None:
        return iter([item for item in iterable if function(item)])
    else:
        return iter([item for item in iterable if item])

# def main():
#     numbers = [1, 2, 3, 4, 5, 6]
#     result = ft_filter(lambda x: x % 2 == 0, numbers)
#     print(list(result))
    
#     data = [0, 1, "", "Hello", [], [1, 2]]
#     result = ft_filter(None, data)
#     print(list(result))
        
     
# if __name__ == "__main__":
#     # print(ft_filter.__doc__)
#     main()