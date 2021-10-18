label A_PreInteraction:



    return True

label B_PreInteraction:
    return True

label C_PreInteraction:
    return True

label D_PreInteraction:
    return True

label E_PreInteraction:
    return True

label F_PreInteraction:
    return True

label G_PreInteraction:
    return True

label TouchHead_A_general:

    scene a_general_1_frown with tstmgr

    bubble_a "你为什么要这么做?"

    bubble_b "好吧......"

    scene a_touchead_night_1 with tstmgr

    a "... ... ... ..."

    a "Eh...这感觉...有点痒..."

    scene a_touchead_night_2 with tstmgr

    a "等等...你离我太近了."

    a "越来越奇怪了..."

    scene a_touchead_night_3 with tstmgr

    a "停..."

    a "(轻微的呻吟)Ah...别..."

    scene void with tstmgr

    "... ... ... ..."

    jump interaction_post

label TouchHead_A_girlfriend:

    scene a_gf_1_default with tstmgr

    bubble_a "摸我的头?"

    bubble_a "当然...我们是恋人."

    scene a_gf_1_touchead_1 with tstmgr

    a "以前没有人对我这么好."

    a "我很高兴......"

    scene a_gf_1_touchead_2 with tstmgr

    a "谢谢...谢谢你和我待一起."

    a "... ... ... ..."

    scene a_gf_1_touchead_3 with tstmgr

    a "你知道的...如果你想的话,你可以做更多的事情."

    a "我是你的..."

    scene void with tstmgr

    "... ... ... ..."

    jump interaction_post

label TouchHead_A_sexpartner:

    scene a_gf_1_default with tstmgr

    bubble_a "摸我的头?"

    bubble_a "当然,[P]."

    scene a_gf_1_touchead_1 with tstmgr

    a "我们就像恋人......"

    a "我是说...不要想太多..."

    scene a_gf_1_touchead_2 with tstmgr

    a "谢谢...谢谢你和我待一起."

    a "... ... ... ..."

    scene a_gf_1_touchead_3 with tstmgr

    a "你知道的...如果你想的话,你可以做更多的事情."

    a "我不会跑..."

    scene void with tstmgr

    "... ... ... ..."

    jump interaction_post


label Hug_A_general:

    scene a_general_1_frown with tstmgr

    bubble_a "你真的认为有必要吗?"

    bubble_a "... ... ... ..."

    scene a_general_1_hug_1 with tstmgr

    a "我知道你这么做是为了安慰我."

    a "谢谢你......"

    scene a_general_1_hug_2 with tstmgr

    a "你的肩膀...它让我感到很有安全感."

    a "很温暖..."

    scene a_general_1_hug_3 with tstmgr

    a "... ... ... ..."

    a "你为什么对我这么好?"

    scene void with tstmgr

    "... ... ... ..."

    jump interaction_post

label Hug_A_girlfriend:

    scene a_gf_1_default with tstmgr

    bubble_a "来吧."

    bubble_a "我想再回到你的怀抱..."

    scene a_gf_1_hug_1 with tstmgr

    a "别那样笑..."

    a "这有点...尴尬."

    scene a_gf_1_hug_2 with tstmgr

    a "(愉悦地呻吟)Ah......[P]......"

    a "尽量不要...在我脖子上留下吻痕."

    scene a_gf_1_hug_3 with tstmgr

    a "我喜欢你对我霸道的样子..."

    a "(愉悦地呻吟)Ahhh......"

    scene void with tstmgr

    "... ... ... ..."

    jump interaction_post

label Hug_A_sexpartner:

    scene a_gf_1_default with tstmgr

    bubble_a "如果你这么说的话..."

    bubble_a "我很乐意这么做."

    scene a_gf_1_hug_1 with tstmgr

    a "别那样笑..."

    a "这有点...尴尬."

    scene a_gf_1_hug_2 with tstmgr

    a "(愉悦地呻吟)Ah......[P]......"

    a "是的...我想要..."

    scene a_gf_1_hug_3 with tstmgr

    a "你喜欢摸我的屁股吗..."

    a "(愉悦地呻吟)Ahhh......"

    scene void with tstmgr

    "... ... ... ..."

    jump interaction_post


label Doggie_A_girlfriend:

    scene a_gf_1_default with tstmgr

    bubble_a "是的...我也想要了...."

    bubble_a "亲爱的......"

    scene void with tstmgr

    "... ... ... ..."

    window hide

    scene a_love_5_26 with tstmgr

    pause

    scene a_love_5_28 with tstmgr

    pause

    scene a_love_5_27 with tstmgr

    pause

    scene a_love_5_30 with tstmgr

    a "我高潮了~~~~~~"

    $ flashlight()

    scene void with tstmgr

    "... ... ... ..."

    jump interaction_post

label Doggie_A_sexpartner:

    scene a_gf_1_frown with tstmgr

    bubble_a "嗯......"

    bubble_a "如果这是你想要的."

    scene void with tstmgr

    "... ... ... ..."

    window hide

    scene a_love_5_25 with tstmgr

    pause

    scene a_love_5_28 with tstmgr

    pause

    scene a_love_5_27 with tstmgr

    pause

    scene a_love_5_30 with tstmgr

    a "我高潮了~~~~~~"

    $ flashlight()

    scene void with tstmgr

    "... ... ... ..."

    jump interaction_post

