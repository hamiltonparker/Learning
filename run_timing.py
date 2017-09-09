import HNFGen as hg
from HNFGen import timing as time
from shutil import copyfile

bases = [[hg.base_mono_1, 'base_mono_1'], [hg.base_mono_2, 'base_mono_2'], [hg.base_mono_3, 'base_mono_3'], [hg.base_ortho_1, 'base_ortho_1'], [hg.base_ortho_2, 'base_ortho_2'], [hg.base_ortho_3, 'base_ortho_3'], [hg.body_cubic_1, 'body_cubic_1'], [hg.body_cubic_2, 'body_cubic_2'], [hg.body_cubic_3, 'body_cubic_3'], [hg.body_cubic_4, 'body_cubic_4'], [hg.body_cubic_5, 'body_cubic_5'], [hg.body_cubic_6, 'body_cubic_6'], [hg.body_cubic_7, 'body_cubic_7'], [hg.body_cubic_8, 'body_cubic_8'], [hg.body_ortho_1, 'body_ortho_1'], [hg.body_ortho_3, 'body_ortho_3'], [hg.body_ortho_4, 'body_ortho_4'], [hg.body_tet_1, 'body_tet_1'], [hg.body_tet_2, 'body_tet_3'], [hg.body_tet_3, 'body_tet_3'], [hg.body_tet_4, 'body_tet_4'], [hg.body_tet_5, 'body_tet_5']]

for i in bases:
    time(i[0])
    copyfile('func_time.out', '/mnt/c/Users/prkrj/Documents/College/Research/HNF_timing/' + i[1])
    print ('Finished ', i[1])

