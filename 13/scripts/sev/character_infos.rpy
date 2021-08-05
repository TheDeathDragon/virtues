default t = Time(total_period=1)

define P_study = Progress("study", "学习", "B_love_meter", base=6.0, nz="森柠")
define P_work = Progress("work", "工作", "C_love_meter", base=6.0, nz="狄奥多拉")

define P_sport = Progress("sport", "运动", "F_love_meter", base=6.0, nz="瑞秋")

define P = Player("P", state="P_state", color=color.cream)

default P_state = PlayerState(cash=500000.0)

define A_love = TrueLove("A_love_meter", max_value=60)
define B_love = TrueLove("B_love_meter", max_value=60)
define C_love = TrueLove("C_love_meter", max_value=70)
define D_love = TrueLove("D_love_meter", max_value=60)
define E_love = TrueLove("E_love_meter", max_value=60)
define F_love = TrueLove("F_love_meter", max_value=40)
define G_love = TrueLove("G_love_meter", max_value=60)

define A_lust = Lust("A_lust_meter", max_value=30)
define B_lust = Lust("B_lust_meter", max_value=30)
define C_lust = Lust("C_lust_meter", max_value=30)
define D_lust = Lust("D_lust_meter", max_value=30)
define E_lust = Lust("E_lust_meter", max_value=30)
define F_lust = Lust("F_lust_meter", max_value=30)
define G_lust = Lust("G_lust_meter", max_value=30)

define A_harem = Harem("A_harem_meter", max_value=25)
define B_harem = Harem("B_harem_meter", max_value=15)
define C_harem = Harem("C_harem_meter", max_value=25)
define D_harem = Harem("D_harem_meter", max_value=20)
define E_harem = Harem("E_harem_meter", max_value=20)
define F_harem = Harem("F_harem_meter", max_value=10)
define G_harem = Harem("G_harem_meter", max_value=25)

define color.A = "#d29881"
define color.B = "#aaaaaa"
define color.C = "#9dc8ca"
define color.D = "#a4d5a9"
define color.E = "#efe2a6"
define color.F = "#0b654f"
define color.G = "#ffbfbf"

define A = Nz("A", "薇拉", 22,
    color="#d29881",
    intro='''一个贫穷的年轻农村女孩独自来到这个城市,梦想过上更好的生活.由于缺乏高等教育,她现在只能做一些低薪的低贱工作.
她非常努力,无论这个社会有多糟糕,她都用一颗热情的心拥抱它.
我在一个喝醉的晚上夺走了她的第一次.''',
    like=["烹饪", "看足球比赛",  "咖喱鸡"],
    hint=A_hint,
    zone=["脚", "嘴巴",  "小穴"]
)

define B = Nz("B", "森柠", 21,
    color="#aaaaaa",
    intro='''她是我大学时最好的朋友,也是一个中国亿万富翁的独生女.
她在学术研究方面很有天赋.她过去两年的平均成绩保持在3.8分.
因为她的善良,她在学校很受欢迎.但和陌生人说话时,她有点内向. ''',
    like=["在图书馆学习", "股票投资", "绿茶"],
    zone=["未知"],
    hint=B_hint
)

define C = Nz("C", "狄奥多拉", 23,
    color="#9dc8ca",
    intro='''作为一位著名企业家的大女儿,她现在是她母亲的一家公司的经理.
我们是按父母的意愿订婚的,但我们之间还没有真正的爱情.事实上,我们并不能融洽相处,就像磁铁的两极一样.
我不喜欢她冷酷而又坚强的个性.''',
    like=["高空跳伞", "安静的地方", "豪华跑车"],
    zone=["乳头"],
    hint=C_hint
)
define D = Nz("D", "艾琳", 18,
    color="#a4d5a9",
    intro='''她是狄奥多拉的妹妹.
虽然她很年轻,但她完全知道如何利用自己的魅力从男孩那里获得优势.
她看起来很天真,但那可能不是她的真实面孔.
我们一起长大,一直保持着亲密的关系直到现在.她把我当作她的亲兄弟.''',
    like=["手绘", "短裙", "角色扮演"],
    zone=["后庭"],
    hint=D_hint
)
define E = Nz("E", "伊莉莎", 40,
    color="#efe2a6",
    intro='''著名企业家,狄奥多拉和艾琳的母亲,目前单身.
她和我爸爸是好朋友,她把我当作自己的儿子来照顾.
她现在和她的小女儿住在她的大宅子里.有时她会感到孤独.''',
    like=["肥皂剧", "规划", "身体SPA"],
    zone=["胸部"],
    hint=E_hint
)
define F = Nz("F", "瑞秋", 20,
    color="#0b654f",
    intro='''大学田径队的一员,是我一生中遇到的最强壮的女孩.
她没有意识到自己的美丽,对自己的脸有点不自信.''',
    like=["锻炼", "空手道", "马拉松"],
    zone=["未知"],
    hint=F_hint
)
define G = Nz("G", "乌诺", 19,
    color="#ffbfbf",
    intro=G_intro,
    like=["角色扮演", "日本漫画", "短视频拍摄"],
    zone=["乳头", "胸部", "脖子"],
    hint=G_hint
)

