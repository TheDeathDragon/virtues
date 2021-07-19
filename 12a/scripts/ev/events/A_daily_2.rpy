label A_daily_2:

    scene cafe_background with tstmgr
    play music happy

    player "Hello,薇拉."

    scene a_cafe_weird with tstmgr

    a "... ... ... ..."

    a "你又来了."

    player "怎么了?"

    a "你最近经常来.似乎...不太正常."

    player "你这话是什么意思?"

    a "我在想你是否想追我..."

    player "不.我来这里是因为我喜欢这里的早餐,没有别的了."

    narrator "那是个谎话,至少部分是."

    narrator "我不能否认我对这个女孩有感觉,我渴望改善我们的关系.但我没有追她,至少现在还没有."

    scene a_cafe_surprise with tstmgr

    a "真的?"

    player "Yeah..."

    scene a_cafe_normal1 with tstmgr

    a "... ... ... ..."

    a "很抱歉问你这个奇怪的问题."

    narrator "她的脸色看起来很正常.然而,我不知道我是不是弄错了,但她的声音里似乎有一点不安."

    scene a_cafe_smile2 with tstmgr

    a "你今天想吃什么?"

    narrator "也许我想得太多了."

    player "熏肉三明治套餐,再加一杯香草奶昔."

    a "OK,我马上就回来."

    scene cafe_background with tstmgr

    narrator "... ... ... ..."

    stop music fadeout 1.0

    jump event_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
