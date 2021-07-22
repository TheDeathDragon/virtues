label bnb_livingroom_forenoon_G_1:

    scene void with tstmgr

    "我发现乌诺在客厅里."



    scene bnb_livingroom_forenoon_g_1_1 with tstmgr

    player "早上好."



    scene bnb_livingroom_forenoon_g_1_2 with tstmgr

    g "(点头)............"



    scene bnb_livingroom_forenoon_g_1_3 with tstmgr

    player "你在看什么?"



    g "... ... ... ..."



    g "你似乎并不是真正的想知道."



    g "记住你只有30秒."



    scene void with tstmgr

    "... ... ... ..."



    $ add(G, G.love, 1)

    jump playlet_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
