label company_afternoon_C_2:

    scene void with tstmgr

    player "这是你的奶茶."



    scene rcsj_c3 with tstmgr

    c "谢谢你.你现在可以回去工作了."



    player "你还要我给你买别的东西吗?一个三明治?一个冰淇淋?或者是一本杂志?"



    scene rcsj_c5 with tstmgr

    c "这可不像你.发生了什么事?"



    player "Eh...你知道,我刚意识到做你的仆人并没有那么糟糕."



    player "至少我可以暂时逃离我的工作."



    c "... ... ... ..."



    c "把这种事告诉你的经理是不明智的."



    c "但无所谓.你可以在附近的沃尔玛给我买些巧克力.我给你20分钟."



    scene void with tstmgr

    "... ... ... ..."



    $ add(C, C.love, 1)

    jump playlet_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
