label bnb_groom_evening_G_1:

    scene void with tstmgr

    player "(开门)Hey,乌诺,晚餐准备好了.你想......"



    scene bnb_groom_evening_g_1_1 with dissolve

    player "Wow... ... ... ..."



    player "抱歉......"



    scene bnb_groom_evening_g_1_2 with tstmgr

    g "Hmmm?"



    g "谢谢你的邀请,但我现在在节食,所以...我就不吃了."



    player "节食,huh...那么昨晚是谁点的炸鸡?"



    scene bnb_groom_evening_g_1_3 with tstmgr

    g "这就是我为什么现在节食~"



    player "好吧...完美的逻辑."



    "... ... ... ..."



    $ add(G, G.love, 1)

    jump playlet_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
