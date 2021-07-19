label CDE_Picnic:

    scene void with tstmgr
    play music happy

    narrator "... ... ... ..."

    narrator "*电话铃声*DududuDududuDududu..."

    narrator "早上我被电话吵醒了.是伊莉莎阿姨."

    player "(打呵欠)Hi...伊莉莎阿姨."

    e "早上好,[P].我刚把你从睡梦中吵醒了吗?如果是的话,我很抱歉."

    player "没关系,伊莉莎阿姨."

    player "找我有什么事儿吗?"

    e "我们今天要举行一次家庭野餐.你想和我们一起去吗?"

    player "Eh,我?..."

    player "Okay,伊莉莎阿姨.我会去的."

    narrator "周末和伊莉莎阿姨一家去野餐是个不错的主意.我是说,我周围会有3位美女.哪个男人会拒绝呢?"

    narrator "... ... ... ..."

    scene cde_date1_1 with tstmgr

    narrator "过了一会儿,我到达了野餐营地.伊莉莎阿姨和她的女儿们已经到了."

    d "[P]!"

    c "他为什么在这里,妈妈?"

    e "我邀请[P]来的.野餐时一定要有一个男人."

    c "... ... ... ..."

    c "好吧..."

    scene cde_date1_2 with tstmgr

    player "... ... ... ..."

    player "(Wow...伊莉莎阿姨的着装...有点大胆.)"

    scene cde_date1_3 with tstmgr

    d "Ah...[P]在盯着妈妈看.变态!"

    player "我没有..."

    scene cde_date1_4 with tstmgr

    d "告诉我,你觉得我们三个人中谁最漂亮."

    narrator "这是什么问题?我该怎么回答这个问题呢?"

    narrator "我看见伊莉莎阿姨和狄奥多拉惊讶地看着艾琳.她们一定意识到这是多么可笑.我想她们会阻止她的."

    scene cde_date1_3 with tstmgr

    e "事实上,yeah,我也很好奇[P]对我们的评价."

    e "[P],告诉我们你是怎么想的."

    c "你们两个...真是幼稚.难以置信."

    d "别装了,狄奥多拉.你也想知道."

    e "所以,怎么说,[P]?"

    e "谁最吸引人?"

    player "Uh... ... ... ..."


    menu:
        "狄奥多拉":

            scene cde_date1_5 with tstmgr

            c "我?"
            scene cde_date1_6 with tstmgr

            e "明智的选择,永远不要让你的未婚妻失望."
            d "狄奥多拉脸红了!狄奥多拉脸红了!"
            scene cde_date1_7 with tstmgr

            c "我没有...闭嘴!我要堵住你的嘴!"
            d "你做得到的话就来呀!"
            e "安静,女孩们,注意你们的举止."
        "艾琳":


            scene cde_date1_8 with tstmgr

            d "Wow,我?"
            c "别逗了,你瞎了吧?"
            scene cde_date1_9 with tstmgr

            d "什么?你是嫉妒吗?"
            c "我为什么要嫉妒?我根本不在乎."
            scene cde_date1_10 with tstmgr

            d "因为[P]更喜欢我!"
            c "你......"
            e "安静,女孩们,注意你们的举止."
        "伊莉莎阿姨":


            scene cde_date1_11 with tstmgr

            e "Oh,看来我赢了.谢谢,[P]."
            d "一定是因为你的穿着,妈妈!你作弊!"
            c "你们都没救了."
            scene cde_date1_12 with tstmgr

            d "等等,[P].你迷恋我妈妈吗?"
            e "别胡说了,艾琳."

    scene void with tstmgr

    e "我们坐下吧."

    scene cde_date1_13 with tstmgr

    narrator "我们走到附近的野餐桌旁坐下."

    scene cde_date1_14 with tstmgr

    c "说真的,妈妈.你今天为什么穿成这样?"

    scene cde_date1_15 with tstmgr

    d "Yeah,我也想问这个问题.你看起来怪怪的,妈妈."

    scene cde_date1_16 with tstmgr

    c "你穿得像个80年代的妓女."

    scene cde_date1_17 with tstmgr

    e "这很没礼貌,狄奥多拉.你不应该这样和我说话."

    e "你每天在工作时展示你的胸罩时,我什么都没说."

    c "Eh... ..."

    scene cde_date1_18 with tstmgr

    e "还有艾琳,我知道你把校服的裙子剪得几乎盖不住屁股了."

    e "所以你们两个都没有权利评判我."

    d "Oh... ..."

    narrator "Wow,伊莉莎阿姨确实知道如何对付这两姐妹."

    narrator "我该说什么?"


    menu:
        "支持狄奥多拉":


            scene cde_date1_19 with tstmgr

            player "我认为狄奥多拉在工作上做得很好."
            player "她知道如何利用自己的魅力来鼓励下属."
            scene cde_date1_20 with tstmgr

            c "(吃惊)Eh?"
            c "Ah, well..."
            scene cde_date1_21 with tstmgr

            c "谢谢你这样说..."
            e "很好.总是讨好你的上司.你真的成长了很多,[P]."
            scene cde_date1_22 with tstmgr

            d "Hmm... ... ... ..."
        "支持艾琳":


            scene cde_date1_19 with tstmgr

            player "我觉得艾琳穿着她的制服裙子很漂亮."
            player "她一定是学校里最迷人的女孩."
            scene cde_date1_23 with tstmgr

            d "谢谢,[P].你最好了!"
            e "多亏了你的辅导,你和艾琳的关系好像越来越好了."
            scene cde_date1_24 with tstmgr

            d "(明亮的笑容)HeeHee..."
            scene cde_date1_25 with tstmgr

            c "Hmm... ... ... ..."
        "支持伊莉莎":


            scene cde_date1_19 with tstmgr

            player "Yeah,我觉得伊莉莎阿姨的着装很漂亮."
            player "它看起来充满活力,也很性感."
            scene cde_date1_26 with tstmgr

            e "Oh,谢谢,[P].我很高兴你支持我."
            c "Yeah,男生都喜欢这样的,无所谓了..."
            d "这不公平!"

    scene void with tstmgr

    narrator "... ... ... ... ... ..."

    narrator "我得承认我真的很喜欢和他们在一起.她们让我觉得我是这个家庭的一员.你知道,我在别的地方从来没有过这种感觉,即使和我爸爸在一起."

    scene cde_date1_27 with tstmgr

    narrator "我没有兄弟姐妹,也没有妈妈.直到我见到伊莉莎阿姨的家人,我才知道和她们在一起是什么感觉.我真的很感激."

    narrator "我愿意就这样永远坐在这里听她们说话.太幸福了."

    scene cde_date1_28 with tstmgr

    e "所以,[P].你在学校怎么样?你觉得边工作边学习有什么困难吗?"

    player "Well...我想还行.我的朋友们会在学习上帮助我,狄奥多拉在工作上也帮了我很多."

    scene cde_date1_29 with tstmgr

    e "听你这么说我很高兴.狄奥多拉看起来很冷漠,但我知道她很关心你."

    narrator "Well...我有点怀疑...我应该怎么说?"


    menu:
        "支持伊莉莎":


            player "Yeah,我能感觉到.狄奥多拉心肠软.和她一起工作很愉快."
            scene cde_date1_20 with tstmgr

            c "Oh...Well...谢谢."
            scene cde_date1_21 with tstmgr

            c "你也很...体贴..."
            d "天啊,你们为什么不下周就结婚呢?"
            scene cde_date1_30 with tstmgr

            c "闭嘴!"
        "一言不发":


            player "(不明确地回应)Uh-huh......"
            scene cde_date1_31 with tstmgr

            c "... ... ... ..."

    scene cde_date1_28 with tstmgr

    e "我听说你拥有一间民宿,对吗,[P]?"

    player "Uh...是的.这只是个小生意."

    scene cde_date1_32 with tstmgr

    d "什么?我都不知道!你为什么不告诉我?"

    player "Well... ..."

    scene cde_date1_23 with tstmgr

    d "我可以去住吗,我可以付钱."

    player "关于这个......"


    menu:
        "我没意见":

            scene cde_date1_24 with tstmgr

            player "Yeah,如果你来的话,我会很高兴的."
            d "真的?"
            scene cde_date1_33 with tstmgr

            e "等你上了大学再考虑吧.但是现在,你必须呆在家里度过高中的最后一年."
            d "嗯......"
            c "的确,你还太小,不能搬出去."
            scene cde_date1_34 with tstmgr

            d "... ... ... ..."
            scene cde_date1_33 with tstmgr

            d "我不能把妈妈一个人留下."
            d "狄奥多拉搬出去后,我是妈妈唯一的孩子."
            scene cde_date1_35 with tstmgr

            c "为什么听起来我是个坏女儿?"
            scene cde_date1_36 with tstmgr

            d "是的,你就是.不然你为什么不和我们一起住呢?"
            scene cde_date1_30 with tstmgr

            c "因为我已经长大了,小女孩.成年人自己住."
            scene cde_date1_36 with tstmgr

            d "不,你只是自私."
            c "Ahhh...无所谓了,你说什么我都不在乎."
        "我觉得你应该和伊莉莎阿姨住在一起":


            scene cde_date1_24 with tstmgr

            player "我觉得你应该和伊莉莎阿姨住在一起.如果你走了,她会感到孤独的."
            scene cde_date1_33 with tstmgr

            d "Oh,你说得对."
            d "狄奥多拉搬出去后,我是妈妈唯一的孩子.我不能离开她."
            scene cde_date1_35 with tstmgr

            c "为什么听起来我是个坏女儿?"
            scene cde_date1_36 with tstmgr

            d "是的,你就是.否则,你为什么要离开家到别的地方去住呢?"
            scene cde_date1_30 with tstmgr

            c "因为我已经长大了,小女孩.成年人自己住."
            scene cde_date1_36 with tstmgr

            d "不,你只是自私."
            c "Ahhh...无所谓了,你说什么我都不在乎."

    e "Okay,孩子们,冷静下来.谁想要一些三明治?"

    scene cde_date1_37 with tstmgr

    narrator "两姐妹停止了争吵,互相怒目而视."
    narrator " "
    narrator "Well,她们从小就相处得不好,但她们都听妈妈的话.伊莉莎阿姨总是能用几句话阻止她们打架."

    scene void with tstmgr

    narrator "... ... ... ..."

    narrator "一段时间后."

    scene cde_date1_17 with tstmgr

    narrator "谈话的主题已经从“家庭和生活”转移到“业务和公司”.伊莉莎阿姨和狄奥多拉是谈话的主角.有时我也会插话,发表一下看法."

    scene cde_date1_38 with tstmgr

    narrator "至于艾琳,她现在很无聊,因为她根本不知道我们在说什么."

    scene cde_date1_39 with tstmgr

    narrator "Hmm?"

    narrator "艾琳突然站了起来."

    scene cde_date1_40 with tstmgr

    narrator "她开始靠近狄奥多拉.她想干什么?"

    scene cde_date1_41 with tstmgr

    narrator "... ... ... ..."

    narrator "我想她要对她姐姐做一个恶作剧.我应该提醒狄奥多拉吗?"


    menu:
        "提醒她":

            scene cde_date1_42 with tstmgr

            narrator "我和狄奥多拉对视了一下.她似乎意识到了这一点."
            scene cde_date1_43 with tstmgr

            c "停下来,艾琳."
            scene cde_date1_44 with tstmgr

            d "什么?你怎么知道我在你后面?"
            c "我听到了.你的脚步很沉重.你最近胖了吗?"
            scene cde_date1_45 with tstmgr

            d "... ... ... ..."
            d "我讨厌你!"
            scene cde_date1_46 with tstmgr

            narrator "艾琳走回座位,没有再看狄奥多拉一眼."
            narrator "... ... ... ..."
            e "现在谁渴了?我带了一些啤酒."
            scene cde_date1_47 with tstmgr

            d "啤酒吗?我,我,我!"
            e "不,你还太小.你可以喝点果汁."
            scene cde_date1_48 with tstmgr

            d "这不公平!"
            scene cde_date1_49 with tstmgr

            d "我讨厌你们所有人!"
            narrator "... ... ... ..."
        "不提醒她":


            narrator "我真的很好奇她会做什么..."
            scene cde_date1_50 with tstmgr

            narrator "紧接着,她跳了出来,用手抓住狄奥多拉的乳房."
            narrator "狄奥多拉颤抖了一下,惊讶地呻吟起来."
            scene cde_date1_51 with tstmgr

            c "你觉得你在干什么?"
            c "停下来."
            d "我不会停直到你说\"请\"."
            scene cde_date1_52 with tstmgr

            c "艾琳,我现在没心情玩."
            c "[P]看着呢...你应该注意你的行为."
            scene cde_date1_53 with tstmgr

            d "Oh,yeah.我差点忘了."
            d "Hey,[P].你知道狄奥多拉最大的弱点是什么吗?"
            player "Uh... ... ... ..."
            scene cde_date1_54 with tstmgr

            d "你想我展现给你看吗?"
            c "停下来,艾琳.你太过分了."
            player "好吧............"
            scene cde_date1_55 with tstmgr

            d "看,我姐姐的身体很敏感.她不想任何人碰她,即使是妈妈."
            c "现在可以放开我了吗."
            d "你知道她身体最敏感的部位是什么吗?"
            scene cde_date1_56 with tstmgr

            c "等等,你在干什么?"
            narrator "狄奥多拉的声音里流露出恐惧和恐慌的情绪."
            scene cde_date1_57 with tstmgr

            c "停,停!"
            narrator "但是艾琳不听."
            d "她身体最敏感的部位是..."
            scene cde_date1_58 with tstmgr

            d "她的乳头."
            narrator "她突然用手指按住狄奥多拉的乳房.看来她找到了狄奥多拉乳头的正确位置."
            narrator "现在,狄奥多拉的乳头受到她妹妹手指的强烈刺激.她像触电似的发抖."
            scene cde_date1_59 with tstmgr

            c "Ahhhhhhhh!!!!!!!"
            c "停!停!停下!!!!!"
            narrator "狄奥多拉尖叫出来.听起来她好像要哭了."
            narrator "我从未见过她这样失态..."
            scene cde_date1_61 with tstmgr

            narrator "当她的乳头受到刺激时,她似乎连反抗的能力都没有."
            narrator "我想也许有一天我会用到它."
            c "停下!!!Ahhhh............"
            d "我说过,我不会停下,直到你说\"请\"."
            scene cde_date1_62 with tstmgr

            c "你!!!......"
            scene cde_date1_59 with tstmgr

            c "Ah!!!我受不了了!......"
            scene cde_date1_63 with tstmgr

            c "请!请!请!请饶了我!"
            narrator "不可思议.狄奥多拉在祈求吗?我以为那只会发生在我的梦中."
            d "不够.继续求我."
            c "Hmm!!! ... ... Ah!!! ... ..."
            e "到此为止,艾琳.别让你姐姐难堪."
            scene cde_date1_64 with tstmgr

            d "Oh... "
            d "Okay,妈妈."
            narrator "艾琳放开了她的姐姐."
            scene cde_date1_65 with tstmgr

            d "看,[P].你应该这样对狄奥多拉."
            scene cde_date1_66 with tstmgr

            c "B,I,T,C,H(婊子)!"
            c "我要杀了你!"
            narrator "狄奥多拉就是这样反击的..."
            scene cde_date1_67 with tstmgr

            d "等等...不..."
            c "你会后悔出生的,妹妹!"
            d "不不不,救救我,妈妈!"
            d "[P]!救救我!"
            c "没人会救你的,婊子!"
            d "Nooooooooo!!! ... ... ... ..."
            scene cde_date1_68 with tstmgr

            narrator "狄奥多拉把艾琳拖到帐篷后面.我仍然能听到艾琳的尖叫声."
            narrator "我对那里的情况有点好奇..."
            player "Uh...你不阻止她们吗?"
            e "为什么我要?"
            e "这是促进她们关系的好方法.就让她们去玩吧."
            player "这真是...奇怪..."
            e "现在忘掉她们吧.你已经到了喝酒的年龄了,对吗?我带了一些啤酒.我们喝一杯吧."
            player "Oh... uh... Okay."
            scene void with tstmgr

            narrator "... ... ... ..."
            narrator "我仍然对帐篷后面发生的事感到好奇."
            narrator "... ... ... ..."

    scene void with tstmgr

    narrator "一段时间以后.太阳就要落山了."

    scene cde_date1_69 with tstmgr

    e "现在该回家了.谢谢,[P],很高兴你今天能和我们一起."

    e "多亏了你,我们都度过了美好的一天."

    d "不,一点也不好.我不快乐."

    scene cde_date1_71 with tstmgr

    c "没人在乎你怎么想."

    scene cde_date1_72 with tstmgr

    d "Hmmmmmmmmmm... ... ... ..."

    e "我想我们应该经常来野餐."

    player "Yeah...那会很有趣..."

    scene void with tstmgr

    narrator "... ... ... ..."

    narrator "今天就到这里了."

    narrator "... ... ... ..."

    stop music fadeout 1.0

    jump event_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
