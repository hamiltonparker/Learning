import HNFGen as hg
from shutil import copyfile

list = [[hg.base_mono_1, "base_mono_1"], [hg.base_mono_2, "base_mono_2"], [hg.base_mono_3, "base_mono_3"], [hg.base_ortho_1, "base_ortho_1"], [hg.base_ortho_2, "base_ortho_2"], [hg.base_ortho_3, "base_ortho_3"], [hg.body_cubic_1, "body_cubic_1"], [hg.body_cubic_2, "body_cubic_2"], [hg.body_cubic_3, "body_cubic_3"], [hg.body_cubic_4, "body_cubic_4"], [hg.body_cubic_5, "body_cubic_5"], [hg.body_cubic_6, "body_cubic_6"], [hg.body_cubic_7, "body_cubic_7"], [hg.body_cubic_8, "body_cubic_8"], [hg.body_ortho_1, "body_ortho_1"],  [hg.body_ortho_2, "body_ortho_2"], [hg.body_ortho_3, "body_ortho_3"], [hg.body_ortho_4, "body_ortho_4"], [hg.body_tet_1, "body_tet_1"], [hg.body_tet_2, "body_tet_2"], [hg.body_tet_3, "body_tet_3"], [hg.body_tet_4, "body_tet_4"], [hg.body_tet_5, "body_tet_5"], [hg.face_ortho_1, "face_ortho_1"], [hg.face_ortho_2, "face_ortho_2"], [hg.face_ortho_3, "face_ortho_3"], [hg.face_ortho_4, "face_ortho_4"], [hg.face_ortho_5, "face_ortho_5"], [hg.face_ortho_6, "face_ortho_6"], [hg.face_ortho_7, "face_ortho_7"], [hg.face_ortho_8, "face_ortho_8"], [hg.face_ortho_9, "face_ortho_9"], [hg.face_ortho_10, "face_ortho_10"], [hg.s_cubic_1, "s_cubic_1"], [hg.s_cubic_2, "s_cubic_2"], [hg.s_cubic_3, "s_cubic_3"], [hg.s_cubic_4, "s_cubic_4"], [hg.s_cubic_5, "s_cubic_5"], [hg.trig_1, "trig_1"], [hg.trig_2, "trig_2"], [hg.trig_3, "trig_3"], [hg.trig_4, "trig_4"]]

for i in list:

    hg.timing(i[0])

    copyfile('func_time.out', '/mnt/c/Users/prkrj/Documents/College/Research/HNF_timing/' + i[1] + '.out') 
