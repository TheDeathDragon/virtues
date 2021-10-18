label find_A_restaurant_evening_A_2:

    scene bar_background with tstmgr

    player "Hi,薇拉."



    scene a_restaurant_slight_surprise with tstmgr

    a "对不起,我现在有点忙.我待会再和你说."



    player "Oh,好的,慢慢来."



    a "... ... ... ..."



    scene a_restaurant_smile with tstmgr

    a "你知道吗?算了,今天我能为你做点什么?"



    player "你不需要担心其他的客人吗?"



    a "你也是我的客人..."



    a "(低语)我最喜欢的客人."



    scene void with tstmgr

    "... ... ... ..."



    $ add(A, A.love, 1)

    jump playlet_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
