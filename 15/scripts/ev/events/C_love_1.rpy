label C_love_1:

    scene void with tstmgr
    play music happy

    c "... ... ... ..."



    player "... ... ... ... ... ..."



    c "... ... ... ..."



    player "... ... ... ... ... ..."



    scene c_love_1_1 with dissolve

    c "... ... ... ..."



    player "... ... ... ... ... ..."



    "我来解释一下这是怎么回事."



    "早些时候,我被派去送一份文件到另一层.我在电梯里碰到狄奥多拉."



    "你看,此时此刻我最不想做的事就是和狄奥多拉单独在一起.我5岁的时候就认识这个女孩了,现在她成了我的主管.这太...尴尬了."



    "你知道更尴尬的是什么吗?"



    "该死的电梯坏了!我们困在一起了!令人难以置信!"



    "公平地说,被困在电梯里没什么大不了的.我没有幽闭恐惧症,而且我很确定这种情况将在最多30分钟内得到解决.但是上帝,为什么我必须和狄奥多拉在一起!"



    c "... ... ... ..."



    player "... ... ... ... ... ..."



    "死一般的沉默."



    c "你为什么把我当成连环杀手之类的?"



    player "Ah?我有吗?"



    c "Yeah,独自和我在一起对你来说是一种折磨吗?"



    player "没有......"



    player "它只是...我真的不知道如何与我的上司相处.我的意思是,我以前从来没有过上司."



    scene c_love_1_2 with tstmgr

    c "Huh... ... ... ..."



    c "说实话,我现在也不知道该怎么跟你相处."



    scene c_love_1_3 with tstmgr

    c "(呢喃)我从来都不知道...如何与你相处......"



    player "你刚才说什么?"



    scene c_love_1_4 with tstmgr

    c "没什么...忘了它..."



    scene c_love_1_5 with tstmgr

    c "我想念以前的你.以前的你是个混蛋,但至少是个有趣的混蛋.在这种情况下,你会喋喋不休,让我不至于厌烦."



    c "而现在...你太无聊了."



    player "现在你是我的上司,所以...我不能像以前那样了.我不想冒犯你."



    scene c_love_1_4 with tstmgr

    c "Yeah我现在是你的经理,但我仍然是你的未婚妻."



    "什么...她想说什么?"



    scene c_love_1_5 with tstmgr

    c "唉...算了..."



    scene c_love_1_4 with tstmgr

    player "你知道,我一直没机会问......"



    player "我们在高中的时候很亲密,但是为什么你上了大学后就再也没有联系我?发生了什么事?"



    c "... ... ... ..."



    c "人是会变的."



    player "Yeah,但是你没有取消我们的婚约.这是否意味着......"



    scene c_love_1_5 with tstmgr

    c "没意味着什么.我妈妈想让我嫁给你,我正在做她想做的事.就这样."



    player "但你不必听你妈妈的话.我的意思是,在遇到你真正爱的人之前,你绝对可以保持单身."



    scene c_love_1_4 with tstmgr

    c "... ... ... ..."



    scene c_love_1_6 with tstmgr

    c "所以你的理由是什么?你为什么答应和我订婚?因为我是你真正“爱”的人?"



    player "我...我不是这个意思."



    scene c_love_1_7 with tstmgr

    c "... ... ... ..."



    c "可疑~"



    c "让我们做个测试~"



    scene c_love_1_8 with tstmgr

    "她突然走近我,把一只手放在我的胸前."



    c "说你不爱我."



    player "什么...你在说什么?"



    c "当你说谎时,你的心跳会急剧加快.你13岁的时候我就知道了.现在说~"



    label C_love_1_choice_1:

    menu:
        "我不爱你":


            scene c_love_1_9 with tstmgr

            c "Hmmmmm hum... ... ... ..."

            c "你真是个差劲的骗子~"

            player "等等,这不公平.因为你离我很近,我的心跳加快了."

            scene c_love_1_8 with tstmgr

            c "无所谓了.反正我得到了我想要的答案~"

            player "... ... ... ..."
        "我爱你":




            scene c_love_1_11 with tstmgr

            c "什么?......"

            scene c_love_1_10 with tstmgr

            c "我............"

            "是我看错了,还是她真的脸红了?"

            c "那可...真麻烦..."

            c "... ... ... ..."



    scene void with tstmgr

    "在我们谈话的时候,电梯又开始动了.我们很快就到了要去的楼层,离开了电梯..."



    "... ... ... ..."

    stop music fadeout 1.0

    jump event_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
