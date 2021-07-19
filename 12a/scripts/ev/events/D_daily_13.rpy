label D_daily_13:

    scene d_daily13_1 with tstmgr
    play music happy

    e "下午好,[P],你是来辅导的吗?"



    player "Ehh...yeah,阿姨."



    scene d_daily13_2 with tstmgr

    e "非常感谢你对艾琳的帮助,亲爱的~"



    scene d_daily13_3 with tstmgr

    e "Wmmmm......艾琳的成绩最近下降了一点.我有点担心.你能不能对她再严厉点?"



    player "Oh,当然,这...这是我的职责."



    player "... ... ... ..."



    "Ahdamn,我现在感到很内疚.自从我和艾琳有了亲密的关系后,辅导课就不再是关于辅导了."



    "在辅导课上,我们花了大部分时间在爱抚,逗弄,玩耍上.她成绩的下降完全是我的责任."



    "我需要改变这种情况了......"



    scene void with tstmgr

    "... ... ... ..."



    "我走进艾琳的房间,她已经在等我了..."



    scene d_daily13_4 with dissolve

    d "Meowmeow~~欢迎回家,主人~"



    player "... ... ... ..."



    "Ahh...她又来了,想挑逗我,让我和她做一些色色的事,这样她就能少花点时间在学习上.真是个坏学生..."



    scene d_daily13_5 with tstmgr

    d "Meow~你今天想对我做什么,主人?~"



    player "... ... ... ..."



    label D_daily_13_choice_1:

    menu:
        "做正确的事":


            player "Oh你不知道~我想你会后悔做了我的猫咪..."

            scene d_daily13_10 with tstmgr

            d "你要对我做一些古奇怪的事吗?Meow~"

            player "Hmmmm......yeah,我想是的......"

            scene d_daily13_11 with tstmgr

            d "Awwww~~~我好兴奋!~"

            scene d_daily13_12 with tstmgr

            d "我准备好了!我准备好了!请告诉我你要做什么,主人!~"

            player "Okay,我要你现在就去做作业,做完所有的事之前不要离开你的椅子."

            scene d_daily13_11 with tstmgr

            d "Yes~ yes~~"

            d "... ... ... ..."

            scene d_daily13_13 with tstmgr

            d "Ha?"

            scene d_daily13_14 with tstmgr

            d "等等,你是认真的吗?"

            player "Uh-huh.每个学生都需要做家庭作业."

            scene d_daily13_15 with tstmgr

            d "我们应该好好的玩玩!这是有史以来最无聊的事!"

            player "你的成绩下降了,女孩,你应该保持警惕.小猫咪,别抱怨了,照我说的去做,否则我不会再和你玩这种宠物游戏了."

            scene d_daily13_16 with tstmgr

            d "Awwwwwwww......好吧,我做......"

            "然后艾琳走到她的书桌前开始做作业."

            scene d_daily13_17 with tstmgr

            "... ... ... ..."

            d "[P]是个傻子......"

            player "别说话!专注于你的作业!"

            scene d_daily13_18 with tstmgr

            d "Meow!"

            scene void with tstmgr

            "... ... ... ..."

            "然后,我花了三个小时的时间辅导,并成功地忍住不与艾琳做任何色色的事情~"
        "Ahhh...去他妈的辅导!":




            scene d_daily13_7 with tstmgr

            d "Yaaaahhhh~~~"

            player "又在逃避学习了,坏猫咪?"

            scene d_daily13_6 with tstmgr

            d "我只是想...和我的主人玩得开心,meow~"

            player "唉......好了,小猫咪,忘了辅导吧.在接下来的三个小时里我要好好疼爱你~"

            scene d_daily13_8 with tstmgr

            d "Yes,yes,这正是我想要的~"

            scene d_daily13_9 with tstmgr

            "... ... ... ..."

            "我又一次让欲望控制了我...Damn,我一定是史上最糟糕的私人教师......"

            scene void with tstmgr

            "... ... ... ..."

    stop music fadeout 1.0

    jump event_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
