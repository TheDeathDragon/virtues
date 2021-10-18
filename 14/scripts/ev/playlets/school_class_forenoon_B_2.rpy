label school_class_forenoon_B_2:

    scene school_class_afternoon_b_1_2 with tstmgr

    b "说真的,[P],我知道你的日子不好过..."



    b "但是你不能总是在课堂上睡觉."



    player "Hmmm... ... ... ..."



    player "你是对的.对不起,我只是太累了."



    b "... ... ... ..."



    scene school_class_forenoon_b_1_1 with tstmgr

    b "别担心,下课后我们去我家,我会帮你复习的."



    player "但我更喜欢和你在你家做些别的事情......"



    scene school_class_afternoon_b_1_2 with tstmgr

    b "Huh?... ... ... ..."



    $ add(B, B.love, 1)

    jump playlet_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
