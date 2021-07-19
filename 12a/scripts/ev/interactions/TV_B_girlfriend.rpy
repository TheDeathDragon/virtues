label TV_B_girlfriend:

    if B.clothes == 1:

        scene b_gf_1_default with tstmgr

    if B.clothes == 2:

        scene b_gf_2_default with tstmgr

    if B.clothes == 3:

        scene b_gf_3_default with tstmgr

    bubble_b "一起看电视吗?"

    bubble_b "听起来不错."



    if B.clothes == 1:

        scene b_gf_1_watchtv_1 with tstmgr

    if B.clothes == 2:

        scene b_gf_2_watchtv_1 with tstmgr

    if B.clothes == 3:

        scene b_gf_3_watchtv_1 with tstmgr

    b "... ... ... ..."

    if B.clothes == 1:

        scene b_gf_1_watchtv_2 with tstmgr

    if B.clothes == 2:

        scene b_gf_2_watchtv_2 with tstmgr

    if B.clothes == 3:

        scene b_gf_3_watchtv_2 with tstmgr

    b "唉...我们又开始了."

    b "你真的很喜欢女孩子的胸,不是吗?"

    if B.clothes == 1:

        scene b_gf_1_watchtv_3 with tstmgr

    if B.clothes == 2:

        scene b_gf_2_watchtv_3 with tstmgr

    if B.clothes == 3:

        scene b_gf_3_watchtv_3 with tstmgr

    b "(呻吟)Wmmmm............"

    b "Oww... [P]... ..."

    if B.clothes == 1:

        scene b_gf_1_watchtv_4 with tstmgr

    if B.clothes == 2:

        scene b_gf_2_watchtv_4 with tstmgr

    if B.clothes == 3:

        scene b_gf_3_watchtv_4 with tstmgr

    if B.clothes in (1, 2):

        b "等等...别......"

        b "(呻吟)Owwww......"

        b "如果我的父母知道我变成了一个这么...坏的女孩...他们会生气的......"

    if B.clothes == 3:

        b "如果我的父母知道我变成了一个这么...脏的女孩...他们会生气的......"

        b "你应该...对此负责......"

        b "Uhh......我的乳头......"

    scene void with tstmgr

    "... ... ... ..."

    jump interaction_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
