'''
Created on Jul 10, 2017

@author: prkrj
'''
import pytest
import copy 
import HNFGen as hg

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

def diff(list1, list2):
    same = False
    difference = []
    for item1 in list1:
        same = False
        for item2 in list2:
            if item1 == item2:
                same = True
                break
        if same == False:
            difference.append(copy.deepcopy(item1))
    print ("Difference:")
    print (difference)
    return    

def test_body_ortho():
    
    correct = read_file("test/output/body_ortho1_10")
    test_output = hg.body_ortho_1(10)
    assert sorted(test_output) == sorted(correct)

    correct = read_file("test/output/body_ortho1_100")
    test_output = hg.body_ortho_1(100)
    assert sorted(test_output) == sorted(correct)

    correct = read_file("test/output/body_ortho2_10")
    test_output = hg.body_ortho_2(10)
    assert sorted(test_output) == sorted(correct)
 
    correct = read_file("test/output/body_ortho3_10")
    test_output = hg.body_ortho_3(10)
    assert sorted(test_output) == sorted(correct)

    correct = read_file("test/output/body_ortho3_100")
    test_output = hg.body_ortho_3(100)
    assert sorted(test_output) == sorted(correct)

    correct = read_file("test/output/body_ortho4_10")
    test_output = hg.body_ortho_4(10)
    assert sorted(test_output) == sorted(correct)

    correct = read_file("test/output/body_ortho4_100")
    test_output = hg.body_ortho_4(100)
    assert sorted(test_output) == sorted(correct)

    print ('Finshed Body Ortho')

def test_base_mono():

    correct = read_file("test/output/base_mono1_10")
    test_output = hg.base_mono_1(10)
    assert sorted(test_output) == sorted(correct)

    correct = read_file("test/output/base_mono1_100")
    test_output = hg.base_mono_1(100)
    assert sorted(test_output) == sorted(correct)

    correct = read_file("test/output/base_mono2_10")
    test_output = hg.base_mono_2(10)
    assert sorted(test_output) == sorted(correct)

    correct = read_file("test/output/base_mono3_10")
    test_output = hg.base_mono_3(10)
    assert sorted(test_output) == sorted(correct)

    correct = read_file("test/output/base_mono3_100")
    test_output = hg.base_mono_3(100)
    assert sorted(test_output) == sorted(correct)

    print ('Finished Base Mono')

def test_base_ortho():

    correct = read_file("test/output/base_ortho1_10")
    test_output = hg.base_ortho_1(10)
    assert sorted(test_output) == sorted(correct)
    
    correct = read_file("test/output/base_ortho1_100")
    test_output = hg.base_ortho_1(100)
    assert sorted(test_output) == sorted(correct)

    correct = read_file("test/output/base_ortho2_10")
    test_output = hg.base_ortho_2(10)
    assert sorted(test_output) == sorted(correct)

    correct = read_file("test/output/base_ortho2_100")
    test_output = hg.base_ortho_2(100)
    assert sorted(test_output) == sorted(correct)

    correct = read_file("test/output/base_ortho3_10")
    test_output = hg.base_ortho_3(10)
    assert sorted(test_output) == sorted(correct)

    correct = read_file("test/output/base_ortho3_100")
    test_output = hg.base_ortho_3(100)
    assert sorted(test_output) == sorted(correct)

    correct = read_file("test/output/base_ortho3_10")
    test_output = hg.base_ortho_3(10)
    assert sorted(test_output) == sorted(correct)

    correct = read_file("test/output/base_ortho3_100")
    test_output = hg.base_ortho_3(100)
    assert sorted(test_output) == sorted(correct)

