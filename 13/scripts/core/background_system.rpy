default persistent.bg_states = {}
default persistent.bg_states_2 = {}
default save_bg_states = {}

python early:
    class BackgroundState(object):
        def __init__(self, name, has_password):
            self.name = name
            if has_password:
                self.is_password_unlocked = False
            else:
                self.is_password_unlocked = True
        
        def __repr__(self):
            return "{}".format("unlocked" if self.is_password_unlocked else "locked")
        
        def __eq__(self, other):
            if isinstance(self, BackgroundState) \
        and self.name == other.name \
        and self.is_password_unlocked == other.is_password_unlocked:
                return True
            
            return False

init python:
    class Background(object):
        def __init__(self, name, password=None, dname=[], pre_events=[], tweet=None):
            self.name = name
            self.dname = dname
            self.pre_events = pre_events
            self.thumbnail = name + "_thumbnail"
            self.password = password
            if password:
                
                self.mosaic_thumbnail = dark(im.Blur("images/thumbnails/"+name+"_thumbnail.webp", 3))
            self.darkins_thumbnail = dark_insensitive("images/thumbnails/"+name+"_thumbnail.webp")
            
            self.tweet = tweet
        
        @property
        def is_password_unlocked(self):
            if self.name in persistent.bg_states_2:
                return persistent.bg_states_2[self.name]
            else:
                return True
        
        @property
        def is_plot_unlocked(self):
            for event in self.pre_events:
                if not seen(event):
                    return False
            return True
        
        @property
        def is_shop_unlocked(self):
            if self.name in save_bg_states:
                return save_bg_states[self.name]
            else:
                return True
        
        @property
        def is_unlocked(self):
            return self.is_password_unlocked and self.is_plot_unlocked and self.is_shop_unlocked
        
        def unlock_from_shop(self):
            save_bg_states[self.name] = True
        
        def unlock_by_password(self, password):
            if password == self.password:
                persistent.bg_states_2[self.name] = True
                Push("背景已解锁.")
                return True
            else:
                Push("密码错误.")
                return False
        
        def __repr__(self):
            return "Background(" + self.name + ")"

    class BackgroundSystem(object):
        data = {}
        states = {}
        current = {}
        
        @classmethod
        def add(cls, name, *args):
            bg = Background(name, *args)
            cls.data[name] = bg
            if not name in persistent.bg_states_2:
                
                persistent.bg_states_2[name] = False if bg.password else True
        
        
        @classmethod
        def add_to_shop(cls, name, *args):
            bg = Background(name, *args)
            cls.data[name] = bg
            if not name in save_bg_states:
                save_bg_states[name] = False
        
        @classmethod
        def get_backgrounds(cls):
            return cls.data.values()
        
        @classmethod
        def get_nz_backgrounds(cls, nz):
            return [bg for name, bg in cls.data.items() if name[0].upper() == nz.code]
        
        @classmethod
        def set_nz_background(cls, nz, bg):
            if bg:
                if bg.is_unlocked:
                    cls.current[nz.code] = bg.name
                    store._bubble_what = bg.tweet
                elif bg.is_shop_unlocked == False:
                    Push("你可以在波西亚或明娜的店里解锁这张照片.")
                else:
                    Push("你可以在推进更多关于她的剧情后解锁这张照片.")
            else:
                cls.current[nz.code] = None
                idx = int(random.random() * len(findee.tweets[findee.relation]))
                store._bubble_what = findee.tweets[findee.relation][idx]
        
        @classmethod
        def get_nz_background(cls, nz):
            if cls.current.get(nz.code, None):
                return cls.current.get(nz.code, None)
            return cls.get_default_nz_background(nz)
        
        @classmethod
        def get_default_nz_background_thumbnail(cls, nz):
            default_name = cls.get_default_nz_background(nz)
            for filepath in renpy.list_files():
                imagename = os.path.basename(filepath).split(".")[0]
                if imagename == default_name:
                    return im.Scale(filepath, 460, 259)
            return "void_thumbnail"
        
        @classmethod
        def get_default_nz_background(cls, nz):
            if nz.relation in ("girlfriend", "sexpartner", "fiancee"):
                relation = "gf"
            else:
                relation = nz.relation
            return "{}_{}_{}_{}".format(nz.code.lower(), relation, nz.clothes, "default")

    def find_bg(nz):
        if BackgroundSystem.get_nz_background(nz):
            return BackgroundSystem.get_nz_background(nz)
        if nz.relation in ("girlfriend", "sexpartner", "fiancee"):
            relation = "gf"
        else:
            relation = nz.relation
        return "{}_{}_{}_{}".format(nz.code.lower(), relation, nz.clothes, "default") 

    password_for_10 = "07578"
    password_for_20 = "78351"
    password_forbit = "𗀀"
    reward_str_for_10 = "{color=#dd6574}{size=-3}$10 奖励{/size}{/color}"
    reward_str_for_20 = "{color=#f4cc6c}{size=-3}$20 奖励{/size}{/color}"
    shop_str = "{color=#a186be}{size=-3}波西亚的商店{/size}{/color}"
    shop2_str = "{color=#a186be}{size=-3}明娜的商店{/size}{/color}"

    BackgroundSystem.add("b_v7_10", password_for_10, ["[reward_str_for_10]年轻的森柠"], [],
        "很...开心...看到...你,[P].")
    BackgroundSystem.add("c_v7_10", password_for_10, ["[reward_str_for_10]年轻的狄奥"], [],
        "你没有忘记你答应过我的事吧?")
    BackgroundSystem.add("c_v7_20", password_for_20, ["[reward_str_for_20]礼物套装"], [],
        "我不是个礼物,但是......无所谓了~")
    BackgroundSystem.add("d_v7_20", password_for_20, ["[reward_str_for_20]礼物套装"], [],
        "惊喜!~艾琳就是给你的礼物!~")
    BackgroundSystem.add("a_normal_1", None, ["女仆套装"], ["A_daily_10"],
        "我是你的专属女仆,hah~~")
    BackgroundSystem.add("b_normal_1", None, ["黄色衬衫"], [],
        "谢谢你来看我,[P]..."),
    BackgroundSystem.add("b_normal_2", None, ["黑寡妇"], ["B_train_sha_1"],
        "你喜欢我穿成这样吗?")
    BackgroundSystem.add("c_normal_1", None, ["白色长裙"], ["C_love_5"],
        "请坐~")
    BackgroundSystem.add("d_normal_1", None, ["学生制服"], [],
        "艾琳是一个好学生~艾琳是一个好学生~~"),
    BackgroundSystem.add("d_normal_2", None, ["猫制服"], ["D_love_6"],
        "Meow~~ Meow~~ Meow meow meow~~~")
    BackgroundSystem.add("g_normal_1", None, ["coser制服"], [],
        "Hi,我的房东先生~")

    BackgroundSystem.add("d_v8_10", password_for_10, ["[reward_str_for_10]成熟的艾琳"], [],
        "Ah!~好久不见了,欧尼酱~")
    BackgroundSystem.add("e_v8_10", password_for_10, ["[reward_str_for_10]年轻的伊莉莎"], [],
        "为什么它...止不住的流?")
    BackgroundSystem.add("e_v8_20", password_for_20, ["[reward_str_for_20]礼物套装"], [],
        "小心点,主人,这个礼物很容易碎~")
    BackgroundSystem.add("a_v8_20", password_for_20, ["[reward_str_for_20]黑暗精灵薇拉"], [],
        "这个湖...被人类的气味腐蚀了吗......")
    BackgroundSystem.add("c_v8_20", password_for_20, ["[reward_str_for_20]战士西奥"], [],
        "有一天我能让这片土地恢复和平吗?")

    BackgroundSystem.add("b_normal_3", None, ["这是我的衬衫!"], ["B_love_6"],
        "我...我明天就会把这件衬衫还给你,所以......")
    BackgroundSystem.add("g_normal_2", None, ["睡衣"], ["G_love_6"],
        "这件衣服...一直从我肩膀上往下滑...")
    BackgroundSystem.add("d_v9_10", password_for_10, ["[reward_str_for_10]吸血鬼公主艾琳"], [],
        "不给糖就捣蛋!~~艾琳不需要糖果,她需要你的血,或者你身体里的其他液体~")
    BackgroundSystem.add("d_v9_20", password_for_20, ["[reward_str_for_20]猫忍者艾琳"], [],
        "Meowmeow~看剑!~")
    BackgroundSystem.add("f_v9_10", password_for_10, ["[reward_str_for_10]异国公主瑞秋"], [],
        "欢迎来到我的王国,旅行者~")
    BackgroundSystem.add("g_v9_20", password_for_20, ["[reward_str_for_20]猫忍者乌诺"], [],
        "你确定...这是我训练的一部分吗?Meow......")


    BackgroundSystem.add("b_v10_10", password_for_10, ["[reward_str_for_10]成熟的森柠"], [],
        "我们...终于又见面了......")
    BackgroundSystem.add("g_v10_10", password_for_10, ["[reward_str_for_10]比基尼战士"], [],
        "你能帮我拍张照片吗?~~")
    BackgroundSystem.add("a_v10_20", password_for_20, ["[reward_str_for_20]狂野西部"], [],
        "来吧,和我一起沉浸在荒野中~")
    BackgroundSystem.add("e_v10_20", password_for_20, ["[reward_str_for_20]狂野西部"], [],
        "跟上,牛仔.太阳就要落山了~")


    BackgroundSystem.add("c_v11_10", password_for_10, ["[reward_str_for_10] Theodora 女仆装"], [],
        "先别烦我，我还有工作要做...")
    BackgroundSystem.add("d_v11_10", password_for_10, ["[reward_str_for_10] Irene 女仆装"], [],
        "艾琳把拖把放在哪里了?... ...")
    BackgroundSystem.add("e_v11_20", password_for_20, ["[reward_str_for_20] Elisa 女皇"], [],
        "欢迎回来，我的国王~")
    BackgroundSystem.add("g_v11_20", password_for_20, ["[reward_str_for_20] 被俘的警察 Uno"], [],
        "Wuuuuuummmmmmmmmmm~~~~~~~~")


    BackgroundSystem.add("b_v12_20", password_for_20, ["[reward_str_for_20] 实习护士"], [],
        "抱歉......如果我打针弄疼了你，就咬住我的乳头吧......。")
    BackgroundSystem.add("f_v12_20", password_for_20, ["[reward_str_for_20] 船长瑞秋"], [],
        "嗯嗯......。但首先我必须建造我自己的船~。")
    BackgroundSystem.add("a_v12_10", password_for_10, ["[reward_str_for_10] 好色女仆薇拉"], [],
        "我......正准备清理浴室，我的主人......。")
    BackgroundSystem.add("g_v12_10", password_for_10, ["[reward_str_for_10] 巫女乌诺"], [],
        "我现在要去洗澡了，别看了！~。")


    BackgroundSystem.add("a_v13_10", password_for_10, ["[reward_str_for_10] 比基尼战士薇拉"], [],
        "有没有......我可以帮助的东西呢？例如，来一发~")
    BackgroundSystem.add("e_v13_10", password_for_10, ["[reward_str_for_10] 围裙裸装伊莉莎"], [],
        "你想吃点牛奶蛋糕吗？")
    BackgroundSystem.add("c_v13_20", password_for_20, ["[reward_str_for_20] 婚纱礼服"], [],
        "现在你拥有了......我的身体，我的心，我的一切～")
    BackgroundSystem.add("b_v13_20", password_for_20, ["[reward_str_for_20] 兔女郎森柠"], [],
        "我就在这里......只为你服务~")


    def save_bg_init():
        BackgroundSystem.add_to_shop("a_store_1", None, ["[shop_str]占星服"], [],
            "这套衣服...很贵,是吗?")
        BackgroundSystem.add_to_shop("b_store_1", None, ["[shop_str]占星服"], [],
            "我应该戴一副墨镜吗?这样看起来更有说服力,对吧?")
        BackgroundSystem.add_to_shop("c_store_1", None, ["[shop_str]占星服"], [],
            "信不信由你,你将会有糟糕的一天~")
        BackgroundSystem.add_to_shop("d_store_1", None, ["[shop_str]占星服"], [],
            "艾琳是个法师~我能把你变成一只绵羊或别的什么吗?~")
        BackgroundSystem.add_to_shop("e_store_1", None, ["[shop_str]占星服"], [],
            "我...我现在该说什么?嘛咪嘛咪哄?")
        BackgroundSystem.add_to_shop("f_store_1", None, ["[shop_str]占星服"], [],
            "Awwww...这真的不是我的风格......")
        BackgroundSystem.add_to_shop("g_store_1", None, ["[shop_str]占星服"], [],
            "我觉得我现在可以和大自然交流了~")
        
        BackgroundSystem.add_to_shop("a_store_2", None, ["[shop2_str]旗袍"], [],
            "谢谢你给我买这件衣服.我非常喜欢~")
        BackgroundSystem.add_to_shop("b_store_2", None, ["[shop2_str]旗袍"], [],
            "祝你新年快乐,春节快乐!")
        BackgroundSystem.add_to_shop("c_store_2", None, ["[shop2_str]旗袍"], [],
            "我真的不应该在上班的时候穿这样的衣服,但是...算了......")
        BackgroundSystem.add_to_shop("d_store_2", None, ["[shop2_str]旗袍"], [],
            "我...穿这件衣服显得成熟吗?我是说,一只成熟的小猫~")
        BackgroundSystem.add_to_shop("e_store_2", None, ["[shop2_str]旗袍"], [],
            "Ah,一件旗袍,好少见.我记得在许多年前的一个时装周上,我曾经看到一位优雅的女士穿着这种衣服.")
        BackgroundSystem.add_to_shop("f_store_2", None, ["[shop2_str]旗袍"], [],
            "我以前从来没有尝试过这种风格.什么?我好看吗?你...确定?")
        BackgroundSystem.add_to_shop("g_store_2", None, ["[shop2_str]旗袍"], [],
            "我不知道，但是......这件衣服真的很适合我呢～")

