label C_daily_6:

    scene void with tstmgr
    play music sorrow

    "我去上班的路上,在电梯里又遇到了狄奥."



    "而且...我意识到有些事情不对劲."



    scene c_daily6_1 with tstmgr

    "那是早上的高峰时间,电梯里非常拥挤.人们站得很近."



    "狄奥多拉被三个人包围着."



    scene c_daily6_2 with tstmgr

    "我不知道他们的名字.这是一家大公司,所以他们可能在不同的楼层工作.我猜狄奥多拉也不知道他们的名字.毕竟,她只是一个部门经理."



    "我看到这三个人把他们的手和胳膊放在狄奥多拉的身上,假装是被人群挤到的样子."



    "但是他们满足的表情出卖了他们.妈的,这群混蛋."



    "狄奥多拉看起来有点不自在.她一定意识到了什么,但她似乎在默默地忍受着."



    "我该怎么办?"



    label C_daily_6_choice_1:

    menu:
        "什么也不做.":


            "也许我应该让她自己处理这种情况."

            "我是说,她不寻求帮助可能是有原因的.也许那些人是她的主管?我不知道.但我最好什么都不做."

            "如果他们更进一步,她肯定会寻求帮助,所以..."

            "我不需要太担心."

            scene void with tstmgr

            "... ... ... ..."

            "几分钟后,狄奥多拉和我一起离开了电梯."

            scene c_daily6_8 with tstmgr

            player "So... ..."

            player "关于电梯里发生的事......"

            player "你为什么不向别人求助呢?"

            c "... ... ... ..."

            scene c_daily6_9 with tstmgr

            c "那些人不是傻瓜.他们只是用手肘和手背碰了碰我的身体.我没有任何确凿的证据."

            player "但是......"

            c "别为我担心.这种程度的性骚扰对职业女性来说是不可避免的.我已经习惯了."

            scene c_daily6_8 with tstmgr

            c "我以为你会帮我的.但是...算了."

            player "抱歉......"

            c "没有必要.我不会因此而责备你."

            scene c_daily6_9 with tstmgr

            c "我要去办公室了.如果你有问题,来那里找我."

            scene void with tstmgr

            "... ... ... ..."
        "帮助她.":




            scene c_daily6_3 with tstmgr

            "我穿过人群,靠近了她.她看到我来,有点吃惊."

            c "你做什......"

            scene c_daily6_4 with tstmgr

            "我把站在她身边的人推开,用胳膊护住她周身的地方."

            player "Eh,早上好,经理."

            c "... ... ... ..."

            scene c_daily6_5 with tstmgr

            c "(低语)你是在...帮我吗?"

            player "我......"

            c "... ... ... ..."

            c "(低语)谢谢."

            scene c_daily6_6 with tstmgr

            "她靠近我我,在我耳边低声说道."

            c "看来你已经变成了一个比我想象中更好的人."

            scene c_daily6_7 with tstmgr

            "在接下来的一秒钟里,她稍微动了动她的头,把她柔软的嘴唇轻轻地贴在我的嘴唇上."

            "这一切发生得太快了,我甚至来不及反应."

            "但是...那感觉...真他妈的好."

            scene void with tstmgr

            "这种神奇的体验只持续了一秒钟,我们就到了我们的楼层.然后我们一起走出了电梯."

            "不一会儿..."

            scene c_daily6_8 with tstmgr

            player "Eh...你介意我问一下......"

            player "那是什么...吻?"

            c "... ... ... ..."

            scene c_daily6_9 with tstmgr

            c "没什么.这只是对你帮助的酬谢."

            scene c_daily6_10 with tstmgr

            c "别太认真了,小处男."

            player "Oh... okay... ..."

            player "顺便说一句,我不喜欢你那样叫我."

            player "还有电梯里发生的事......"

            player "你为什么不向别人求助呢?"

            scene c_daily6_8 with tstmgr

            c "... ... ... ..."

            c "那些人不是傻瓜.他们只是用手肘和手背碰我的身体.我没有任何确凿的证据."

            player "但是......"

            scene c_daily6_9 with tstmgr

            c "别为我担心.这种程度的性骚扰对职业女性来说是不可避免的.我已经习惯了."

            scene c_daily6_8 with tstmgr

            player "这对你来说一定很难.性骚扰是最糟糕的事了."

            scene c_daily6_10 with tstmgr

            c "真的吗?我想如果你发现一个女孩在公共场合摸你的裆部,你会很高兴的."

            player "... ... ... ..."

            player "如果是个漂亮的女孩,也许我会喜欢."

            scene c_daily6_11 with tstmgr

            c "如果你是那个骚扰我的人,我也会喜欢的."

            player "什么???"

            scene c_daily6_10 with tstmgr

            c "... ... ... ..."

            c "我要去办公室了.如果你有问题,来那里找我."

            scene void with tstmgr

            "... ... ... ..."

    stop music fadeout 1.0









    jump event_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
