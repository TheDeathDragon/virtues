label d6_1:

    scene void with tstmgr

    narrator "... ... ... ..."

    narrator "第二天早上."

    narrator "今天是星期六,也许我应该去找森柠.希望她从昨天的愤怒中冷静下来."

    narrator "... ... ... ..."

    scene school_day_background with tstmgr

    narrator "我来到了校园."

    player "嗨,森柠."

    scene b_school_day_unhappy with tstmgr

    b "... ... ... ..."

    scene school_day_background with tstmgr

    player "(妈的,她还是不想和我说话)."

    player "(她可能认为我已经成为一个坏学生)."

    player "(我应该向她证明我不是)"

    call screen hint("为了让森柠不要生你的气,你最好多去上课,让她相信你还是个好学生")

    call screen hint("从现在开始,将会有更多的可用地点和行动显示在地图上.明智地制定你的每日计划.")

    jump event_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
