label find_A_restaurant_evening_A_1:

    scene a_restaurant_smile with tstmgr

    a "[P]?"



    player "Hi,薇拉."



    a "我能为你做点什么?"



    player "请给我一杯啤酒.我只是在等你下班."



    scene a_restaurant_slight_surprise with tstmgr

    a "Oh, okay..."



    a "我...我很快就回来."



    scene bar_background with tstmgr

    "... ... ... ..."



    $ add(A, A.love, 1)

    jump playlet_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
