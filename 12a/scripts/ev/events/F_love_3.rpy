default F_love_3_submit = False
label F_love_3:

    scene f_wood_normal with tstmgr
    play music happy

    player "老实说,我认为你这些天应该尽量不要一个人出去."



    f "Huh?这是为什么?"



    player "我刚看了新闻.上个月这个城市的犯罪率增加了很多."



    scene f_wood_weird with tstmgr

    f "你是认真的吗?这听起来有些可怕."



    scene f_wood_wink with tstmgr

    f "但是别担心.如果我遇到坏人,我可以跑.没有人能赶上我."



    f "即便没法跑,我还可以和他们斗争."



    f "我对自己的能力很有信心."



    player "但是,你知道,当你和别人打架的时候,力量并不是唯一重要的东西."



    player "技术,动作,反应...所有这些都很重要."



    scene f_wood_sharp with tstmgr

    f "... ... ... ..."



    f "听起来你很专业."



    "突然,她的眼睛变得锐利起来."



    f "那我们来比赛吧."



    player "比赛?"



    player "Ehh...okay.但是你想怎么弄?"



    scene f_wood_wink with tstmgr

    f "摔跤,就像他们在WWE(职业摔跤比赛)中做的那样."



    player "你知道WWE并不是真正的战斗,对吧?"



    scene f_wood_surprise with tstmgr

    f "什么???不可能!"



    player "... ... ... ..."



    player "算了,我接受你的挑战.摔跤听起来有趣."



    scene f_wood_wink with tstmgr

    f "太好了.我们去我的房间吧."



    scene void with tstmgr

    "... ... ... ..."



    "过了一会儿,在瑞秋的房间里..."



    "... ... ... ..."



    "Well... shit... ... ... ..."



    scene f_love_3_1 with dissolve



    "原来这个女孩是个怪物."



    "她打起架来就像漫威的黑寡妇.妈的,她真的把我打得够呛."



    "这可能是我一生中最尴尬的时刻之一.感谢上帝,没有其他人看到这个."



    scene f_love_3_2 with tstmgr

    f "服了吗?"



    player "操......"



    "我现在该怎么办?我看不出有什么机会赢."



    "除非............"



    label F_love_3_choice_1:

    menu:
        "认输":


            $ F_love_3_submit = True

            player "(没关系,这只是个游戏.我不需要赢.)"

            player "Okay,女孩.我认输.一个有美德的人总是会承认自己的失败."

            f "Yeah!"

            f "打得不错.我已经很久没有这么开心了.谢谢你!."

            player "Yeah,yeah,不客气."

            player "你得请我吃顿饭,因为我肚子上挨了一拳."

            f "Oh,对此我感到很抱歉."

            f "我碰巧知道附近有个吃烤肉串的好地方."

            "... ... ... ..."
        "耍阴招":




            $ F_love_3_submit = False

            scene f_love_3_1 with tstmgr

            player "一个真正的男人...永远不会...放弃......"

            scene f_love_3_2 with tstmgr

            f "Well,硬汉.你现在还能怎么办?"

            player "至少...我可以..."

            scene f_love_3_3 with tstmgr

            player "这样!"

            "我开始挠她的脚底."

            scene f_love_3_4 with tstmgr

            f "(突然叫了起来)Ahhh............"

            f "这是...新的...招数......"

            f "但如果你想扭转这种局面,这个可远远不够."

            player "这只是个开始,女孩.接招吧!"

            scene f_love_3_5 with tstmgr

            f "这他妈......"

            "我突然用手抓住她的右胸."

            f "还是...不...够......"

            player "那这个呢?"

            scene f_love_3_6 with tstmgr

            f "Owwwww... ... ... ..."

            f "不,我的乳头!"

            scene f_love_3_7 with tstmgr

            f "这是耍诈!规则里没有这个!..."

            player "我们不是在正式比赛,记得吗?现在放开我!"

            f "Ahhh!你真让我生气!"

            scene f_love_3_8 with tstmgr

            $ flashlight()

            f "Ha!现在你不能再用手玩小把戏了!认输,现在!"

            scene f_love_3_9 with tstmgr

            player "Hmmm... ... ... ..."

            player "Well...是的,我现在不能用我的手,但是......"

            scene f_love_3_10 with tstmgr

            player "... ... ... ..."

            f "Emm?等等,这是什么?"

            scene f_love_3_11 with tstmgr

            f "你在做什么?"

            f "你为什么...舔我的短裤?"

            scene f_love_3_12 with tstmgr

            f "这感觉不对.等等,等等..."

            scene f_love_3_13 with tstmgr

            f "Wmmmmmmm............停...停...[P]...停下......"

            player "Yum... yum... yum... yum... ..."

            scene f_love_3_14 with tstmgr

            f "Oh不......"

            f "我感觉我要尿出来了......"

            f "OhmyGod...怎么会这么舒服......"

            f "我感觉不到...我的腿了......"

            scene void with tstmgr

            "... ... ... ..."

            "不一会儿..."

            scene f_love_3_15 with dissolve

            f "(沉重的呼吸)我......我认输......"

            f "你赢了...现在放开我...拜托......"

            scene f_love_3_16 with tstmgr

            player "Yum... yum... yum... yum... ..."

            f "Owww...我受不了."

            player "但我还没弄完呢."

            f "什么?但是我已经认输了."

            scene void with tstmgr

            f "等等...不!!!"

            scene f_love_3_17 with dissolve

            f "(呻吟)Uhhh............"

            f "你为什么...对我这么刻薄?我已经认输了!"

            f "我以为我们是好朋友..."

            player "(舔)Yum...yum...yum......"

            player "你在说什么?我只是想让你舒服点."

            f "Owww... ... ... ..."

            f "但是......"

            scene f_love_3_18 with tstmgr

            f "我要尿了!!!!!............"

            "她达到了高潮.一股水从她的小穴喷了出来,把我的脸都弄湿了."

            scene f_love_3_20 with tstmgr

            player "这很美味......"

            player "你感觉如何,瑞秋?"

            player "瑞秋?"

            "... ... ... ..."

            "她好像晕过去了."

            scene f_love_3_19 with tstmgr

            player "... ... ... ..."

            player "Well...我现在该怎么办?"

            player "这个屁股...我真想从后面操她."

            player "但是...不行,在我对她做了那么多之后,她醒来一定会揍我的."

            player "我最好现在就走."

            scene void with tstmgr

            "... ... ... ..."

    stop music fadeout 1.0

    jump event_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
