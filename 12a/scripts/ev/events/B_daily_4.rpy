label B_daily_4:

    scene school_day_background with tstmgr
    play music happy

    narrator "我在学校找到了森柠."

    player "嘿,森柠,一切都好吗?"

    scene b_school_day_frown with tstmgr

    b "... ... ... ..."

    b "聊一聊?"

    player "当然,随时奉陪.你想聊什么?"

    b "我知道你们的秘密事业是开民宿."

    b "我也知道现在你和薇拉小姐住在一起."

    b "她是谁?你为什么从来不告诉我她的事?"

    player "Eh...她是我的一个朋友,最近我才认识她的."

    b "... ... ... ..."

    b "什么样子的朋友?"

    player "她只是...一个普通的朋友.我们只是室友,没有别的."

    b "... ... ... ..."

    player "等等,你为什么这么在乎?"

    b "... ... ... ..."

    player "你在嫉妒吗?"

    scene b_school_day_unhappy with tstmgr

    b "不,我没有."

    scene b_school_day_frown with tstmgr

    b "我只是对薇拉小姐很好奇.她就像你家的女主人一样.你们俩一定很亲密."

    player "你觉得她怎么样?"

    scene b_school_day_normal with tstmgr

    b "她既漂亮又有礼貌.我有点喜欢她."

    player "她擅长做饭和打扫房间.你们俩有很多共同点."

    scene b_school_day_frown with tstmgr

    b "你认为我和薇拉小姐能成为朋友吗?"

    player "Yeah,为什么不呢?你一定要多去我家,多了解她."

    b "... ... ... ..."

    scene b_school_day_normal with tstmgr

    b "我会考虑的..."

    b "... ... ... ..."

    b "要开始上课了.我们该走了."

    player "好吧..."

    narrator "... ... ... ..."

    stop music fadeout 1.0

    jump event_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
