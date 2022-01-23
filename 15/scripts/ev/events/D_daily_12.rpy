label D_daily_12:

    scene void with tstmgr

    play music happy

    if _in_replay:
        "为了重演这个情节,我得先知道这个."
        menu:
            "狄奥多拉搬进了你的房子":
                jump D_daily_12.line_a
            "狄奥多拉还没搬进你的房子":
                jump D_daily_12.line_b
    else:
        if seen("C_daily_12"):
            jump D_daily_12.line_a
        else:
            jump D_daily_12.line_b

    jump event_post

label D_daily_12.end:

    stop music fadeout 1.0

    jump event_post

label D_daily_12.line_a:

    "*门铃的声音*叮咚~叮咚~"

    d "Hello!有人在家吗?乌诺?我们去看电影吧!"

    scene d_daily12_24 with dissolve

    c "*打开门*Ahhh......我真的不想打开这扇门......"

    scene d_daily12_25 with tstmgr

    d "狄奥多拉?你在这里做什么?"

    c "我现在住在这里.妈妈没告诉你吗?"

    scene d_daily12_26 with tstmgr

    d "什么?你和[P]住在一起了?这太不公平了!"

    c "Hah,我们下个月就要结婚了."

    scene d_daily12_27 with tstmgr

    d "什么鬼?!"

    scene void with tstmgr

    $ flashlight()

    "???" "Uhhhhhhhhhh!!!!!什么?!!!!"

    scene d_daily12_28 with dissolve

    c "Hmmmm?"

    scene d_daily12_29 with tstmgr

    d "*躲在狄奥多拉后面*Awwwww......"

    scene d_daily12_32 with tstmgr

    b "Mamamamama...结婚?"

    "看来艾琳并没有关门,森柠只是跟着她进来的."

    scene d_daily12_30 with tstmgr

    c "Ah,你一定就是森柠了.[P]告诉过我关于你的事."

    c "我叫狄奥多拉,一个...租户.我开个玩笑,你不要当真."

    scene d_daily12_31 with tstmgr

    c "这是我的妹妹,艾琳."

    scene d_daily12_33 with tstmgr

    b "很高兴认识你.我...我很抱歉.我反应过度了......"

    scene d_daily12_34 with tstmgr

    d "Yeah,你最好道歉,小姐!你吓到我了!"

    scene d_daily12_35 with tstmgr

    $ flashlight()

    b "Yaaaaaaaahhh!!!"

    scene d_daily12_29 with tstmgr

    d "*又躲在狄奥多拉后面*Awwwwww......她什么毛病?"

    b "*喃语*好可爱......"

    c "啊哈?"

    b "*喃语*艾琳...太可爱了......"

    scene d_daily12_36 with tstmgr

    d "Oh,谢谢你这么说.你也很可爱~"

    scene d_daily12_37 with tstmgr

    d "等等,不,陌生的女士!你又吓到我了!你一点都不可爱!"

    b "*使劲吞咽*............"

    c "你看起来不太好.你还好吗,森柠?"

    b "我...我很好.我很好,只是......"

    scene d_daily12_38 with tstmgr

    b "我从来没见过...有人能...这么可爱......"

    b "我需要............"

    c "森柠?"

    scene d_daily12_39 with tstmgr

    "森柠突然失去平衡,向前摔倒了."

    c "森柠!"

    d "OhmyGod!她怎么样了?"

    c "... ... ... ..."

    c "典型的低血糖的问题.她因为太激动而晕倒了.我们把她放在地上."

    d "Ohno!她需要救护车吗?我们怎么帮她?"

    c "我想她几分钟内就会恢复正常.这不是什么大问题."

    d "她晕倒是我的错吗?"

    scene d_daily12_40 with tstmgr

    c "我不知道,也许吧......"

    c "她晕倒是因为你...可爱吗?这听起来...怪怪的......"

    scene d_daily12_41 with tstmgr

    d "Awwwwww......我很抱歉,虽然我不知道到底发生了什么."

    c "别担心,我们把她送到客厅去,她很快就会好起来的."

    b "好...可爱...卡哇伊......"

    scene void with tstmgr

    "... ... ... ..."

    "*森柠与狄奥多拉和艾琳成了朋友.*"

    "... ... ... ..."

    jump D_daily_12.end

