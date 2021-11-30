default fortunetelling_today = False
default cleansing_today = False
default blessing_today = False
default fortunetelling_count = 0
default cleansing_count = 0
default blessing_count = 0

label shop:
    $ set_scene("Action")
    scene shop with tstmgr

    label shop.shop_menu:
    $ set_shop_ui()

    if seen('store_1_ft_firstime', 'store_1_bl_firstime'):
        $ shop_buy_service_badge = ""
    else:
        $ shop_buy_service_badge = "{image=badge2}"


    menu:
        posia "Hi,这里,小哥哥~ {fast}"
        "买她的服务 [shop_buy_service_badge]":


            label shop.shop_buy_serive:

            if not seen('store_1_cl_firstime'):
                $ shop_fortune_badge = "{image=badge2}"
            else:
                $ shop_fortune_badge = ""

            if not seen('store_1_bl_firstime'):
                $ shop_cleanse_badge = "{image=badge2}"
            else:
                $ shop_cleanse_badge = ""

            menu:
                "占卜 ($200) [shop_fortune_badge]" if not fortunetelling_today:
                    if not P.buy(200, _("占卜")):
                        jump shop.shop_menu

                    $ set_default_ui()
                    $ fortunetelling_today = True
                    $ fortunetelling_count += 1

                    if not seen('store_1_ft_firstime'):
                        $ run_event('store_1_ft_firstime')

                    elif fortunetelling_count == 4:
                        $ run_event('store_1_cl_firstime')
                    else:

                        $ rdc = RandomChoice(3)
                        if rdc(1):
                            $ run_event('store_1_ft_playlet1')
                        elif rdc(2):
                            $ run_event('store_1_ft_playlet2')
                        else:
                            $ run_event('store_1_ft_playlet3')

                "{color=#aaaaaa}Fortunetelling (come tomorrow){/color} [shop_fortune_badge]" if fortunetelling_today:
                    jump shop.shop_buy_serive

                "净化 ($500) [shop_cleanse_badge]" if seen("store_1_cl_firstime") and not cleansing_today:
                    if not P.buy(500, _("净化")):
                        jump shop.shop_menu

                    $ set_default_ui()
                    $ cleansing_today = True
                    $ cleansing_count += 1

                    if cleansing_count == 4:
                        $ run_event('store_1_bl_firstime')
                    else:

                        $ rdc = RandomChoice(2)
                        if rdc(1):
                            $ run_event('store_1_cl_playlet1')
                        elif rdc(2):
                            $ run_event('store_1_cl_playlet2')

                "{color=#aaaaaa}Cleansing (come tomorrow){/color} [shop_fortune_badge]" if seen("store_1_cl_firstime") and cleansing_today:
                    jump shop.shop_buy_serive

                "祝福 ($800)" if seen("store_1_bl_firstime") and not blessing_today:
                    if not P.buy(800, _("祝福")):
                        jump shop.shop_menu

                    $ set_default_ui()
                    $ blessing_today = True
                    $ blessing_count += 1

                    $ run_event('store_1_bl_playlet1')

                "{color=#aaaaaa}Blessing (come tomorrow){/color}" if seen("store_1_bl_firstime") and blessing_today:
                    jump shop.shop_buy_serive
                "返回":

                    jump shop.shop_menu
        "从她那里买些什么":

            label shop.buy_wallpaper:
            $ set_shop_ui_wide()
            menu:
                "薇拉的占星师套装墙纸 ($500)" if not BackgroundSystem.data["a_store_1"].is_shop_unlocked:
                    if P.buy(500, _("Wallpaper")):
                        $ BackgroundSystem.data["a_store_1"].unlock_from_shop()
                    jump shop.buy_wallpaper
                "森柠的占星师套装墙纸 ($500)" if not BackgroundSystem.data["b_store_1"].is_shop_unlocked:
                    if P.buy(500, _("Wallpaper")):
                        $ BackgroundSystem.data["b_store_1"].unlock_from_shop()
                    jump shop.buy_wallpaper
                "狄奥多拉的占星师套装墙纸 ($500)" if not BackgroundSystem.data["c_store_1"].is_shop_unlocked:
                    if P.buy(500, _("Wallpaper")):
                        $ BackgroundSystem.data["c_store_1"].unlock_from_shop()
                    jump shop.buy_wallpaper
                "艾琳的占星师套装墙纸 ($500)" if not BackgroundSystem.data["d_store_1"].is_shop_unlocked:
                    if P.buy(500, _("Wallpaper")):
                        $ BackgroundSystem.data["d_store_1"].unlock_from_shop()
                    jump shop.buy_wallpaper
                "伊莉莎的占星师套装墙纸 ($500)" if not BackgroundSystem.data["e_store_1"].is_shop_unlocked:
                    if P.buy(500, _("Wallpaper")):
                        $ BackgroundSystem.data["e_store_1"].unlock_from_shop()
                    jump shop.buy_wallpaper
                "瑞秋的占星师套装墙纸 ($500)" if not BackgroundSystem.data["f_store_1"].is_shop_unlocked:
                    if P.buy(500, _("Wallpaper")):
                        $ BackgroundSystem.data["f_store_1"].unlock_from_shop()
                    jump shop.buy_wallpaper
                "乌诺的占星师套装墙纸 ($500)" if not BackgroundSystem.data["g_store_1"].is_shop_unlocked:
                    if P.buy(500, _("Wallpaper")):
                        $ BackgroundSystem.data["g_store_1"].unlock_from_shop()
                    jump shop.buy_wallpaper
                "返回":
                    jump shop.shop_menu
        "返回":

            pass

    $ set_default_ui()
    jump action_post

