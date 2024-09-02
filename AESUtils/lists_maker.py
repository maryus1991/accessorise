import math


def lists_maker(item: list, slicer_count=2):
    length = len(item) / slicer_count
    length = int(math.floor(length))
    return_list = []
    slicer_counter = 0
    while slicer_counter <= length * slicer_count:
        if slicer_counter + length <= len(item):
            return_list.append(item[slicer_counter:slicer_counter + length])
            del item[slicer_counter:slicer_counter + length]
            slicer_counter += length
        else:

            return_list.append(item)
            break
    return return_list



