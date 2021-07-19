label hint_clean:

    scene void with tstmgr
    play music happy

    "早上,当我和薇拉打扫房子的时候..."



    scene hint_clean_1 with dissolve

    a "你知道,这房子有点奇怪..."



    player "什么意思?"



    scene hint_clean_2 with tstmgr

    a "你不觉得客厅和厨房有点...对这么大的房子来说太小了?"



    player "... ... ... ..."



    "我觉得她说的有道理.我从来没见过客厅和厨房这么小的大房子.这就像...有人建了一堵墙,把它们从中间切开了."



    player "我不知道...我看看能不能弄到这房子的布局图."



    scene void with tstmgr

    "... ... ... ..."

    call screen hint("你可以多做几次房子清洁,以发现隐藏在你的房子的空间.")

    call screen hint("在“清洁”按钮上总是会有一个红点.等你发现了什么,它就会消失.")

    stop music fadeout 1.0

    jump event_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