default hotel_shop_chat_count = 0
default hotel_shop_chat_today = False
default satisfy_her_need_count = 0
default satisfy_her_need_today = False
label hotel_shop:
    $ set_scene("Action")
    scene hotel_shop with tstmgr

    label hotel_shop.shop_menu:
    $ set_hotel_shop_ui()

    if seen('store_2_more_firstime', 'store_2_sex_firstime'):
        $ hotel_interact_with_badge = ""
    else:
        $ hotel_interact_with_badge = "{image=badge2}"

    menu:
        minna "啊,这是我未来的女婿~{fast}"
        "与她互动 [hotel_interact_with_badge]":


            label hotel_shop.interact_with:

            if not seen('store_2_more_firstime'):
                $ hotel_shop_chat_badge = "{image=badge2}"
            else:
                $ hotel_shop_chat_badge = ""

            if not seen('store_2_sex_firstime'):
                $ satisfy_her_need_badge = "{image=badge2}"
            else:
                $ satisfy_her_need_badge = ""

            menu:
                "与她交谈 [hotel_shop_chat_badge]" if not hotel_shop_chat_today:
                    $ set_default_ui()
                    $ hotel_shop_chat_count += 1
                    $ hotel_shop_chat_today = True

                    $ rdc = RandomChoice(3)
                    if rdc(1):
                        $ run_event('store_2_chat_1')
                    elif rdc(2):
                        $ run_event('store_2_chat_2')
                    else:
                        $ run_event('store_2_chat_3')

                "{color=#aaaaaa}Talk with her (come tomorrow){/color} [hotel_shop_chat_badge]" if hotel_shop_chat_today:
                    jump hotel_shop.interact_with

                "满足她的需求 [satisfy_her_need_badge]" if what_about_me and not satisfy_her_need_today:
                    $ set_default_ui()
                    $ satisfy_her_need_count += 1
                    $ satisfy_her_need_today = True

                    $ rdc = RandomChoice(2)
                    if rdc(1):
                        $ run_event('store_2_more_playlet1')
                    else:
                        $ run_event('store_2_more_playlet2')

                "{color=#aaaaaa}Satisfy her need (come tomorrow){/color} [satisfy_her_need_badge]" if what_about_me and satisfy_her_need_today:
                    jump hotel_shop.interact_with
                "Back":

                    jump hotel_shop.shop_menu
        "从她那里买东西":

            label hotel_shop.buy_wallpaper:
            $ set_hotel_shop_ui_wide()
            menu:
                "穿着旗袍的薇拉墙纸 ($500)" if not BackgroundSystem.data["a_store_2"].is_shop_unlocked:
                    if P.buy(500, _("Wallpaper")):
                        $ BackgroundSystem.data["a_store_2"].unlock_from_shop()
                    jump hotel_shop.buy_wallpaper
                "穿着旗袍的森柠墙纸 ($500)" if not BackgroundSystem.data["b_store_2"].is_shop_unlocked:
                    if P.buy(500, _("Wallpaper")):
                        $ BackgroundSystem.data["b_store_2"].unlock_from_shop()
                    jump hotel_shop.buy_wallpaper
                "穿着旗袍的狄奥多拉墙纸 ($500)" if not BackgroundSystem.data["c_store_2"].is_shop_unlocked:
                    if P.buy(500, _("Wallpaper")):
                        $ BackgroundSystem.data["c_store_2"].unlock_from_shop()
                    jump hotel_shop.buy_wallpaper
                "穿着旗袍的艾琳墙纸 ($500)" if not BackgroundSystem.data["d_store_2"].is_shop_unlocked:
                    if P.buy(500, _("Wallpaper")):
                        $ BackgroundSystem.data["d_store_2"].unlock_from_shop()
                    jump hotel_shop.buy_wallpaper
                "穿着旗袍的伊莉莎墙纸 ($500)" if not BackgroundSystem.data["e_store_2"].is_shop_unlocked:
                    if P.buy(500, _("Wallpaper")):
                        $ BackgroundSystem.data["e_store_2"].unlock_from_shop()
                    jump hotel_shop.buy_wallpaper
                "穿着旗袍的瑞秋墙纸 ($500)" if not BackgroundSystem.data["f_store_2"].is_shop_unlocked:
                    if P.buy(500, _("Wallpaper")):
                        $ BackgroundSystem.data["f_store_2"].unlock_from_shop()
                    jump hotel_shop.buy_wallpaper
                "穿着旗袍的乌诺墙纸 ($500)" if not BackgroundSystem.data["g_store_2"].is_shop_unlocked:
                    if P.buy(500, _("Wallpaper")):
                        $ BackgroundSystem.data["g_store_2"].unlock_from_shop()
                    jump hotel_shop.buy_wallpaper
                "返回":
                    jump hotel_shop.shop_menu
        "返回":

            pass

    $ set_default_ui()
    jump action_post