label D_daily_12.line_b:

    "*门铃的声音*叮咚~叮咚~"



    d "Hello!有人在家吗?"



    a "来了~"



    scene d_daily12_1 with tstmgr

    a "*开门*Oh,hi,艾琳.什么风把你吹来了?"



    scene d_daily12_2 with tstmgr

    d "我是来看你和乌诺的!不欢迎吗?~"



    scene d_daily12_3 with tstmgr

    a "Oh,当然欢迎,请进吧~但不幸的是乌诺和[P]现在不在家."



    b "*脸红*............"



    scene d_daily12_4 with tstmgr

    a "Hmm?Oh,抱歉,我忘了介绍了."



    scene d_daily12_5 with tstmgr

    a "森柠,这是艾琳,[P]是她的家庭教师."



    a "艾琳,这位是森宁,[P]的大学朋友~"



    scene d_daily12_6 with tstmgr

    d "很高兴认识你,森柠."



    b "*脸红*............"



    scene d_daily12_7 with tstmgr

    a "森?"



    scene d_daily12_8 with tstmgr

    b "Hi......很高兴...见到你......"



    scene d_daily12_9 with tstmgr

    d "你还好吗?你看起来很糟糕."



    b "*喃语*好可爱......"



    d "啊哈?"



    scene d_daily12_11 with tstmgr

    b "*喃语*你看起来...太可爱了......"



    scene d_daily12_10 with tstmgr

    d "谢谢你这么说.你也很可爱~"



    b "*使劲吞咽*............"



    b "我可以...抱抱你吗,艾琳小姐?"



    d "Hug? Okay~"



    scene d_daily12_12 with tstmgr

    "... ... ... ..."



    b "Awwwwwwww... ..."



    scene d_daily12_13 with tstmgr

    d "Wow...你的心跳得太快了.你确定你没事吗?"



    scene d_daily12_14 with tstmgr

    b "我...我很好.我很好,只是......"



    scene d_daily12_15 with tstmgr

    b "我从来没见过...有人...能像你这么可爱......"



    scene d_daily12_16 with tstmgr

    b "我需要............"



    a "森?"



    scene d_daily12_17 with tstmgr

    "森柠突然失去平衡,向后跌倒."



    scene d_daily12_18 with tstmgr

    a "森!"



    "薇拉在摔倒在地之前及时抓住了森宁."



    scene d_daily12_19 with tstmgr

    d "OhmyGod!她怎么样了?"



    a "[P]有一次告诉我她有低血糖的问题.当她在很短的时间内变得超级兴奋时,她可能会晕倒."



    scene d_daily12_20 with tstmgr

    d "Ohno!她需要救护车吗?我们怎么帮她?"



    a "我...我想她几分钟后就会恢复正常.这不是什么大问题......"



    d "她晕倒是我的错吗?"



    scene d_daily12_21 with tstmgr

    a "Eh...也许吧,我...我不知道......"



    a "她晕倒是因为你...可爱吗?这听起来...怪怪的......"



    scene d_daily12_22 with tstmgr

    d "Awwwwww......我很抱歉,虽然我不知道到底发生了什么."



    a "别担心,我们把她带到客厅去,她几分钟后就会醒."



    a "你们俩会成为好朋友的,我很确定~"



    scene d_daily12_23 with tstmgr

    d "我也想和她做朋友.她看起来像个超级有趣的女孩!~"



    b "好...可爱...卡哇伊......"



    scene void with tstmgr

    "... ... ... ..."



    "*艾琳和森柠成了朋友.*"



    "... ... ... ..."

    jump D_daily_12.end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
