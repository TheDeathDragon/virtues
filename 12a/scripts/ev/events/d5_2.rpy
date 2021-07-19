label d5_2:

    scene void with tstmgr

    narrator "第二天早上."

    scene a_apartment_background_day with tstmgr

    narrator "这个地方...看起来很糟糕...而且闻起来很难闻..."

    narrator "我又来到了薇拉的公寓楼前."

    narrator "她住在贫民窟里...天啊,这地方真臭..."

    narrator "Well,她可能不想看到我出现在这里,所以我最好不要让她知道我在这里."

    narrator "你可能想知道我为什么来这里.嗯,你知道,这是一个有美德的人需要做的,他犯了一个错误,他试图弥补它.这是我的第一步."

    scene slum_door_background with tstmgr

    narrator "我走进公寓,很快就找到了她的房间.现在是早上7点.我想她应该还在她的房间里."

    narrator "我把一个药瓶,一些名片和一封信放在她门前的地上."

    player "Okay,行了."

    narrator "然后我安静地离开了这个地方."

    scene void with tstmgr

    narrator "... ... ... ..."

    narrator "晚些时候."

    scene a_door_curious with tstmgr

    a "(打开门,注意到地上有东西)Hm?"

    scene a_door_letter with tstmgr

    a "(把它们捡起来)这是...?"

    a "一封道歉信,一瓶药,还有医生的名片?"

    narrator "薇拉打开了信."

    narrator "{i}嗨,薇拉.是我,[P].我不敢请求你的原谅,但我想让你知道,我对我对你所做的一切深感抱歉.{/i}"

    narrator "{i}毕竟是我的错.你有理由恨我,但我还是希望你能接受这些东西.{/i}"

    narrator "{i}瓶子里的药片是紧急避孕药.我尽力回忆那天晚上发生的事,我记得我没有...你知道的...在你体内,但仍然有怀孕的可能性.所以我想你需要这个.{/i}"

    narrator "{i}还有一些著名医生的名片.如果你想做健康检查或其他什么,打电话给他们,安排一个预约.它将是完全免费的,只要告诉医生我的名字.{/i}"

    narrator "{i}最后,再说一次,我很抱歉,如果你能给我一个机会,我真的很想弥补你.这是我的电话号码:5XX2XX4XXX.如果你需要任何帮助,尽管打电话给我.{/i}"

    a "... ... ... ..."

    a "他......"

    narrator "... ... ... ... ... ..."

    scene void with tstmgr

    narrator "... ... ... ..."

    jump event_post


label d5_2_bLine:

    scene void with tstmgr

    "第二天早上..."



    scene d5_2_1 with dissolve

    "我又来了,在薇拉的公寓大楼前."



    "她住在贫民窟里.这个地方...看起来很可怕的...而且味道很难闻..."



    scene d5_2_2 with tstmgr

    a "Hmm?你在这里干什么?"



    scene d5_2_4 with tstmgr

    a "等等,请再说一次你的名字?"



    player "[P]... ..."



    player "我只是想四处看看,你知道,看看有什么我可以帮你的......"



    player "我为那天晚上发生的事感到抱歉......"



    scene d5_2_5 with tstmgr

    a "唉...这不是你的错.又不是你强奸了我或者强迫我做什么.记得吗,我们喝醉了?"



    scene d5_2_6 with tstmgr

    a "我想我的余生都会为那一天而后悔,但我并不真的为此责怪你..."



    player "但是......"



    scene d5_2_7 with tstmgr

    a "Ehhh......我的腰...还疼......"



    player "认真的吗?如果你愿意我可以开车送你去医院."



    scene d5_2_8 with tstmgr

    a "谢谢,不过我想我能行..."



    a "请...别打扰我了.我不需要你提醒我那晚发生了什么..."



    scene d5_2_9 with tstmgr

    a "现在我要去工作了.再见,哦不,我是说,再也不见......"



    scene d5_2_1 with tstmgr

    "然后她不理我了,一瘸一拐地朝街上走去..."



    player "... ... ... ..."



    "她真是个特别的女孩.她的自尊心不允许她接受我的帮助,但是...我想我还能为她做些什么..."



    "... ... ... ..."

    jump event_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
