label mansion_tutor_evening_D_2:

    scene rcsj_d14 with tstmgr

    d "Ahhhh......我累了."



    d "我可以休息一下吗?我想小睡一会儿."



    player "但是你休息的时候,你的同学都在努力学习."



    scene rcsj_d13 with tstmgr

    d "Huh,你说话像我妈妈."



    player "... ... ... ..."



    $ add(D, D.love, 1)



    $ P.cash.add(100)

    jump playlet_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
