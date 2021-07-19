label clothing_afternoon_A_1:

    scene a_dressstore_frown with tstmgr

    a "... ... ... ..."



    a "你又来了..."



    a "我得提醒你多少次这是一家女装店?"



    player "Hmm... ..."



    player "Yeah,像我这样的人一个人来这里是有点奇怪."



    scene a_dressstore_smile3 with tstmgr

    a "很高兴你能意识到这一点."



    player "所以...你考虑过换工作吗?你知道,也许去一家男装店?"



    scene a_dressstore_weird with tstmgr

    a "什么?"



    a "你疯了......"



    scene void with tstmgr

    "... ... ... ..."



    $ add(A, A.love, 1)

    jump playlet_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
