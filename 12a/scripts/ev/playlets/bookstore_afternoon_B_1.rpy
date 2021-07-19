label bookstore_afternoon_B_1:

    scene g_daily2_9 with tstmgr

    b "下午好,[P]."



    player "Hello,森,你在这儿工作得怎么样?"



    b "还行.这里的人都很友好.我可以感觉到我的英语口语能力正在迅速提高."



    player "我很高兴听到这个,森."



    b "所以......你想买一本书吗?"



    b "连环画,漫画,小说......所有你想要的."



    player "你为什么不带我参观一下呢?"



    scene void with tstmgr

    "... ... ... ..."



    $ add(B, B.love, 1)

    jump playlet_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
