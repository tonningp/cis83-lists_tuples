import list_utils
import cis83_sequences as listdemo
import cis83_tuples as tupledemo

if __name__ == '__main__':
    listdemo.lists_as_sequences()
    listdemo.lists_are_mutable()
    t = tupledemo.tuples_are_immutable()
    l = list_utils.lo_shu()
    print(l)
    list_utils.spiralPrint([
        [1,2,3,4,5,6],
        [7,8,9,10,11,12],
        [13,14,15,16,17,18]
    ])
    a = list_utils.rotate_list([2, 7, 6, 9, 5, 1, 4, 3, 8],3)
    print(a)
    a = list_utils.rotate_list(a,3)
    print(a)
    a = list_utils.rotate_list(a,3)
    print(a)
