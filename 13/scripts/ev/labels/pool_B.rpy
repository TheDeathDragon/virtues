label pool_B:
    menu:
        "在梯子那儿等她" if True:
            jump pool_B.b_pool_1
        "和她一起去游泳池" if True:

            jump pool_B.b_pool_2

    jump pool.end

label pool_B.b_pool_1:

    scene b_pool_1_1 with tstmgr

    b "我...我还是有点...害怕进入水中......"



    b "你能给我只手吗?"



    scene b_pool_1_2 with tstmgr

    player "当然,森,我会陪着你的~"



    b "Emmmm?你为什么抓着我的屁股?"



    player "Well,啊这......"



    scene b_pool_1_3 with tstmgr

    player "*把脸埋在森柠的屁股里*我怎么能错过品尝美味屁股的机会呢?"



    scene b_pool_1_4 with tstmgr

    b "Awwwww......等等~~~"



    scene b_pool_1_5 with tstmgr

    b "我是让你给我只手,不是让你......"



    scene b_pool_1_6 with tstmgr

    b "Yaaaaaaaaaahhhh~~~~~~~"



    scene b_pool_1_7 with tstmgr

    b "Awwwwwww~~~~~"



    scene b_pool_1_8 with tstmgr

    b "... ... ... ..."



    player "Eh,森?"



    scene b_pool_1_9 with tstmgr

    b "*在水中冒泡*............"



    b "你欺负我."



    player "什么?不,我没有."



    player "... ... ... ..."



    player "好了,抱歉,森,是我的错.来吧,我现在教你游泳~"



    scene b_pool_1_10 with tstmgr

    b "我不想再让你教我了.我要去找狄奥多拉.她一定是一个比你更好的老师."



    player "Awwww......森,我怎样做才能得到你的原谅?做什么都行!"



    b "... ... ... ..."



    scene b_pool_1_11 with tstmgr

    b "*在水中冒泡*............"



    player "森?"



    scene b_pool_1_12 with tstmgr

    $ flashlight()

    b "惊喜!我真的骗到你了!我一点也不怪你,我们去游泳吧!~"



    player "Wow...女孩,你什么时候把衣服都脱了?"



    scene b_pool_1_13 with tstmgr

    b "你喜欢吗......"



    scene b_pool_1_14 with tstmgr

    player "Awww,森,你不知道你在水里有多美~"



    b "[P]... ... ... ..."



    scene b_pool_1_15 with tstmgr

    b "等等,我的眼镜去哪了?"



    scene b_pool_1_16 with tstmgr

    b "Ohno!我把它掉在水里了!"



    player "Eh... ... ... ..."



    scene void with tstmgr

    "然后我们一直在找森柠的眼镜."



    "... ... ... ..."

    jump pool.end

label pool_B.b_pool_2:

    scene void with tstmgr

    "... ... ... ..."



    scene b_pool_2_16 with dissolve

    player "Yes,yes,你做得对."



    player "放松身体,让浮力起作用~"



    scene b_pool_2_1 with tstmgr

    b "[P]...听起来很专业~"



    scene b_pool_2_2 with tstmgr

    b "但是你也不擅长游泳~Haha~"



    player "Well,至少我能浮在水里.那我就足够当你的第一个游泳老师了~"



    scene b_pool_2_3 with tstmgr

    b "Okay,[P]老师!~"



    scene b_pool_2_4 with tstmgr

    b "但是...我们什么时候开始下一节课?我觉得我现在已经可以浮起来了."



    player "你确定吗?好吧,我们来加点料~"



    scene b_pool_2_5 with tstmgr

    b "Hmmmm?你在干什么?"



    scene b_pool_2_6 with tstmgr

    "我在水下脱下了她的胸罩..."



    b "[P]...请集中精力教我..."



    player "我在集中精力呢~你需要让自己不要因为这样的分心而沉下去."



    scene b_pool_2_7 with tstmgr

    b "Awwww......但你只是在占我便宜!"



    player "那就去告我性骚扰吧~我不在乎~"



    scene b_pool_2_8 with tstmgr

    player "我现在唯一关心的就是我手里的这对软水球."



    player "它们随着水流动,ohmy......我爱死它们了~"



    scene b_pool_2_9 with tstmgr

    b "坏老师~"



    scene b_pool_2_10 with tstmgr

    pause



    scene b_pool_2_11 with tstmgr

    pause



    b "Awwwmmmm~~~~ hummmm~~~"



    scene b_pool_2_12 with tstmgr

    pause



    player "森............"



    b "[P]~~"



    scene b_pool_2_13 with tstmgr

    b "Emmmm?有点不对劲!"



    scene b_pool_2_14 with tstmgr

    b "浮力不起作用了!Awwwww~~"



    player "Ha!~告诉过你这并不容易~"



    scene b_pool_2_15 with tstmgr

    b "*在水里说话*pu-lupu-lupu-lupu-lu............"



    scene void with tstmgr

    "... ... ... ..."

    jump pool.end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
