label basic_room:
    jump action_post

default first_clean = True
default clean_count = 0
label clean:
    if first_clean:
        "为了吸引客人,我们没有收取任何保洁费.但是如果我能在他们允许的情况下打扫他们的卧室,也许他们会给我一些小费."
        $ first_clean = False

    if is_day():
        scene home_livingroom_day_background with tstmgr
    elif True:
        scene home_livingroom_night_background with tstmgr
    narrator "我打扫了一会儿房间,从客人那里得到了一些小费."

    $ time_proceed(1)
    $ P.earn (50.0, "小费")
    $ clean_count += 1
    jump action_post

label decorate:

    jump action_post

label new_room:

    jump action_post

label new_facility:

    jump action_post

label frontyard:
    scene home_frontyard_day_background with tstmgr
    "我检查了一下,一切正常."
    jump action_post

label livingroom:
    if is_day():
        scene home_livingroom_day_background with tstmgr
    elif True:
        scene home_livingroom_night_background with tstmgr
    "我检查了一下,一切正常."
    jump action_post

label free_money:
    "... ... ... ..."
    "为什么沙发上有一个袋子."
    "里面是什么..."
    "一叠现金?"
    "还有个备注..."
    "来自开发者的一点帮助.祝你好运(*^▽^*)"
    "... ... ... ..."
    "什么是开发者?这太奇怪了."
    "但是...我想我还是收下这笔钱."
    "... ... ... ..."
    $ P.cash.add(2000)
    $ free_money = True
    jump action_post

label kitchen:
    scene home_kitchen_day_background with tstmgr
    "我检查了一下,一切正常."
    jump action_post

label bathroom:
    scene home_shower_day_background with tstmgr
    "我检查了一下,一切正常."
    jump action_post

label toilet:

    "我检查了一下,一切正常."
    jump action_post

default build_pool_count = 0
label build_pool:
    scene void with tstmgr
    "我花了几个小时建游泳池......"
    $ build_pool_count += 1
    $ time_proceed(1)
    jump action_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
