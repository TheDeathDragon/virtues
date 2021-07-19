label TV_D_general:

    if D.clothes == 1:

        scene d_general_1_default with tstmgr

    if D.clothes == 2:

        scene d_general_2_default with tstmgr







    bubble_d "棒!是时候休息了."

    bubble_d "你是最棒的,[P]!"



    if D.clothes == 1:

        scene d_general_1_watchtv_1 with tstmgr

    if D.clothes == 2:

        scene d_general_2_watchtv_1 with tstmgr







    d "... ... ... ..."

    d "就像我坐在一个沙发怪物上."



    if D.clothes == 1:

        scene d_general_1_watchtv_2 with tstmgr

    if D.clothes == 2:

        scene d_general_2_watchtv_2 with tstmgr







    d "Oww...好痒......"

    d "坏沙发,坏沙发..."



    if D.clothes == 1:

        scene d_general_1_watchtv_3 with tstmgr

    if D.clothes == 2:

        scene d_general_2_watchtv_3 with tstmgr







    d "但无所谓.我喜欢你吻我的脸."

    d "我的皮肤比狄奥多拉还软,你不觉得吗?"

    jump interaction_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
