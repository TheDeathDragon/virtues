label F_daily_1:

    scene park_woodpath_day_background with tstmgr
    play music happy

    narrator "我已经在公园里锻炼了好几天了.我能感觉到我的体能正在恢复."

    narrator "今天,我又遇到了瑞秋.她好像每隔几天就在这个公园里跑步."

    player "Hi,瑞秋."

    scene f_wood_smile with tstmgr

    f "Oh,hi,[P].你在这里干什么?"

    player "Eh...跑步...你知道,就像你一样."

    scene f_wood_smile2 with tstmgr

    f "很高兴看到你这么做.跑步有益健康."

    f "小心点,别把自己逼得太紧.我不想让你再中暑."

    player "你能...别说那个吗?有点尴尬."

    scene f_wood_normal with tstmgr

    f "对不起,对不起.我的错."

    scene f_wood_frown with tstmgr

    f "人们总是说我不擅长交谈..."

    f "如果我冒犯了你,请原谅我."

    player "Nah,你很好.坦率从来都不是坏事."

    scene f_wood_smile with tstmgr

    f "谢谢你..."

    f "... ... ... ..."

    scene f_wood_smile2 with tstmgr

    f "你想和我一起吗?我们可以一起跑步."

    player "Oh,eh,是的,我很乐意."

    player "只是不要跑的得太快..."

    scene park_woodpath_day_background with tstmgr

    narrator "... ... ... ..."

    narrator "我和瑞秋在公园里呆了一段时间..."

    stop music fadeout 1.0

jump event_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