label TouchHead_B_general:

    if B.clothes == 1:
        scene b_general_1_frown with tstmgr
    elif B.clothes == 2:
        scene b_general_2_frown with tstmgr

    bubble_b "摸...我的头?"
    bubble_b "Hmm......好吧..."

    if B.clothes == 1:
        scene b_touchead_day_1 with tstmgr
    elif B.clothes == 2:
        scene b_general_2_touchead_1 with tstmgr
    b "... ... ... ..."
    b "你喜欢这样吗?"

    if B.clothes == 1:
        scene b_touchead_day_2 with tstmgr
    elif B.clothes == 2:
        scene b_general_2_touchead_2 with tstmgr
    b "你的手好大..."
    b "... ... ... ..."

    if B.clothes == 1:
        scene b_touchead_day_3 with tstmgr
    elif B.clothes == 2:
        scene b_general_2_touchead_3 with tstmgr
    b "感觉好温暖..."
    b "我开始喜欢上这种感觉了..."

    scene void with tstmgr

    "... ... ... ..."

    jump interaction_post


label ShouderRub_C_general:

    scene c_general_1_smile with tstmgr

    bubble_c "... ... ... ..."
    bubble_c "舒服..."
    bubble_c "你是想取悦我吗?我不会因为这个而提高你的工资的."
    bubble_c "我在沙发等你."

    scene c_sdmassage_1 with tstmgr

    c "... ... ... ..."

    c "... ... ... ... ... ..."

    scene c_sdmassage_2 with tstmgr

    c "Hmm... ..."

    scene c_sdmassage_3 with tstmgr

    c "?... ..."

    c "(他又来了.我应该意识到的.)"

    c "... ... ... ..."

    scene c_sdmassage_2 with tstmgr

    c "(不管了...只要他不太过分...)"

    c "... ... ... ..."

    scene void with tstmgr

    "... ... ... ..."
    jump interaction_post


label TouchHead_D_general:

    if D.clothes == 1:
        scene d_general_1_default with tstmgr
    elif D.clothes == 2:
        scene d_general_2_default with tstmgr
    bubble_d "Ha?摸我的头?"
    bubble_d "棒!来吧."

    if D.clothes == 1:
        scene d_touchead_1 with tstmgr
    elif D.clothes == 2:
        scene d_general_2_touchead_1 with tstmgr
    d "... ... ... ..."
    d "感觉真好..."

    if D.clothes == 1:
        scene d_touchead_2 with tstmgr
    elif D.clothes == 2:
        scene d_general_2_touchead_2 with tstmgr
    d "这就像...我被宠爱着."
    d "太舒服了..."

    if D.clothes == 1:
        scene d_touchead_3 with tstmgr
    elif D.clothes == 2:
        scene d_general_2_touchead_3 with tstmgr
    d "Meow, Meow!"
    d "你喜欢听我这么叫吗?"

    scene void with tstmgr

    "... ... ... ..."

    jump interaction_post


label LapPillow_E_general:

    if E.clothes == 1:
        scene e_general_1_frown with tstmgr
    elif E.clothes == 2:
        scene e_general_2_frown with tstmgr
    bubble_e "你想要...再来一遍?"
    bubble_e "(这个可怜的孩子在寻求妈妈的爱.我应该帮他.)"
    bubble_e "... ... ... ..."
    bubble_e "好了,孩子,过来."

    if E.clothes == 1:
        scene e_lapillow_1 with tstmgr
    elif E.clothes == 2:
        scene e_general_2_lapillow_1 with tstmgr
    e "睡吧,睡吧,小宝贝..."
    e "我在这呢..."

    if E.clothes == 1:
        scene e_lapillow_2 with tstmgr
    elif E.clothes == 2:
        scene e_general_2_lapillow_2 with tstmgr
    e "(Oh,他熟睡的脸很可爱.)"
    e "(我一直想有自己的儿子...)"

    if E.clothes == 1:
        scene e_lapillow_3 with tstmgr
    elif E.clothes == 2:
        scene e_general_2_lapillow_3 with tstmgr
    e "(他现在一定在做梦...)"
    e "(我想知道他在做什么梦...)"

    scene void with tstmgr

    "... ... ... ..."

    jump interaction_post


label TouchBreasts_G_general:

    if G.clothes == 1:
        scene g_general_1_smile with tstmgr
    elif G.clothes == 2:
        scene g_general_2_smile with tstmgr

    bubble_g "把握时间,30秒."

    if G.clothes == 1:

        scene g_general_1_breastouch_1 with tstmgr

        g "只要记住不要做任何...奇怪的事."

        g "... ... ... ..."

        scene g_general_1_breastouch_2 with tstmgr

        g "温...柔点,拜托."

        g "不要留下任何瘀伤.下周我有一个角色扮演活动."

        scene g_general_1_breastouch_3 with tstmgr

        g "Hmm?... ..."

        g "你真的要脱下我的胸罩吗?"

        scene g_general_1_breastouch_4 with tstmgr

        g "... ... ... ..."

        g "它们...很丑,对吧?大的有点下垂了...我希望它们能小一点."

        scene g_general_1_breastouch_5 with tstmgr

        g "真的吗?你喜欢它们?"

        g "Well...你...今天可以多摸5秒."

        scene void with tstmgr

        "... ... ... ..."

    elif G.clothes == 2:

        scene g_general_2_breastouch_1 with tstmgr

        g "只要记住不要做任何...奇怪的事."

        g "... ... ... ..."

        scene g_general_2_breastouch_2 with tstmgr

        g "温...柔点,拜托."

        g "不要留下任何瘀伤.下周我有一个角色扮演活动."

        scene g_general_2_breastouch_3 with tstmgr

        g "你为什么...像在玩玩具一样."

        g "它们很重,不是吗?"

        scene g_general_2_breastouch_4 with tstmgr

        g "(愉悦地呻吟)Aww............"

        g "乳头..."

        scene g_general_2_breastouch_5 with tstmgr

        g "(呻吟)感觉...有点奇怪..."

        g "(呻吟)时间...到...了..."

        g "现在放开我..."

        scene void with tstmgr

        "... ... ... ..."

    jump interaction_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
