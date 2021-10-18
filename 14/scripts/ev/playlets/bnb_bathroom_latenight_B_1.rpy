label bnb_bathroom_latenight_B_1:

    scene bnb_bathroom_latenight_b_1_1 with tstmgr

    b "谢谢你让我用你的浴室."



    player "随时欢迎."



    player "现在很晚了,如果你愿意,可以在这里住一晚."



    scene bnb_bathroom_latenight_b_1_2 with tstmgr

    b "... ... ... ..."



    b "但是............"



    player "你可以睡在我的......"



    a "咳嗽,咳嗽."



    scene bnb_bathroom_latenight_b_1_3 with tstmgr

    a "森柠可以和我一起睡."



    scene bnb_bathroom_latenight_b_1_4 with tstmgr

    b "Yeah,我非常乐意."



    scene bnb_bathroom_latenight_b_1_5 with tstmgr

    a "跟我来,我带你去房间.我们可以聊一整夜女生之间的事."



    scene void with tstmgr

    player "... ... ... ..."



    player "好吧......"



    $ add(B, B.love, 1)

    jump playlet_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
