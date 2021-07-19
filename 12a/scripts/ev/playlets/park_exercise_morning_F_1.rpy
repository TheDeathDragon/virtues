label park_exercise_morning_F_1:

    scene void with tstmgr

    "我今天早上在公园碰到瑞秋."



    scene f_wood_smile2 with tstmgr

    f "嗨,我的朋友.我要去慢跑.你要和我一起吗?"



    player "Eh......yeah,当然."



    scene f_wood_frown with tstmgr

    f "为什么听起来你已经很累了?"



    f "你不喜欢和我在一起吗?"



    player "不...绝对不是......"



    player "它只是...太早了.我还有点迷糊."



    scene f_wood_wink with tstmgr

    f "Oh,okay.别担心,慢跑20分钟后你会感觉好些的."



    scene void with tstmgr

    "... ... ... ..."



    $ add(F, F.love, 1)

    jump playlet_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
