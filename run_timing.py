import HNFGen as hg
from shutil import copyfile

list = [[hg.base_mono_1, "Base Mono 1"], [hg.base_mono_2, "Base Mono 2"], [hg.base_mono_3, "Base Mono 3"], [hg.base_ortho_1, "Base Ortho 1"], [hg.base_ortho_2, "Base Ortho 2"], [hg.base_ortho_3, "Base Ortho 3"], [hg.body_cubic_1, "Body Cubic 1"], [hg.body_cubic_2, "Body Cubic 2"], [hg.body_cubic_3, "Body Cubic 3"], [hg.body_cubic_4, "Body Cubic 4"], [hg.body_cubic_5, "Body Cubic 5"], [hg.body_cubic_6, "Body Cubic 6"], [hg.body_cubic_7, "Body Cubic 7"], [hg.body_cubic_8, "Body Cubic 8"], [hg.body_ortho_1, "Body Ortho 1"],  [hg.body_ortho_2, "Body Ortho 2"], [hg.body_ortho_3, "Body Ortho 3"], [hg.body_ortho_4, "Body Ortho 4"], [hg.body_tet_1, "Body Tet 1"], [hg.body_tet_2, "Body Tet 2"], [hg.body_tet_3, "Body Tet 3"], [hg.body_tet_4, "Body Tet 4"], [hg.body_tet_5, "Body Tet 5"], [hg.face_ortho_1, "Face Ortho 1"], [hg.face_ortho_2, "Face Ortho 2"], [hg.face_ortho_3, "Face Ortho 3"], [hg.face_ortho_4, "Face Ortho 4"], [hg.face_ortho_5, "Face Ortho 5"], [hg.face_ortho_6, "Face Ortho 6"], [hg.face_ortho_7, "Face Ortho 7"], [hg.face_ortho_8, "Face Ortho 8"], [hg.face_ortho_9, "Face Ortho 9"], [hg.face_ortho_10, "Face Ortho 10"], [hg.s_cubic_1, "Simple Cubic 1"], [hg.s_cubic_2, "Simple Cubic 2"], [hg.s_cubic_3, "Simple Cubic 3"], [hg.s_cubic_4, "Simple Cubic 4"], [hg.s_cubic_5, "Simple Cubic 5"], [hg.trig_1, "Trigonal 1"], [hg.trig_2, "Trigonal 2"], [hg.trig_3, "Trigonal 3"], [hg.trig_4, "Trigonal 4"]]

result_file = open('timing_results.md', 'w')
result_file.write('| Basis | Time |\n')
result_file.write('|-------|------|\n')

for i in list:

    times = hg.timing(i[0])
    result = str(times[2])

    copyfile('func_time.out', '/mnt/c/Users/prkrj/Documents/College/Research/HNF_timing/' + i[1] + '.out')
    result_file.write('| ' + i[1] + ' | ' + result + ' |\n')
    print ('Finished ', i[1])
    