init -1 python:

    def G_intro():
        intro = '''一个著名的coser,艾琳的朋友.
我还不太了解她.'''
        if seen("G_MoveIn"):
            intro = '''一个著名的coser,一个业余的福利姬,一个书店店员.这个女孩充满神秘感.
不知为什么,她对自己的胸部并不自信——她认为自己的胸部太大了.
她话不多,但有能力在短时间内与陌生人很好的相处. '''
        return intro

    def A_clothes():
        clothes = ["默认"]
        return clothes

    def B_clothes():
        clothes = ["默认"]
        if seen("B_date_1"):
            clothes.append("黄色衬衫")
        if B.relation != "general":
            clothes.append("男衬衫")
        return clothes

    def C_clothes():
        clothes = ["默认"]
        return clothes

    def D_clothes():
        clothes = ["默认"]
        if seen("pcsj"):
            clothes.append("校服")
        if seen("D_love_6"):
            clothes.append("猫女孩服装")
        return clothes

    def E_clothes():
        clothes = ["默认"]
        if seen("CDE_Picnic"):
            clothes.append("打结衬衫")
        return clothes

    def F_clothes():
        clothes = ["默认"]
        return clothes

    def G_clothes():
        clothes = ["默认"]
        clothes.append("默认(Coser)")
        return clothes

    def A_hint():
        hint = "试着去她的工作场所和她聊聊,和她好好相处."
        if seen("A_love_2") and not seen("pcsj"):
            hint = "我最近已经找到薇拉太多次了,也许我应该花点时间在森柠身上."
        return hint

    def B_hint():
        hint = "还没有."
        if seen("d6_1"):
            hint = "试着在商业街给她买一件礼物,然后在她的好感达到5点后的下午再去找她."
        if seen("B_love_1"):
            hint = "她欣赏那些热爱学习的人.你应该去学校学习,努力给她留下好印象."
        if seen("B_love_2"):
            hint = "最近我找森柠太多次了,也许我应该花点时间在薇拉身上."
        if seen("pcsj"):
            hint = "她欣赏那些热爱学习的人.你应该去学校学习,努力给她留下好印象."
        return hint

    def C_hint():
        hint = "还没有."
        if seen("pcsj"):
            hint = "她欣赏那些努力工作的人.你应该经常去上班,试着给她留下好印象."
        return hint

    def D_hint():
        hint = "试着给她买个礼物,然后下午去她家拜访她."
        if seen("D_dqsj"):
            hint = "还没有."
        if seen("pcsj"):
            hint = "你可以每天下午或晚上辅导她."
        return hint

    def E_hint():
        hint = "还没有."
        if seen("pcsj"):
            hint = "她给了你两份工作,一份在她的公司工作,另一份辅导她的小女儿.你需要向她证明你能做好那些工作."
        return hint

    def F_hint():
        hint = "她欣赏身体强壮的人.你应该多去公园锻炼,给她留下好印象."
        return hint

    def G_hint():
        hint="还没有."
        if seen("G_MoveIn"):
            hint = "她下午在书店工作,平时你总能在那里找到她."
        return hint


default A_love_meter = Meter("A_love")
default B_love_meter = Meter("B_love")
default C_love_meter = Meter("C_love")
default D_love_meter = Meter("D_love")
default E_love_meter = Meter("E_love")
default F_love_meter = Meter("F_love")
default G_love_meter = Meter("G_love")

default A_lust_meter = Meter("A_lust")
default B_lust_meter = Meter("B_lust")
default C_lust_meter = Meter("C_lust")
default D_lust_meter = Meter("D_lust")
default E_lust_meter = Meter("E_lust")
default F_lust_meter = Meter("F_lust")
default G_lust_meter = Meter("G_lust")

default A_harem_meter = Meter("A_harem")
default B_harem_meter = Meter("B_harem")
default C_harem_meter = Meter("C_harem")
default D_harem_meter = Meter("D_harem")
default E_harem_meter = Meter("E_harem")
default F_harem_meter = Meter("F_harem")
default G_harem_meter = Meter("G_harem")

default A_state = NzState()
default B_state = NzState()
default C_state = NzState()
default D_state = NzState()
default E_state = NzState()
default F_state = NzState()
default G_state = NzState()


define a = Character("[A]", who_color=A.color)
define b = Character("[B]", who_color=B.color)
define c = Character("[C]", who_color=C.color)
define c_qm = Character("[C]?", who_color=C.color)
define d = Character("[D]", who_color=D.color)
define e = Character("[E]", who_color=E.color)
define f = Character("[F]", who_color=F.color)
define g = Character("[G]", who_color=G.color)
define narrator = Character(None, what_color=gui.dialogue_color)
define player = Character("[P.name]", who_color=P.color)


define posia = Character("波西亚", who_color="#A657C4")
define minna = Character("明娜夫人", who_color="#6E0C1B")
define bubble_a = Character(None, screen="bubble", show_color=A.color)
define bubble_b = Character(None, screen="bubble", show_color=B.color)
define bubble_c = Character(None, screen="bubble", show_color=C.color)
define bubble_d = Character(None, screen="bubble", show_color=D.color)
define bubble_e = Character(None, screen="bubble", show_color=E.color)
define bubble_f = Character(None, screen="bubble", show_color=F.color)
define bubble_g = Character(None, screen="bubble", show_color=G.color)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
