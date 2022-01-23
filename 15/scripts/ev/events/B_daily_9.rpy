label B_daily_9:

    scene void with tstmgr
    play music happy

    "考试之后..."



    scene b_school_day_smile with tstmgr

    b "你觉得这次考试怎么样?"



    player "我不知道.这次似乎挺简单,但我不确定我的答案是否是对的."



    player "... ... ... ..."



    player "不说这个了.你下午怎么安排?"



    player "你想和我一起去看电影吗?"



    scene b_school_day_frown with tstmgr

    b "我?Hmm......"



    b "No,我不认为这是个好主意."



    b "我想我还是呆在房间里休息一下吧."



    player "Oh...好吧......"



    scene b_school_day_normal with tstmgr

    b "... ... ... ..."



    b "也许吧..."



    scene b_school_day_smile with tstmgr

    b "你知道...如果你愿意,也许我们可以一起喝下午茶."



    player "Eh,你是说,在你的房间里?"



    b "(点头)............"



    player "Yeah,乐意至极."



    player "我们还在等什么?走吧!"



    scene void with tstmgr

    "... ... ... ..."



    "过了一会儿,在森柠的房间里."



    scene b_daily9_1 with tstmgr

    b "你觉得这茶怎么样?"



    b "我知道你不喜欢苦味,所以我在你的茶里加了一些冰糖.你喜欢吗?"



    player "我...是的,我喜欢."



    label B_daily_9_choice_1:

    menu:
        "夸这个茶":


            player "这茶叫什么名字?味道真的很好."

            b "我很高兴你喜欢."

            b "它叫金骏眉,金马的眉毛."

            player "这个名字真好听..."

            b "这是我最喜欢的红茶.你可以在走之前带上一些."

            player "没有必要那样做."

            player "每当我想念这个味道的时候,我都会来找你."

            scene b_daily9_2 with tstmgr

            b "Oh... ..."

            scene b_daily9_1 with tstmgr

            b "Yeah,随时欢迎."
        "夸她":




            player "... ... ... ..."

            scene b_daily9_2 with tstmgr

            b "...你为什么那样盯着我看?"

            player "(微笑)............"

            b "Eh...你笑什么?"

            player "只是...你知道,感觉不真实."

            player "在一个美好的下午,与一位美丽的女士在阳台上喝茶.我觉得我是英国贵族之类的."

            scene b_daily9_1 with tstmgr

            player "我想我们应该多在一起喝下午茶."

            b "Yeah,随时欢迎."



    scene b_daily9_3 with tstmgr

    "阳光穿过云层,照在她的笑脸上.哦...她太美了."



    scene b_daily9_2 with tstmgr

    b "Hmmm... ... ... ..."



    b "你的微笑变得更怪了."



    player "抱歉."



    b "而且你还在盯着我看."



    player "(拿起茶,假装在喝)emmmm......"



    scene b_daily9_4 with tstmgr

    b "小心!"



    "我不小心把茶洒在衬衫上了."



    player "Ah...可恶..."



    player "没关系,没什么大不了的.水不烫."



    scene b_daily9_2 with tstmgr

    b "但是茶会弄脏你的衬衫.它可能很难清洗,因为普通的清洁剂对茶渍没什么作用."



    b "Hmm... ... ... ..."



    scene b_daily9_5 with tstmgr

    b "如果你不介意的话,可以把衬衫留给我.我会帮你手洗."



    player "Oh,别担心.我可以自己洗."



    b "无意冒犯,但我认为你处理不好."



    b "直到上个月你才知道如何使用洗碗机."



    b "来吧,我帮你洗.别客气.我们是朋友."



    player "Hmmm......好吧."



    player "谢谢你,森,你太好了."



    scene b_daily9_6 with tstmgr

    b "我很乐意为你做点事."



    scene void with tstmgr

    "... ... ... ..."



    stop music fadeout 1.0

    jump event_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
