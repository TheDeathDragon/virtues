label park_stroll_morning_B_2:

    scene park_stroll_morning_b_2_1 with tstmgr

    player "森柠?我没想到这么早能在这里见到你."



    b "Hello, [P]."



    b "我昨晚没睡好,所以...决定去公园散步."



    player "昨晚发生了什么事?"



    scene park_stroll_morning_b_2_2 with tstmgr

    b "是我的邻居特蕾莎.她的男朋友昨晚在她的房间里..."



    b "我能听到她整夜的呻吟."



    b "唉......"



    scene void with tstmgr

    player "... ... ... ..."



    $ add(B, B.love, 1)

    jump playlet_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