def test_body_cubic():
  
    correct = read_file("test/output/body_cubic1_8")
    test_output = hg.body_cubic_1(8)
    assert sorted(test_output) == sorted(correct)

    correct = read_file("test/output/body_cubic1_108")
    test_output = hg.body_cubic_1(108)
    assert sorted(test_output) == sorted(correct)

    assert hg.body_cubic_1(10) == []

    correct = read_file("test/output/body_cubic2_8")
    test_output = hg.body_cubic_2(8)
    assert sorted(test_output) == sorted(correct)

    correct = read_file("test/output/body_cubic2_108")
    test_output = hg.body_cubic_2(108)
    assert sorted(test_output) == sorted(correct)

    assert hg.body_cubic_2(10) == []

    correct = read_file("test/output/body_cubic3_8")
    test_output = hg.body_cubic_3(8)
    assert sorted(test_output) == sorted(correct)

    correct = read_file("test/output/body_cubic3_108")
    test_output = hg.body_cubic_3(108)
    assert sorted(test_output) == sorted(correct)

    assert hg.body_cubic_3(10) == []

    correct = read_file("test/output/body_cubic4_8")
    test_output = hg.body_cubic_4(8)
    assert sorted(test_output) == sorted(correct)

    correct = read_file("test/output/body_cubic4_108")
    test_output = hg.body_cubic_4(108)
    assert sorted(test_output) == sorted(correct)

    assert hg.body_cubic_4(10) == []

    correct = read_file("test/output/body_cubic5_8")
    test_output = hg.body_cubic_5(8)
    assert sorted(test_output) == sorted(correct)

    correct = read_file("test/output/body_cubic5_108")
    test_output = hg.body_cubic_5(108)
    assert sorted(test_output) == sorted(correct)

    assert hg.body_cubic_5(10) == []

    correct = read_file("test/output/body_cubic6_8")
    test_output = hg.body_cubic_6(8)
    assert sorted(test_output) == sorted(correct)

    correct = read_file("test/output/body_cubic6_108")
    test_output = hg.body_cubic_6(108)
    assert sorted(test_output) == sorted(correct)

    assert hg.body_cubic_6(10) == []

    correct = read_file("test/output/body_cubic7_8")
    test_output = hg.body_cubic_7(8)
    assert sorted(test_output) == sorted(correct)

    correct = read_file("test/output/body_cubic7_108")
    test_output = hg.body_cubic_7(108)
    assert sorted(test_output) == sorted(correct)

    assert hg.body_cubic_7(10) == []

    correct = read_file("test/output/body_cubic8_8")
    test_output = hg.body_cubic_8(8)
    assert sorted(test_output) == sorted(correct)

    correct = read_file("test/output/body_cubic8_108")
    test_output = hg.body_cubic_8(108)
    assert sorted(test_output) == sorted(correct)

    assert hg.body_cubic_8(10) == []

def test_body_tet():

    correct = read_file("test/output/body_tet1_10")
    test_output = hg.body_tet_1(10)
    assert sorted(test_output) == sorted(correct)

    correct = read_file("test/output/body_tet1_100")
    test_output = hg.body_tet_1(100)
    assert sorted(test_output) == sorted(correct)

    correct = read_file("test/output/body_tet2_10")
    test_output = hg.body_tet_2(10)
    assert sorted(test_output) == sorted(correct)

    correct = read_file("test/output/body_tet2_100")
    test_output = hg.body_tet_2(100)
    assert sorted(test_output) == sorted(correct)

    correct = read_file("test/output/body_tet3_10")
    test_output = hg.body_tet_3(10)
    assert sorted(test_output) == sorted(correct)

    correct = read_file("test/output/body_tet3_100")
    test_output = hg.body_tet_3(100)
    assert sorted(test_output) == sorted(correct)

    correct = read_file("test/output/body_tet4_10")
    test_output = hg.body_tet_4(10)
    assert sorted(test_output) == sorted(correct)

    correct = read_file("test/output/body_tet4_100")
    test_output = hg.body_tet_4(100)
    assert sorted(test_output) == sorted(correct)

    correct = read_file("test/output/body_tet5_10")
    test_output = hg.body_tet_5(10)
    assert sorted(test_output) == sorted(correct)

    correct = read_file("test/output/body_tet5_100")
    test_output = hg.body_tet_5(100)
    assert sorted(test_output) == sorted(correct)

