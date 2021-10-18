label B_daily_8:

    scene void with tstmgr
    play music happy

    "这段时间,我总觉得有些事情困扰着我."



    "这个女孩真的喜欢我吗?"



    "我们每天去上课,一起学习,总是一起出去玩."



    "And... ..."



    scene b_date1_13 with tstmgr

    pause

    scene b_love3_6 with tstmgr

    pause

    scene b_love4_14 with tstmgr

    pause



    scene void with tstmgr

    "我们的关系现在有点暧昧,但我还是不能确定她对我的想法."



    "我是一个潜在的男朋友,还是一个最好的朋友?"



    scene b_daily8_1 with dissolve

    player "... ... ... ..."



    player "(女孩的心思真难猜.)"



    player "(Hmmm...我该怎么办?)"



    scene b_daily8_2 with tstmgr

    "*声响*..."



    scene b_daily8_3 with tstmgr

    player "Uh?"



    scene b_daily8_4 with tstmgr

    "我把头转了一下.接着,我的脸被一个柔软的手指轻轻戳了一下."



    scene b_daily8_5 with tstmgr

    b "逮到你了."



    player "森柠?"



    b "Oh.我打断你的冥想了吗?"



    player "冥想?"



    player "Eh...为什么你会以为我在冥想?"



    b "你站在水池前,像个雕像一样.如果这不是冥想,那么你一定是在想一些麻烦的事情."



    player "... ... ... ..."



    player "Yeah...你是对的.确实有些事使我烦恼."



    scene b_daily8_6 with tstmgr

    b "想说说吗?"



    player "... ... ... ..."



    b "......如果你不想说也没关系.但是如果有什么我能做的,请告诉我."



    player "... ... ... ..."



    scene b_daily8_7 with tstmgr

    player "Oh,森..."



    "我情不自禁地把她搂在怀里.这个女孩是个天使."



    b "等等......"



    "她的身体又轻又小.我感觉自己像抱着一个脆弱的中国娃娃."



    label B_daily_8_choice_1:

    menu:
        "吻她的额头":


            scene b_daily8_8 with tstmgr

            player "*亲吻*......"

            b "(惊讶)Yah!......"

            player "... ... ... ..."

            scene b_daily8_7 with tstmgr

            b "你为什么要吻我?"

            player "Eh...我不知道.就自然而然..."

            scene b_daily8_9 with tstmgr

            b "(似乎有点生气)Wmmm........."

            b "你不能无缘无故地亲一个女孩.这是不礼貌的!"

            player "抱歉......"

            scene b_daily8_10 with tstmgr

            b "... ... ... ..."

            scene b_daily8_11 with tstmgr

            b "(低语)下次...一定要有一个好的理由..."

            player "森............"

            scene b_daily8_12 with tstmgr

            b "*嗅,嗅*......"

            scene b_daily8_11 with tstmgr

            b "你用了一个新香水吗?"

            b "它...蛮好闻的."

            player "Yeah,我很高兴你喜欢."

            b "... ... ... ..."

            b "不说了.现在我要去见一位教授.待会见."

            player "到时候见."

            scene void with tstmgr

            "... ... ... ..."
        "轻拍她的头":




            scene b_daily8_13 with tstmgr

            player "*轻拍*......"

            b "(惊讶)Yah!......"

            player "... ... ... ..."

            scene b_daily8_7 with tstmgr

            b "你干嘛?"

            player "Eh...我不知道.你看起来太可爱了,我忍不住."

            scene b_daily8_11 with tstmgr

            b "(似乎有点高兴)Hmmm........."

            b "你真的认为...我很可爱?"

            player "Yep,当然,毫无疑问."

            b "... ... ... ..."

            b "(低语)谢谢你......"

            scene b_daily8_12 with tstmgr

            b "*嗅,嗅*......"

            b "你用了一个新香水吗?"

            scene b_daily8_11 with tstmgr

            b "它...蛮好闻的."

            player "Yeah,我很高兴你喜欢."

            b "... ... ... ..."

            b "不说了.现在我要去见一位教授.待会见."

            player "到时候见."

            scene void with tstmgr

            "... ... ... ..."

    stop music fadeout 1.0

    jump event_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