label bungalow:
    if is_day():
        scene e_love_8_8 with tstmgr
    else:
        scene e_train_inti_1_4 with tstmgr
    "伊丽莎姨妈现在不在平房里,我肯定不会走过那片森林的..."
    jump action_post

label my_room_in_hotel:
    menu:
        "回房":
            if t.period < LateNight:
                "现在睡觉太早了."
            else:
                if t.period < LateNight:
                    "现在睡觉太早了."
                else:
                    $ new_day()
        "返回":
            pass
    jump action_post

label my_room:
    hide screen bnb
    $ show_home()
    jump action_post



label course:

    if not seen('B_love_1'):
        scene class_background with tstmgr
        "我去了一个班,花了一些时间来学习."
        "我试图与森柠交谈,但她仍然对我很生气."
        "... ... ... ..."
    else:
        scene go_to_class with tstmgr
        $ rdc = RandomChoice(3)
        if rdc(1):
            b "本课结束时将有一次测验,记得不要提前离开."
        elif rdc(2):
            b "教授说,下次考试不会涉及今天的课,所以... ..."
        else:
            b "嗨,[P].让我们坐在一起."
        "我在森柠的课堂上花了一些时间."
        "... ... ... ..."

    $ add(B, B.love, 1)
    $ time_proceed(1)
    jump action_post



default days_worked = 0
label work:

    scene go_to_work with tstmgr
    $ rdc = RandomChoice(3)
    if rdc(1):
        c "继续这样工作,你很快就会被提拔."
    elif rdc(2):
        c "如果你有任何问题,请随时到我的办公室找我."
    else:
        c "你最近去了我妈妈的家吗?她和艾琳怎么样了?"

    "我花了一些时间在公司工作."
    "... ... ... ..."

    $ add(C, C.love, 1)
    $ days_worked += 1

    if renpy.random.random() <= 0.5 and not E.love.is_locked:
        call E_inspect_work

    $ time_proceed(1)

    jump action_post

