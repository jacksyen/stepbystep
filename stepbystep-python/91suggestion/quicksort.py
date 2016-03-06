# _*_ coding=utf-8 _*_
__author__ = 'patrick'


def quick_sort(array):
    if len(array) <= 1: return array
    less = [];
    great = []
    pivot = array.pop()

    for i in array:
        if i < pivot:
            less.append(i)
        else:
            great.append(i)

    return quick_sort(less) + [pivot] + quick_sort(great)


if __name__ == '__main__':
    print quick_sort([11, 32, 30, 4, 5, 7, 9, 0, 100])