screen bg_selection():

    zorder 100

    button:
        action Hide("bg_selection", transition=Dissolve(0.3))

    frame:
        align 0.5, 0.5
        xysize 1600, 1080

        has vpgrid:
            cols 3
            mousewheel True
            arrowkeys True
            draggable True
            scrollbars "vertical"

            xysize 1520, 1216
            align 0.5, 0.5
            style_prefix "slot"
            spacing 20

        vbox spacing 10:
            $ thumbnail = BackgroundSystem.get_default_nz_background_thumbnail(findee)
            imagebutton:
                idle thumbnail
                hover thumbnail
                selected_idle thumbnail
                selected_hover thumbnail
                action Function(BackgroundSystem.set_nz_background, nz=findee, bg=None)
            text "恢复默认" align 0.5, 0.5

        for bg in BackgroundSystem.get_nz_backgrounds(findee):
            vbox spacing 10:
                if bg.is_unlocked:
                    imagebutton:
                        idle bg.thumbnail
                        hover bg.thumbnail
                        selected_idle bg.thumbnail
                        selected_hover bg.thumbnail
                        action Function(BackgroundSystem.set_nz_background, nz=findee, bg=bg)
                elif bg.password:
                    imagebutton:
                        idle bg.mosaic_thumbnail
                        hover bg.mosaic_thumbnail
                        selected_idle bg.mosaic_thumbnail
                        selected_hover bg.mosaic_thumbnail
                        action ShowTransient("bg_unlocker", bg=bg)
                else:
                    imagebutton:
                        idle bg.darkins_thumbnail
                        hover bg.darkins_thumbnail
                        selected_idle bg.darkins_thumbnail
                        selected_hover bg.darkins_thumbnail
                        action Function(BackgroundSystem.set_nz_background, nz=findee, bg=bg)
                for name in bg.dname:
                    text name align 0.5, 0.5

style bg_unlocker:
    align (0.5, 0.5)
    xsize 400

style bg_unlocker:
    variant "phone"
    align (0.5, 0.1)
    xsize 400

screen bg_unlocker(bg):
    default password = ""
    style_prefix "bg_unlocker"
    zorder 101

    frame:
        align 0.5, 0.5
        xsize 400

        has vbox:
            align 0.5, 0.5
        text "输入密码解锁:"

        input:
            style "name_input_input"
            pixel_width 320
            copypaste True
            value ScreenVariableInputValue("password", default=True, returnable=False)

        hbox:
            align 0.5, 0.5
            button:
                style "name_input_button"
                text _("确定") style "name_input_button_text"
                action Function(bg.unlock_by_password, password=password)
            button:
                style "name_input_button"
                text _("取消") style "name_input_button_text"

                action Return()

        textbutton "想知道密码吗？ ":
            action OpenURL('https://www.patreon.com/posts/43901371')
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
