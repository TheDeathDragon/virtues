label B_daily_21:



    scene void with tstmgr
    play music happy

    "... ... ... ..."



    scene b_daily21_1 with dissolve

    "明娜夫人""Hmmm?这不是我最亲爱的孩子吗?"



    player "明娜夫人?下午好......"



    "我注意到明娜夫人后面藏着一个人头."



    player "森?"



    b "Hi, [P]~"



    scene b_daily21_2 with tstmgr

    "明娜夫人""... ... ... ..."



    "明娜夫人""你为什么不给你的男人一个拥抱,小柠檬?"



    scene b_daily21_3 with tstmgr

    b "No... ... ... ..."



    "看起来森柠在她妈妈身边的时候很害羞."



    "明娜夫人""西方男孩喜欢女孩更外向.如果你再这样不活跃的话,[P]很快就会对你感到厌倦的."



    scene b_daily21_4 with tstmgr

    b "不可能,[P]不会厌倦我的~"



    scene b_daily21_5 with tstmgr

    "明娜夫人""Ha...一旦你看到你的对手,你就不会那么自信了."



    scene b_daily21_6 with tstmgr

    b "对手?"



    scene b_daily21_7 with tstmgr

    e "Ah-rah,真巧~"



    c "[P]...和森柠?"



    "明娜夫人""开始了......"



    scene b_daily21_8 with tstmgr

    e "*注意到明娜*Hmmmmm?"



    scene b_daily21_9 with tstmgr

    e "我们...以前见过,对吧,女士?"



    "明娜夫人""Yeah,五年前的一个时装周上.你从我这里买了一件旗袍,现在记起来了吗?"



    scene b_daily21_10 with tstmgr

    e "Ohyeah!你是明娜女士,旗袍女王!"



    scene b_daily21_11 with tstmgr

    "明娜夫人""很高兴你还记得我的名字,伊莉莎~"



    "这两位女士一见面就很投缘,很快就表现得像最好的朋友一样..."



    scene void with tstmgr

    "... ... ... ..."



    scene b_daily21_12 with dissolve

    player "我不知道她们是真的那么亲密还是她们只是装出来的......"



    "狄奥多拉耸了耸肩."



    scene b_daily21_13 with tstmgr

    e "Oh~~看看你,那么年轻,那么漂亮,就像五年前一样.我很嫉妒~"



    scene b_daily21_14 with tstmgr

    "明娜夫人""瞎说~我现在已经是是某人的祖母了~"



    scene b_daily21_13 with tstmgr

    e "那不代表什么.如果我们走在一起,人们会误以为你是我女儿~"



    scene b_daily21_14 with tstmgr

    "明娜夫人""Nope,我不会跟你一起走的.你会抢走我所有的风头~"



    player "... ... ... ..."



    scene b_daily21_15 with tstmgr

    player "想去吃点冰淇淋吗?"



    c "Yeah,有何不可."



    player "... ... ... ..."



    label B_daily_21_choice_1:

    menu:
        "牵森柠的手":


            scene b_daily21_16 with tstmgr

            player "*牵森柠的手*我们走吧~"

            b "[P]~~~"

            c "Huh... ... ... ..."
        "牵狄奥多拉的手":




            scene b_daily21_17 with tstmgr

            player "*牵狄奥多拉的手*我们走吧~"

            c "*有点惊讶*Huh......"

            b "*嘟囔*对...对手............"
        "同时握住她们的手":




            scene b_daily21_18 with tstmgr

            player "Alright,我们走吧~"

            c "*有点惊讶*Huh......"

            b "O... okay~~"



    scene void with tstmgr

    "... ... ... ..."

    stop music fadeout 1.0

    jump event_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
