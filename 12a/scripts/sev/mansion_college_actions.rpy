label mansion_bathroom:
    scene mansion_bathroom_background with tstmgr
    "这是这所房子的主浴室,它可能比我的房间还大."
    jump action_post

label mansion_toilet:
    scene mansion_toilet_background with tstmgr
    "这只是个厕所."
    jump action_post

label mansion_guestroom:
    scene mansion_guestroom_background with tstmgr
    "我以前住在这个房间里,这里充满了回忆."
    jump action_post

label mansion_pool:
    if is_day():
        scene mansion_swimpool_day_background with tstmgr
    elif True:
        scene mansion_swimpool_night_background with tstmgr
    "为什么我在一个没有人的游泳池里?"
    jump action_post

label mansion_livingroom:
    "我检查了一下,一切正常."
    jump action_post

label college_bathroom:
    "这是女浴室,我不能进去."
    jump action_post

label campus:
    scene school_day_background with tstmgr
    "我花了一些时间在校园里散步."
    jump action_post

label library:
    scene library_background with tstmgr
    "我花了一些时间在图书馆学习."
    $ time_proceed(1)
    jump action_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
