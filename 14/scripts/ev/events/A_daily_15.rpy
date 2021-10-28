label A_daily_15:


    scene void with tstmgr

    play music happy

    if seen("G_love_1"):
        jump A_daily_15.line_c
    else:
        jump A_daily_15.line_d

    jump event_post

label A_daily_15.end:

    stop music fadeout 1.0

    jump event_post

label A_daily_15.line_c:

    "*下面的情节来自薇拉的视角*"



    scene a_daily15_1 with dissolve

    g "早上还，薇拉... ..."



    scene a_daily15_2 with tstmgr

    a "哦，嗨，乌喏，你今天怎么起得这么早??"



    scene a_daily15_3 with tstmgr

    g "*打哈欠* 啊... ... hh... ...hhh... ..."



    scene a_daily15_4 with tstmgr

    g "我只是上个厕所而已... 马... 马......上就回去睡了."



    a "哦，你想吃点什么早餐吗?"



    scene a_daily15_5 with tstmgr

    g "不，我很好，老妈，谢谢你的关心~."



    scene a_daily15_6 with tstmgr

    a "老妈.......我还没那么老! ~"



    g "Hee hee~~~"



    g "我相信在你有了孩子之后，你会成为一个伟大的母亲~."



    scene a_daily15_7 with tstmgr

    a "一个... 孩子... ..."



    g "你怎么能每天都起得这么早，而且还精力充沛?人生是如此的不公平~."



    g "今晚见，祝你有个愉快的一天~."



    scene a_daily15_8 with tstmgr

    a "好梦~"



    "乌诺离开客厅，又去睡觉了."



    scene a_daily15_9 with tstmgr

    a "... ... ... ..."



    scene a_daily15_10 with tstmgr

    a "(嗯~是时候把[P]叫醒了~.)"



    scene a_daily15_11 with tstmgr

    a "... ... ... ..."



    scene a_daily15_12 with tstmgr

    a "(等一下......我觉得......)"



    scene a_daily15_13 with tstmgr

    a "(Ewwwwww... ...我...我想我要吐了... ...)"



    scene void with tstmgr

    "薇拉以最快的速度跑向厕所，甚至忘了关掉煤气炉......"



    "... ... ... ..."





    "10 minutes later... ..."



    scene a_daily15_14 with dissolve

    a "*离开厕所* 啊... ... 真奇怪，以前从没发生过这种症状."



    scene a_daily15_15 with tstmgr

    a "我是得了胃病吗?"



    a "或者... ... ... ..."



    a "这实际上是一种晨昏颠倒的现象吗?"



    scene a_daily15_16 with tstmgr

    a "我......这个月也没有来月经."



    a "我是不是......怀孕了?"



    scene a_daily15_5 with flashback

    g "我相信在你有了孩子之后，你会成为一个伟大的母亲~."



    scene a_daily15_16 with flashback

    a "哦，亲爱的... ... ... ..."



    scene a_daily15_17 with tstmgr

    a "我这就将成为一个母亲了吗??"



    scene void with tstmgr

    "... ... ... ..."

    jump A_daily_15.end

label A_daily_15.line_d:

    "*下面的情节来自维拉的视角*"



    scene a_daily15_1 with dissolve

    "民宿客人""早上好，薇拉......... ..."



    scene a_daily15_2 with tstmgr

    a "哦，你好，史密斯夫人，早餐已经准备好了."



    "民宿客人" "啊，我很期待这份早餐，但我现在要去参加一个面试，所以......."



    scene a_daily15_8 with tstmgr

    a "没关系~祝你面试成功.你能做到的!"



    "民宿客人" "我会的，谢谢..."



    "民宿客人" "... ... ... ..."



    "民宿客人" "我希望我能有一个像你一样的妈妈... ..."



    scene a_daily15_6 with tstmgr

    a "蛤??"



    "民宿客人" "哦，我是说......你是一个如此贤惠的女人，我只在这里呆了几天，但你已经给了我一种像家人一样被关心的感觉.... ..."



    "民宿客人" "我相信在你有了孩子之后，你会成为一个伟大的母亲.~"



    scene a_daily15_7 with tstmgr

    a "一个... 孩子... ..."



    "民宿客人" "总之，今晚见，薇拉，祝你有个愉快的一天~"



    scene a_daily15_8 with tstmgr

    a "你也是，史密斯夫人~"



    "这位女客人随后离开了，去接受采访.... ..."



    scene a_daily15_9 with tstmgr

    a "... ... ... ..."



    scene a_daily15_10 with tstmgr

    a "(嗯~是时候把[P]叫醒了~)"



    scene a_daily15_11 with tstmgr

    a "... ... ... ..."



    scene a_daily15_12 with tstmgr

    a "(等一下... ... 我觉得... ...)"



    scene a_daily15_13 with tstmgr

    a "(Ewwwwww... ...我...我想我要吐了... ...)"



    scene void with tstmgr

    "薇拉以最快的速度跑向厕所，甚至忘了关掉煤气炉...."



    "... ... ... ..."



    "10 minutes later... ..."



    scene a_daily15_14 with dissolve

    a "离开厕所* 啊... ...这很奇怪，它以前从未发生过."



    scene a_daily15_15 with tstmgr

    a "我是得了胃病吗?"



    a "或者... ... ... ..."



    a "这实际上是一种晨昏颠倒的现象吗?"



    scene a_daily15_16 with tstmgr

    a "我......这个月也没有来月经."



    a "我是不是......怀孕了?"



    scene a_daily15_6 with flashback

    "民宿客人" "我相信在你有了孩子之后，你会成为一个伟大的母亲.~"



    scene a_daily15_16 with flashback

    a "哦，亲爱的... ... ... ..."



    scene a_daily15_17 with tstmgr

    a "我真的会成为一个母亲吗?"



    scene void with tstmgr

    "... ... ... ..."

    jump A_daily_15.end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
