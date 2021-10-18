label B_date_1:

    scene map_day with dissolve
    play music happy

    narrator "多么可爱的周末.想想看,我今天应该做什么?"

    narrator "呆在我房间玩PS4?那太乏味."

    narrator "回顾课程材料吗?天,这太可怜了."

    narrator "... ... ... ..."

    narrator "也许我应该约森柠出去共度时光."

    narrator "我给她打了个电话."

    b "你好,[P.name]."

    player "嗨,森柠,你今天有空吗?"

    b "Hmm...有空.怎么了?"

    player "你想和我一起去兜风吗?你还没有看到我的新车,对吗?我两个月前才买的."

    b "听起来不错.我们什么时候去?"

    player "我半小时后到你的公寓."

    scene void with tstmgr

    narrator "... ... ... ..."

    narrator "半小时后..."

    scene b_date1_1 with tstmgr

    player "嗨,森柠."

    menu:
        "你看起来很棒":

            scene b_date1_2 with tstmgr
            b "谢谢."
            scene b_date1_4 with tstmgr
            b "所以这是你的新车?"
        "为什么这么久才来?":

            scene b_date1_3 with tstmgr
            b "对不起,我在化妆上花了太多时间."
            player "没什么大不了的,值得等待.你看起来很漂亮."
            scene b_date1_2 with tstmgr
            b "谢谢."
            scene b_date1_4 with tstmgr
            b "所以这是你的新车?"

    player "如何?"

    scene b_date1_3 with tstmgr

    b "非常棒..."

    if not seen('pcsj'):

        b "但这是不是有点太张扬了?"

        menu:
            "这就是我买下她的原因":
                pass
            "我同意你的看法,但她真的很好":

                pass
    else:

        b "但是它一定需要很多钱来维护.你现在负担得起吗?"

        player "这确实是个问题.所以我现在很少开车了.今天是个例外."

        b "你为什么不把它卖了呢?"

        player "我永远不会卖掉我的车.她是我的朋友.此外,我只买了她两个月."


    b "为什么用\"她\"? ..."

    b "奇怪..."

    narrator "她上了我的车.然后我们开车离开学校去海边大道."

    scene b_date1_5 with tstmgr

    narrator "我应该选择哪个话题开始对话?"

    menu:
        "谈论汽车":


            player "你能感觉到速度吗?你能听到引擎轰鸣吗?如此美妙的交响乐!"
            scene b_date1_6 with tstmgr

            b "Eh...我对汽车了解不多."
            b "但是你现在超速了吗?车速限制是70英里."
            player "Oh,ah,操."
            player "我不是故意的.我一定是上头了."
            scene b_date1_5 with tstmgr

            b "没什么.我只是希望你开车时更小心些."
            b "你知道,我最喜欢的电影明星之一死于车祸."
            player "谢谢你的关心..."
            narrator "这个时刻变得越来越尴尬.我应该换个话题."
            narrator "她刚刚谈到了她最喜欢的电影明星.谈谈电影怎么样?"
            narrator "So... ..."

            menu:
                "谈论浪漫电影":

                    player "你知道,我们学校的剧院下周将放映一些经典的浪漫电影.你想看吗?"
                    scene b_date1_8 with tstmgr

                    b "具体放映什么电影?"
                    player "《泰坦尼克号》,《人鬼情未了》和其他一些我不记得的电影."
                    b "我还从没看过人鬼情未了.好看吗?"
                    player "这是世界上最浪漫的电影之一.我可以向你保证."
                    player "你知道,当它第一次在蒙特利尔上映的时候,每个女观众都会收到一个信封,里面有一些纸巾,以防她们哭."
                    b "男性没有吗?"
                    player "Yep,只有女士有."
                    scene b_date1_6 with tstmgr

                    b "那在今天看来,这听起来像是性别歧视."
                    player "Yeah,我认为他们不会再这样做了."
                    player "但是不管怎样,那部电影真的很棒.如果你还没看过,你一定要去看."
                    scene b_date1_7 with tstmgr

                    b "很好.下周我们一起看."
                    narrator "和她一起看浪漫电影?哇,我怎么能拒绝呢?"
                    player "这将会很棒的!"
                "谈论中国电影":



                    player "我不熟悉中国电影.你能给我讲讲吗?"
                    b "你想知道什么?"
                    player "比如,中国的电影行业,怎么样?"
                    scene b_date1_7 with tstmgr

                    b "我不专业,所以我说的听听就好."
                    b "中国电影市场规模庞大,购买力强,产业规模巨大."
                    b "有时候,中国对一部好莱坞电影的票房贡献可能比世界其他地方还要高."
                    player "这听起来...令人吃惊."
                    b "但遗憾的是,尽管中国每年制作400多部电影,但只有少数是好电影.其余的都是垃圾."
                    b "因为人们意识到他们并不真的需要制作一部好电影来在这么大的市场中获利."
                    player "嗯,这很合理.他们都是商人."
                    player "你有什么中国电影可以推荐吗?"
                    b "就在几个月前,中国刚刚上映了一部很好的科幻电影《流浪地球》.你现在可以在网飞上观看."
                    player "科幻电影吗.听起来很酷.我去看看."
                    narrator "... ... ... ..."
        "谈论她":

            player "这周过得怎么样?"
            b "没什么特别的,到目前为止还不错."
            player "我也是.如果你不接受这个约会,我会闷死的."
            scene b_date1_8 with tstmgr

            b "等等,这是约会?"
            player "呃,怎么了?"
            b "我以为只有情侣才能约会."
            player "不,不是这样的."
            narrator "... ... ... ..."

            menu:
                "谈谈她的恋爱经历":

                    player "你曾经和一个男孩交往过吗?"
                    scene b_date1_6 with tstmgr

                    b "我在中国上高中的时候有过一次."
                    narrator "Wow,这是我不知道的.我以为她的感情生活是一张白纸."
                    b "但是...我们之间什么也没发生."
                    b "在中国,高中生被禁止谈恋爱."
                    b "所以...我们什么也不敢做.我们从不亲吻,拥抱,甚至不握对方的手."
                    player "这...真难受."
                    b "事实上,是的..."
                    player "所以这只是柏拉图式的关系?"
                    b "是的...我想是这样的."
                    narrator "看来她的爱情生活就像一张白纸."
                    player "我为你感到难过,森柠,真的."
                    player "我认为...既然你已经上了大学,这可能是你和某人开始一段真正关系的好时机."
                    scene b_date1_7 with tstmgr

                    b "... ... ... ..."
                    b "我会考虑的."
                "谈谈她目前的恋爱状况":




                    player "跟我说实话.我们学校有你喜欢的男生吗?"
                    scene b_date1_6 with tstmgr

                    b "Eh...为什么这么问?"
                    player "我们是好朋友,不是吗?我问是因为我关心你."
                    scene b_date1_7 with tstmgr

                    b "好吧好吧..."
                    b "我喜欢你."
                    player "Oh,我不会随便评价的...等等,什么?"
                    b "你是我在这个国家最好的朋友.我怎么会不喜欢你?"
                    player "... ... ... ..."
                    player "我知道你什么意思了."
                    player "别想愚弄我.你知道那不是我要问的.我在问你有没有潜在的男朋友目标."
                    scene b_date1_6 with tstmgr

                    b "Oh..."
                    b "这是个秘密..."
                    player "我就当你默认了.那真是个幸运的家伙."
                    scene b_date1_5 with tstmgr

                    b "... ... ... ..."
                    b "(小声说话)你真傻..."



    narrator "... ... ... ..."

    narrator "一路上我们聊得很开心.森柠在公共场合看起来很内向,但当她和我在一起时,她变得很外向.我们基本上什么都谈."

    player "这是你的新衣服吗?我从来没见你穿过它."

    b "是的,看起来怎么样?"

    player "无论你穿什么,你看起来都很棒,这件衣服让你看起来更棒."

    scene b_date1_9 with tstmgr

    b "谢谢.你真会说话."

    player "但是,说实话,我有点失望."

    scene b_date1_6 with tstmgr

    b "这是为什么?"

    player "我以为你会穿一些不那么保守的衣服.我是说,你身材很好,但你总是把它藏在衣服里.这是一个遗憾."

    b "我们已经讨论过了.我不喜欢穿那些性感的衣服.这不是我的风格."

    player "但是如果你在海滩上呢?你不穿比基尼吗?这是最性感的."

    b "这是...不同的."

    player "你在沙滩上穿比基尼吗?听你这么说真高兴."

    scene b_date1_5 with tstmgr

    player "... ... ... ..."

    menu:
        "建议去海滩":

            player "我们今天去海滩怎么样?现在时间还早."
            scene b_date1_6 with tstmgr

            b "什么?但是我没有带我的泳衣..."
            player "没关系.我开车送你回去拿."
            b "... ... ... ..."
            b "你为什么对它如此热情?你这么想看到我穿比基尼吗?"
            player "Yep,没错."
            narrator "诚实是一种美德."
            b "... ... ... ..."
            scene b_date1_5 with tstmgr

            b "好吧.反正我也没有别的事可做."
            player "你同意了吗?太好了!"
            narrator "我转过身,开车送她回公寓."
            narrator "... ... ... ..."

            scene void with dissolve

            narrator "两小时以后......"
            narrator "接下来发生的事出乎我们的意料——我们遇到了大塞车.当我们终于到达海滩时,太阳就要下山了,没有其他人在海滩上."
            narrator "但是...事实证明,这实际上是一件好事."
            narrator "... ... ... ..."
            b "我看起来怎么样?"

            $ openeyes("b_date1_10")

            narrator "森柠穿着比基尼.她像黄昏女神一样向我走来."
            narrator "她看起来和平常一样漂亮,但是性感多了.夕阳在她的身后闪耀,使她端庄如天仙."
            narrator "阳光照在她白皙的皮肤上,照在她丰满的乳房上,照在她平坦的肚子上.现在她是...女神..."
            narrator "我贪婪地看着她,就像看着一件珍贵的艺术品."
            narrator "我不知道说什么好."
            scene b_date1_11 with tstmgr

            narrator "她坐在我的旁边."
            b "你怎么如此安静?"
            player "... ... ... ..."
            player "你看起来...令人惊讶."
            b "就这些吗?没有其他的?"
            player "你还想让我看到什么?你从我脸上看不出来吗?"
            player "你就像一个女神来到现实中..."
            player "我很幸运,现在只有我一个人看到了这一切."
            scene b_date1_12 with tstmgr

            b "Hmm,谢谢你."
            b "... ... ... ..."
            b "我有个问题要问你,一个愚蠢的问题.你可以选择不回答."
            player "说吧."
            b "我是你见过的最漂亮的比基尼女郎吗?"
            narrator "是吗?"
            narrator "当然是的..."
            narrator "但是..."
            narrator "森柠问完这个问题后,我脑海中浮现出另一个女孩的脸."
            scene day2_c10 with flashback

            narrator "狄奥多拉."
            narrator "虽然狄奥多拉和我并不是很合得来,但我还是不得不承认,她穿泳衣的样子非常迷人.我认为没有人能抗拒她."
            narrator "那么谁更好呢?森柠?或者狄奥多拉?"
            narrator "我该怎么回答她呢?"

            menu:
                "你是我见过最漂亮的.":
                    scene b_date1_12 with flashback

                    b "真的吗?谢谢你这样说."
                    b "我不知道你说的是不是真的,但我还是很高兴."
                    player "你为什么觉得我在说谎?"
                    b "因为你是个花花公子,认识很多女孩.一定有比我更好的."
                    player "Well..."
                    player "首先,我不是一个花花公子.我是个有美德的人."
                    player "第二,你应该对自己更有信心.我刚才说的完全正确.你真的是我这辈子见过的最好的比基尼女郎."
                    b "... ... ... ..."
                    b "好吧..."
                    b "谢谢你..."
                    narrator "... ... ... ..."
                "你是我见过最美丽的人之一.":

                    scene b_date1_11 with flashback
                    b "\"之一\"?"
                    scene b_date1_12 with tstmgr

                    b "好吧,至少你很诚实."
                    player "请不要误会.你看起来很棒,但是我..."
                    narrator "她用眼神阻止了我的解释."
                    narrator "... ... ... ..."
                    narrator "事实上,她似乎并不生气.也许就像她说的,那只是一个愚蠢的问题."
                    narrator "... ... ... ..."

            scene b_date1_13 with tstmgr

            b "日落真是太美了."
            player "Yeah,我们一定要多来看看这个,就我们两个人."
            b "... ... ... ..."
            b "我同意这个观点."
            narrator "我们并排坐在海滩上.直到太阳完全消失在地平线下,我们才离开."
        "建议结束这个约会":


            scene b_date1_5 with tstmgr
            player "我真的很想建议现在去海滩,但是现在是下午的交通高峰期.如果我们现在不回去,我们肯定会遇到交通堵塞."
            scene b_date1_6 with tstmgr

            b "... ... ... ..."
            b "你是对的.我们也许应该回去."
            player "我们下次再去海滩吧?"
            scene b_date1_7 with tstmgr

            b "em, okay."

    scene void with tstmgr

    narrator "... ... ... ..."

    narrator "我很晚才回家."

    stop music fadeout 1.0

    jump event_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