def test_face_ortho():
    
    correct = read_file("test/output/face_ortho1_10")
    test_output = hg.face_ortho_1(10)
    assert sorted(test_output) == sorted(correct)

    correct = read_file("test/output/face_ortho1_100")
    test_output = hg.face_ortho_1(100)
    assert sorted(test_output) == sorted(correct)

    correct = read_file("test/output/face_ortho2_10")
    test_output = hg.face_ortho_2(10)
    assert sorted(test_output) == sorted(correct)

    correct = read_file("test/output/face_ortho2_100")
    test_output = hg.face_ortho_2(100)
    assert sorted(test_output) == sorted(correct)

    correct = read_file("test/output/face_ortho3_10")
    test_output = hg.face_ortho_3(10)
    assert sorted(test_output) == sorted(correct)

    correct = read_file("test/output/face_ortho3_100")
    test_output = hg.face_ortho_3(100)
    assert sorted(test_output) == sorted(correct)

    correct = read_file("test/output/face_ortho4_10")
    test_output = hg.face_ortho_4(10)
    assert sorted(test_output) == sorted(correct)

    correct = read_file("test/output/face_ortho4_100")
    test_output = hg.face_ortho_4(100)
    assert sorted(test_output) == sorted(correct)

    correct = read_file("test/output/face_ortho5_10")
    test_output = hg.face_ortho_5(10)
    assert sorted(test_output) == sorted(correct)

    correct = read_file("test/output/face_ortho5_100")
    test_output = hg.face_ortho_5(100)
    assert sorted(test_output) == sorted(correct)

    correct = read_file("test/output/face_ortho6_10")
    test_output = hg.face_ortho_6(10)
    assert sorted(test_output) == sorted(correct)

    correct = read_file("test/output/face_ortho6_100")
    test_output = hg.face_ortho_6(100)
    assert sorted(test_output) == sorted(correct)

    correct = read_file("test/output/face_ortho7_10")
    test_output = hg.face_ortho_7(10)
    assert sorted(test_output) == sorted(correct)

    correct = read_file("test/output/face_ortho7_100")
    test_output = hg.face_ortho_7(100)
    assert sorted(test_output) == sorted(correct)

    correct = read_file("test/output/face_ortho8_10")
    test_output = hg.face_ortho_8(10)
    assert sorted(test_output) == sorted(correct)

    correct = read_file("test/output/face_ortho8_100")
    test_output = hg.face_ortho_8(100)
    assert sorted(test_output) == sorted(correct)

    correct = read_file("test/output/face_ortho9_10")
    test_output = hg.face_ortho_9(10)
    assert sorted(test_output) == sorted(correct)

    correct = read_file("test/output/face_ortho9_100")
    test_output = hg.face_ortho_9(100)
    assert sorted(test_output) == sorted(correct)

    correct = read_file("test/output/face_ortho10_10")
    test_output = hg.face_ortho_10(10)
    assert sorted(test_output) == sorted(correct)

    correct = read_file("test/output/face_ortho10_100")
    test_output = hg.face_ortho_10(100)
    assert sorted(test_output) == sorted(correct)

def test_s_cubic():

    correct = read_file("test/output/s_cubic1_8")
    test_output = hg.s_cubic_1(8)
    assert sorted(test_output) == sorted(correct)

    correct = read_file("test/output/s_cubic1_108")
    test_output = hg.s_cubic_1(108)
    assert sorted(test_output) == sorted(correct)

    assert hg.s_cubic_1(10) == []

    correct = read_file("test/output/s_cubic2_8")
    test_output = hg.s_cubic_2(8)
    assert sorted(test_output) == sorted(correct)

    correct = read_file("test/output/s_cubic2_108")
    test_output = hg.s_cubic_2(108)
    assert sorted(test_output) == sorted(correct)

    assert hg.s_cubic_2(10) == []
    
    correct = read_file("test/output/s_cubic3_8")
    test_output = hg.s_cubic_3(8)
    assert sorted(test_output) == sorted(correct)

    correct = read_file("test/output/s_cubic3_108")
    test_output = hg.s_cubic_3(108)
    assert sorted(test_output) == sorted(correct)

    assert hg.s_cubic_3(10) == []

    correct = read_file("test/output/s_cubic4_8")
    test_output = hg.s_cubic_4(8)
    assert sorted(test_output) == sorted(correct)

    correct = read_file("test/output/s_cubic4_108")
    test_output = hg.s_cubic_4(108)
    assert sorted(test_output) == sorted(correct)

    assert hg.s_cubic_4(10) == []

    correct = read_file("test/output/s_cubic5_8")
    test_output = hg.s_cubic_5(8)
    assert sorted(test_output) == sorted(correct)

    correct = read_file("test/output/s_cubic5_108")
    test_output = hg.s_cubic_5(108)
    assert sorted(test_output) == sorted(correct)

    assert hg.s_cubic_5(10) == []

def test_trig():
    
    correct = read_file("test/output/trig1_10")
    test_output = hg.trig_1(10)
    assert sorted(test_output) == sorted(correct)

    correct = read_file("test/output/trig1_100")
    test_output = hg.trig_1(100)
    print (correct)
    print (test_output)
    assert sorted(test_output) == sorted(correct)

    correct = read_file("test/output/trig2_10")
    test_output = hg.trig_2(10)
    assert sorted(test_output) == sorted(correct)

    correct = read_file("test/output/trig2_100")
    test_output = hg.trig_2(100)
    assert sorted(test_output) == sorted(correct)

    correct = read_file("test/output/trig3_10")
    test_output = hg.trig_3(10)
    assert sorted(test_output) == sorted(correct)

    correct = read_file("test/output/trig3_100")
    test_output = hg.trig_3(100)
    assert sorted(test_output) == sorted(correct)

    correct = read_file("test/output/trig4_10")
    test_output = hg.trig_4(10)
    assert sorted(test_output) == sorted(correct)

    correct = read_file("test/output/trig4_100")
    test_output = hg.trig_4(100)
    assert sorted(test_output) == sorted(correct)
