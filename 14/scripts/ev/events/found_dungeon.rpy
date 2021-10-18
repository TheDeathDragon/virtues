label found_dungeon:



    scene void with tstmgr
    play music happy

    "一大早,我和薇拉像往常一样打扫客厅..."



    scene found_dungeon_1 with dissolve

    a "[P],你拖地了吗?"



    player "Oh,我在拖."



    scene found_dungeon_2 with tstmgr

    player "... ... ... ..."



    player "我一定要买个扫地机器人来拖地..."



    scene found_dungeon_3 with tstmgr

    a "省点钱,好吗?我们可以自己拖的~"



    a "再说了,会不会太吵了?我们不想在这么早的时候把人们吵醒."



    scene found_dungeon_4 with tstmgr

    player "Ehhh......说得好."



    scene found_dungeon_5 with tstmgr

    player "... ... ... ..."



    scene found_dungeon_6 with tstmgr

    player "Hmmmm?为什么书柜前面的地板上有一道划痕?你以前注意过吗?"



    scene found_dungeon_7 with tstmgr

    a "地板上的划痕?Yeah,但我不知道该怎么修补."



    player "No...这不是修补的问题......"



    scene found_dungeon_8 with tstmgr

    player "似乎...书柜是一扇隐藏的门或什么东西,划痕是移动它造成的."



    scene found_dungeon_9 with tstmgr

    a "什么?一个隐藏的门?就像电影里一样?"



    player "我不知道...让我检查一下......"



    scene void with tstmgr

    "我在书柜上摸索着,想看看有没有开关."



    a "拜托,[P],我们还是专心打扫吧,好吗?"



    a "在现实生活中根本没有这样的事情,你太荒唐了."



    "*Pa-dam*"



    a "... ... ... ..."



    a "是什么声音?你真的......"



    player "我...我想是这样.书架上确实有一个开关按钮.你敢信?"



    "随着齿轮移动的一声巨响,书柜自己移动了,我们看到了一间黑暗的房间."



    "... ... ... ..."



    scene found_dungeon_10 with dissolve

    a "这...是个什么地方?"



    player "OhmyGod.这是...这是......"



    scene found_dungeon_11 with tstmgr

    player "这是...一个地牢.我猜这房子的前任主人一定很喜欢玩SM......"



    scene found_dungeon_12 with tstmgr

    a "这太恐怖了......他是罪犯还是什么?我害怕."



    scene found_dungeon_15 with tstmgr

    player "别担心.我会...呃...保护你的."



    scene found_dungeon_16 with tstmgr

    a "*微笑*............"



    scene found_dungeon_13 with tstmgr

    player "我不认为他是罪犯.这些东西看起来不像是真正的刑具.看,木马上有一层海绵,防止人们受伤."



    a "... ... ... ..."



    scene found_dungeon_14 with tstmgr

    a "不管怎样,待在这里我觉得不舒服.我们应该尽快离开这个地方让这个地方保持原样."



    player "实际上...我倒是有些兴趣......"



    player "... ... ... ..."



    player "Yeah,你说得对,我们走吧."



    scene void with tstmgr

    player "... ... ... ..."



    player "(一个地牢,huh......也许将来我能想到它的一些用途...)"

    call screen hint("从现在开始,你可以带你的服从度达到2级的女孩到地牢.")

    call screen hint("你可以通过在女孩的房间里找到她们,并使用“带她去”按钮来做到这一点.")


    stop music fadeout 1.0

    jump event_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
