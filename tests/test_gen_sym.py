'''
Created on Jul 10, 2017

@author: prkrj
'''

from HNFGen import bodyOrtho1, bodyOrtho2, bodyOrtho3, bodyOrtho4
import pytest

def read_file(list_file):
    file = open(list_file, 'r')
    i = 0
    matrix = []
    final_list = []
    for line in file:
        row = line.split()
        if row != []:
            new_row = []
            for value in row:
                new_value = int(value)
                new_row.append(new_value)
            matrix.append(new_row)
            i += 1
            if i == 3:
                final_list.append(matrix)
                matrix = []
                i = 0
    file.close()
    return final_list

def test_gen_sym():
    
    correct = read_file("tests/output/body_ortho1_10")
    test_output = bodyOrtho1(10)
    assert test_output.sort() == correct.sort()
    print ('Finished 1_10')

    correct = read_file("tests/output/body_ortho1_100")
    test_output = bodyOrtho1(100)
    assert test_output.sort() == correct.sort()
    print ('Finished 1_100')
    
    correct = read_file("tests/output/body_ortho2_10")
    test_output = bodyOrtho2(10)
    assert test_output.sort() == correct.sort()
    print ('Finished 2_10')

    correct = read_file("tests/output/body_ortho2_100")
    test_output = bodyOrtho2(100)
    assert test_output.sort() == correct.sort()
    print ('Finished 2_100')
    
    correct = read_file("tests/output/body_ortho3_10")
    test_output = bodyOrtho3(10)
    assert test_output.sort() == correct.sort()
    print ('Finished 3_10')

    correct = read_file("tests/output/body_ortho3_100")
    test_output = bodyOrtho3(100)
    assert test_output.sort() == correct.sort()
    print ('Finished 3_100')

    correct = read_file("tests/output/body_ortho4_10")
    test_output = bodyOrtho4(10)
    assert test_output.sort() == correct.sort()
    print ('Finished 4_10')

    correct = read_file("tests/output/body_ortho4_100")
    test_output = bodyOrtho4(100)
    assert test_output.sort() == correct.sort()
    print ('Finished 4_100')
