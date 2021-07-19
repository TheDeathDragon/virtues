default sleepers = set()
init python:
    def update_sleepers():
        old_sleepers = sleepers.copy()
        if seen("A_love_5"):
            sleepers.add(A.code)
        if seen("C_daily_12"):
            sleepers.add(C.code)
        if seen("G_love_6"):
            sleepers.add(G.code)
        for nz in (sleepers - old_sleepers):
            Push('You can now sleep with {} at night.'.format(get(nz)))

default sleep_A_count = 0
label sleep_A:

    $ sleep_A_count += 1

    $ rdc = RandomChoice(3)

    if rdc(1):
        scene sleep_a_1 with tstmgr
        player "Oww...薇拉...你很擅长这个..."
        narrator "... ... ... ..."
    elif rdc(2):
        scene sleep_a_2 with tstmgr
        a "我明天还要上班,[P.name].别...做太久了."
    elif True:
        scene sleep_a_3 with tstmgr
        a "停下...我想睡觉..."
        "... ... ... ..."

    $ new_day()

    jump label_post

default sleep_C_count = 0
label sleep_C:

    $ sleep_C_count += 1

    $ rdc = RandomChoice(3)

    if rdc(1):
        scene sleep_c_1 with tstmgr
        c "(梦呓)艾琳...我没有帮你做作业......"
        "... ... ... ..."
    elif rdc(2):
        scene sleep_c_2 with tstmgr
        c "等等~~不要玩我的乳头!~~~"
        "... ... ... ..."
    elif True:
        scene sleep_c_3 with tstmgr
        c "晚安,我的小处男~"
        "... ... ... ..."

    $ new_day()

    jump label_post

default sleep_G_count = 0
label sleep_G:

    $ sleep_G_count += 1

    $ rdc = RandomChoice(3)

    if rdc(1):
        scene sleep_g_1 with tstmgr
        g "等待,等等,别睡~夜晚才刚开始~"
        "... ... ... ..."
    elif rdc(2):
        scene sleep_g_2 with tstmgr
        g "Awwwwwwww~~~~~yes,yes,继续这样操我~~"
        "... ... ... ..."
    elif True:
        scene sleep_g_3 with tstmgr
        g "(梦呓)鸡......炸鸡......"
        "... ... ... ..."

    $ new_day()

    jump label_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
