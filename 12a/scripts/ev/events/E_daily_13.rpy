label E_daily_13:

    scene void with tstmgr
    play music happy

    "薇拉好像在走廊上和别人说话.我应该去看看..."



    scene e_daily13_1 with dissolve

    player "伊莉......伊莉莎?"



    scene e_daily13_2 with tstmgr

    e "Hi,[P].这是我第一次来你家.这地方真棒~"



    e "你有个很好的室友......"



    scene e_daily13_3 with tstmgr

    a "你太好了,新光夫人~"



    a "我现在要准备午饭了,再见~"



    e "待会见,亲爱的~"



    scene e_daily13_4 with tstmgr

    "... ... ... ..."



    player "所以...什么风把你吹来了,伊莉莎阿姨?"



    scene e_daily13_5 with tstmgr

    e "... ... ... ..."



    e "我还是不敢相信我要这么做,但是......"



    scene e_daily13_6 with tstmgr

    e "给......"



    "她递给我一把钥匙."



    e "这是...那间平房的钥匙.我觉得你应该要有一把..."



    scene e_daily13_7 with tstmgr

    e "*喃喃语*所以...当你想再次和我独处的...时候,我们可以......在那儿见......"



    "伊莉莎的脸涨得通红,就像一个终于鼓起勇气和初恋对象说话的十几岁的女孩.我以前从未见过这位坚强的女士如此害羞."



    player "谢谢,阿姨,我收下了."



    scene e_daily13_8 with tstmgr

    e "还有...不要告诉别人那个地方.这是...我们之间的秘密."



    player "我肯定不会的......"



    scene e_daily13_9 with tstmgr

    e "*欣慰的笑*............"



    e "Okay,就这些了.我该走了..."



    player "你不想待在这里吃午饭吗?薇拉做的菜很棒..."



    e "我现在要去见狄奥多拉.所以......"



    player "Oh, okay... ..."



    e "拜,亲爱的~"



    scene void with tstmgr

    "... ... ... ..."

    $ add(E, E.love, 1)

    stop music fadeout 1.0

    jump event_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