label find_C_company:

    scene expression find_bg(C) with Dissolve(0.5)

    "我没有太多的时间.什么事?"

    $ show_find_fix(C)

    jump action_post



default B_gift = False
default D_gift = False
label street:

    if is_day():
        scene downtown_day_background
    else:
        scene downtown_night_background
    "我真希望我可以带着某人来这里… …"

    if not B_gift or not D_gift:

        label downtown_menu:
        menu:
            "给森柠买礼物 ($2000)" if not B_gift:
                $ P.buy(2000, _("Gift"))
                $ B_gift = True
                jump downtown_menu
            "给艾琳买礼物 ($5000)" if not D_gift:
                $ P.buy(5000, _("Gift"))
                $ D_gift = True
                jump downtown_menu
            "返回":
                $ time_proceed(1)
                jump action_post

    jump action_post




label B_room:
    if seen("d5_2") and not seen("B_love_1"):
        scene b_school_day_unhappy with tstmgr




        b "... ... ... ..."
        $ show_map()
        jump action_post

    scene expression find_bg(B) with Dissolve(0.5)

    b "Hello, [P.name], 见到你真好."

    $ show_find_fix(B)

    jump action_post

label C_room:
    if is_day():
        scene croom_day_background with tstmgr
    else:
        scene croom_night_background with tstmgr

    "这是狄奥多拉的旧房间.在她从这座豪宅搬走后,没有人住在这里.但是伊莉莎阿姨仍然把这个房间保持得很好很干净.."
    jump action_post

label D_room:
    if not seen("D_dqsj"):
        scene void with tstmgr
        narrator "艾琳还在生我的气.我应该去给她买个礼物,然后再回来找她."
        $ show_map()
        jump pauser

    scene expression find_bg(D) with Dissolve(0.5)

    d "[P.name]!"

    $ show_find_fix(D)

    jump action_post

label E_room:
    scene expression find_bg(E) with Dissolve(0.5)

    e "见到你真好, [P]!"

    $ show_find_fix(E)

    jump action_post

label F_room:
    scene expression find_bg(F) with Dissolve(0.5)

    if F.love >= 25 and not seen("A_love_5"):
        $ Push("在你改善与维拉的关系后,她的更多故事将被解锁")

    d "[P.name]!"

    $ show_find_fix(F)

    jump action_post

label tutor:

    scene ddqsj_d5 with tstmgr
    "我花了更多时间辅导艾琳."

    $ add(D, D.love, 1)
    $ P.earn(50, _("辅导"), t)
    $ time_proceed(1)

    if renpy.random.random() <= 0.5 and not E.love.is_locked:
        call E_inspect_tutor
    jump action_post



label booking:
    jump action_post




label bookstore:



    scene g_bookstore_smile with tstmgr

    g "Hi, [P]."

    g "你在找书吗?"

    player "没有,只是来看看你的情况."

    scene g_bookstore_normal with tstmgr

    g "... ... ... ..."

    $ add(G, G.love, 1)

    $ time_proceed(1)

    jump action_post

label supermarket:
    jump action_post




label exercise:

    if exercise.count_of_day == 0:
        scene go_to_sports with tstmgr
        $ rdc = RandomChoice(3)
        if rdc(1):
            f "你好,我的朋友.我要去慢跑了.你和我一起吗??"
        elif rdc(2):
            f "不要懒惰.让我们一起流汗."
        else:
            f "你为什么盯着我看?来吧,我们去跑步吧!"

        "我和瑞秋在公园里呆了一会儿."
        "... ... ... ..."
        $ add(F, F.love, 1)
        $ time_proceed(1)
    else:
        "我今天太累了."



    jump action_post

label alley:
    scene alley_background with tstmgr
    "一个黑暗的、令人毛骨悚然的、危险的小巷.我为什么要独自来到这里?"
    jump action_post

