label mansion_tutor_afternoon_D_1:

    scene rcsj_d14 with tstmgr

    d "Ahhhhh......我讨厌数学!"



    player "冷静点,这只是个简单的问题."



    player "耐心点,你就会找到正确的解决办法."



    scene rcsj_d15 with tstmgr

    d "... ... ... ..."



    d "Okay,但是如果我自己解决了这个问题,你需要奖励我."



    player "你在想什么?"



    scene rcsj_d16 with tstmgr

    d "我想玩10分钟手机!"



    player "... ... ... ..."



    $ add(D, D.love, 1)



    $ P.cash.add(100)

    jump playlet_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
