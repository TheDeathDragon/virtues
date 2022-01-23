label mansion_tutor_evening_D_1:

    scene void with tstmgr

    "今天晚上,我在艾琳的房间里辅导她......"



    scene rcsj_d13 with tstmgr

    d "已经很晚了.我想你今晚应该呆在这里,[P]."



    player "Eh,我很乐意,但我还有别的事要做."



    d "什么事?"



    player "我需要在朋友下班后去接她."



    scene rcsj_d14 with tstmgr

    d "她?"



    player "不要想太多,现在专心做你的作业."



    scene rcsj_d13 with tstmgr

    d "... ... ... ..."



    d "好吧......"



    $ add(D, D.love, 1)



    $ P.cash.add(100)

    jump playlet_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
