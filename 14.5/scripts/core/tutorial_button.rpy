define guide_text = '''此汉化由@夜尽天明，@御坂，@琰SAMA，@那年雪落制作，仅供交流学习使用.
如果你是在其他地方付费购买了这个游戏的话，那么恭喜你，你交了智商税.
---------------------------------------------------------------
你不需要攻略来玩这个游戏.

这个游戏中的所有情节和事件都可以很容易地被触发.我们不想添加任何谜题，或复杂的触发条件，可能会让你感到厌烦.

推进故事的最重要方式是提高女孩的好感度.你可以通过两种方式实现这一目标.

1.在特定地点与女孩们见面.例如，平日里可以在教室里找到森宁.你可以点击大学面板上的 "去教室"按钮，在那里见到她，然后她的好感度就会提高.

2.触发女生的短期事件，这些事件会自动在地图上显示出女生的迷你头像的徽章.这些事件只会在序幕之后出现.

每当有一个新的可触发的情节和事件，它将在地图上显示一个徽章（红色/橙色/迷你头像）.
---------------------------------------------------------------
如果你被困在一个无法继续游戏的地方，可以使用右键菜单中的逃生按钮，回到主菜单上.(或按E键打开逃生菜单).'''

screen guide():
    zorder 91

    button:
        action Hide("guide", transition=Dissolve(0.3))

    frame:
        if renpy.variant("small"):
            xfill True yfill True
        else:
            xsize 1200 ysize 900

        xalign .5 yalign .5
        background Solid("#000000e6")
        padding (gui.frame_padding-11, gui.frame_padding-11)

        if not renpy.variant("small"):
            add xbtn(action=Hide("guide", transition=Dissolve(0.3)), xpos=1211, ypos=-9)

        vbox:
            xalign .5 yalign .5
            spacing 10

            if renpy.variant("small"):
                xsize 1600 ysize 900

            else:
                xsize 1000 ysize 670 yoffset 20

            text "{size=+10}{color=#e8888a}前言{/color}{/size}"

            text guide_text:
                size 27
                if renpy.variant("small"):
                    size 32
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
