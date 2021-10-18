label TouchHead_D_girlfriend:


    if D.clothes == 1:

        scene d_gf_1_smile with tstmgr

    if D.clothes == 2:

        scene d_gf_2_smile with tstmgr

    if D.clothes == 3:

        scene d_gf_3_smile with tstmgr

    bubble_d "Yeah,yeah!这听起来不错!"



    if D.clothes == 1:

        scene d_gf_1_touchead_1 with tstmgr

    if D.clothes == 2:

        scene d_gf_2_touchead_1 with tstmgr

    if D.clothes == 3:

        scene d_gf_3_touchead_1 with tstmgr

    if D.clothes in (1, 2):

        d "来嘛,来嘛.用你的手摸我......"

        d "别让我等太久,不然我会咬你的."

    if D.clothes == 3:

        d "来嘛,来嘛.用你的手摸我......"

        d "别让我等太久,不然我会咬你的..."

    if D.clothes == 1:

        scene d_gf_1_touchead_2 with tstmgr

    if D.clothes == 2:

        scene d_gf_2_touchead_2 with tstmgr

    if D.clothes == 3:

        scene d_gf_3_touchead_2 with tstmgr

    if D.clothes == 1:

        d "Wuuuuuuuu... ... ... ..."

        d "Yes,yes,奖励你可爱的小妹妹~~"

    if D.clothes == 2:

        d "Wuuuuuuuu... ... ... ..."

        d "Yes,yes,奖励你的好学生~~"

    if D.clothes == 3:

        d "Ohhh......对不起,我用错词了.咳~咳~"

        d "请...原谅我...主人......"

    if D.clothes == 1:

        scene d_gf_1_touchead_3 with tstmgr

    if D.clothes == 2:

        scene d_gf_2_touchead_3 with tstmgr

    if D.clothes == 3:

        scene d_gf_3_touchead_3 with tstmgr

    if D.clothes == 1:

        d "现在你能给你的小妹妹一个吻吗?"

        d "欧尼酱~~~~"

    if D.clothes == 2:

        d "现在你能给你的学生一个吻吗?"

        d "[P]老师~~~~"

    if D.clothes == 3:

        d "Yes,yes......惩罚我~~随你怎么玩弄我的身体,主人~~"

        d "这是我这个淘气的猫咪应得的~~~"

    scene void with tstmgr

    "... ... ... ..."

    jump interaction_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