label beach:
    scene beach_background with tstmgr
    "这个海滩是这个城市的一个著名的风景区.但一个人来到这里有点可怜.."
    jump action_post




label G_room:

    scene expression find_bg(G) with Dissolve(0.5)

    g "... ... ... ... Hi..."

    $ show_find_fix(G)

    jump action_post

default first_A_room = True
label A_room:

    if first_A_room:
        "现在维拉和我住在彼此的隔壁.我可以每天与她见面."
        "但请记住,除了星期天,她每天只在早上和深夜在她的房间里.. "
        "嗯,她现在在家,我想现在可能是和她谈谈的好时机.."
        "(c敲门,敲门,敲门.)"
        a "这是谁?"
        player "是我, [P]."
        a "哦,等一下,我现在正在换衣服."
        "换衣服了?所以她现在是半裸着跟我说话?这......真的吸引了我的想象力..."
        "(门开了)"
        $ first_A_room = False

    if seen("A_love_4") and not seen("A_love_5"):
        "她现在没有心情."
        $ show_map()
        jump action_post

    scene expression find_bg(A) with Dissolve(0.5)

    $ show_find_fix(A)

    jump action_post

label C_room_2:
    if is_day():
        scene bnb_croom_background with tstmgr
        "狄奥多拉不在她的房间里."
        "... ... ... ..."
    else:
        scene void with tstmgr
        "狄奥多拉锁上了她的门.也许她不想让别人知道她在做什么.."
        "... ... ... ..."
    jump action_post



label find_A_cafe:

    if seen("A_love_4") and not seen("A_love_5"):
        scene a_cafe_weird with tstmgr
        a "... ... ... ..."
        "她现在没有心情."
        $ add(A, A.love, 1)
        $ time_proceed(1)
        jump action_post

    scene cafe_background with tstmgr
    player "嗨,薇拉"
    scene a_cafe_normal1 with tstmgr
    a "[P.name]?"
    a "你今天想吃什么?"
    scene cafe_background with tstmgr
    "... ... ... ..."

    $ add(A, A.love, 1)


    $ time_proceed(1)
    jump action_post


label find_A_clothing:

    if seen("A_love_4") and not seen("A_love_5"):
        scene a_dressstore_frown with tstmgr
        a "... ... ... ..."
        "她现在没有心情."
        $ add(A, A.love, 1)
        $ time_proceed(1)
        jump action_post

    if A.relation == "general":
        scene a_dressstore_weird with tstmgr
        a "... ... ... ..."
        a "你又来了..."
        scene dressstore_background with tstmgr
        "... ... ... ..."
        $ add(A, A.love, 1)
        $ time_proceed(1)
    else:


























        scene a_dressstore_smile3

        a "Hello, [P]."

        a "Thanks for coming to see me. I'm bored to death right now."

        a "… … … …"

        $ add(A, A.love, 1)

        $ time_proceed(1)




    jump action_post


label find_A_restaurant:

    if seen("A_love_4") and not seen("A_love_5"):
        scene bar_background with tstmgr
        "... ... ... ..."
        "Vera is not in the mood right now."
        $ add(A, A.love, 1)
        $ time_proceed(1)
        jump action_post

    scene a_restaurant_smile with tstmgr
    a "[P.name]?"
    player "Hi, Vera."
    a "What can I get for you?"
    player "Nothing but a cup of beer, please. I'm just waiting for you getting off work."
    scene a_restaurant_slight_surprise with tstmgr
    a "Oh, okay..."
    scene bar_background with tstmgr
    "... ... ... ..."

    $ add(A, A.love, 1)
    $ time_proceed(1)




    jump action_post




label hang_park:
    if is_day():
        scene park_day_background with tstmgr
    else:
        scene park_night_background with tstmgr
    "I took a walk at the park. Nothing special."

    $ time_proceed(1)
    jump action_post



label map:
    jump action_post
label hotel:
    jump action_post
label my_house:
    jump action_post
label park:
    jump action_post
label college:
    jump action_post
label mansion:
    jump action_post
label cafe:
    jump action_post
label bar:
    jump action_post
label mall:
    jump action_post
label clothing:
    jump action_post
label company:
    jump action_post