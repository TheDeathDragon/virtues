label TV_D_girlfriend:

    if D.clothes == 1:

        scene d_gf_1_default with tstmgr

    if D.clothes == 2:

        scene d_gf_2_default with tstmgr

    if D.clothes == 3:

        scene d_gf_3_default with tstmgr

    bubble_d "是的,来吧!"

    bubble_d "我想坐在你身上!"



    if D.clothes == 1:

        scene d_gf_1_watchtv_1 with tstmgr

    if D.clothes == 2:

        scene d_gf_2_watchtv_1 with tstmgr

    if D.clothes == 3:

        scene d_gf_3_watchtv_1 with tstmgr

    if D.clothes in (1, 2):

        d "你连电视都没打开.Ohhhh~~~~"

        d "但如果你的按摩能让我的胸变得更大......"

    if D.clothes == 3:

        d "(他把我抱在怀里......这感觉真好.)"

        d "(但他没有发现我的秘密......)"

    if D.clothes == 1:

        scene d_gf_1_watchtv_2 with tstmgr

    if D.clothes == 2:

        scene d_gf_2_watchtv_2 with tstmgr

    if D.clothes == 3:

        scene d_gf_3_watchtv_2 with tstmgr

    if D.clothes in (1, 2):

        d "Wuuuuuuuu!!!~~~~~我的乳头!~~~"

        d "你太坏了,太坏了,我不喜欢你了!"

    if D.clothes == 3:

        d "(他没发现我肛门里的小东西...)"

        d "(也许他下次把他的大鸡儿插进去时会容易些......)"

    if D.clothes == 1:

        scene d_gf_1_watchtv_3 with tstmgr

    if D.clothes == 2:

        scene d_gf_2_watchtv_3 with tstmgr

    if D.clothes == 3:

        scene d_gf_3_watchtv_3 with tstmgr

    if D.clothes in (1, 2):

        d "除非...除非你给我一个法式湿吻..."

        d "就像人们在电影里做的那样............"

    if D.clothes == 3:

        d "(欲望的呻吟)Ahhhh......ahhh......ahhh............"

        player "Hmm?你的脸色看起来怪怪的?怎么了?"

        d "没...没什么......没什么......"

    scene void with tstmgr

    "... ... ... ..."

    jump interaction_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
