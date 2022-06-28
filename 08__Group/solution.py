from itertools import groupby

def group(items):
    result = [list(iterator) for i, iterator in groupby(items)]
    return result

                
group([1, 1, 1, 2, 3, 1, 1])