label B_daily_11:

    scene void with tstmgr
    play music happy

    "又是上学的一天,马上就要去上课了,一切如常,没什么特别的."



    "除了这个..."



    scene b_daily11_1 with tstmgr

    b "你能...慢一点吗?"



    "除了我这辈子第一次牵着森柠的手."



    scene b_daily11_2 with tstmgr

    b "我们还有时间,不着急."



    player "Oh...抱歉."



    scene b_daily11_3 with tstmgr

    b "有必要一路上牵着我的手吗?"



    b "我觉得...有点尴尬."



    player "我想你会习惯的,既然我们在一起了."



    b "... ... ... ..."



    scene b_daily11_4 with tstmgr

    b "嗯......"



    if B.relation == "girlfriend":

        player "我想让每个人都看到你现在是我的女朋友."

    if B.relation == "sexpartner":

        player "我想让每个人都看到你现在是我的了."



    b "这是在炫耀吗?"



    player "Hmm... yep."



    player "你不喜欢?"



    b "我............"



    b "...你喜欢就好..."



    scene void with tstmgr

    "... ... ... ..."

    stop music fadeout 1.0

    jump event_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
