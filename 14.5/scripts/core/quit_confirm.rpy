style link:
    color "#0088ff"
    hover_color gui.main_accent_color

layeredimage qcb:
    always Solid(color.cream+"33", xysize=(660, 280), align=(.5, .5))
    always Solid(color.blackish, xysize=(658, 278), align=(.5, .5))

screen quit_confirm():
    style_prefix "confirm"



    frame at normal_t(0.2):
        xfill True yfill True
        background Solid(color.blackish)
        fixed:
            align .5, .3
            xysize 400, 300
            add "gui/play_cute.png":
                zoom 0.5
                xalign .5
                yoffset -200
                xoffset -34

        frame:
            align .5, .65
            xysize 660, 280
            add "qcb"
            vbox:
                align .5, .5
                label "你确定要退出吗?":
                    style "confirm_prompt"
                    xalign 0.5
                null height 90
                hbox:
                    xalign 0.5
                    spacing 300

                    textbutton _("Yes") action Hide("confirm"), Quit(confirm=False)
                    textbutton _("No") action Hide("confirm")
        vbox:
            align .5, .95
            add Solid("#e6e6e6", xsize=860, ysize=1, xalign=0.5)
            text "想知道解锁密码吗，加群了解更多吧～"
            button:
                text "{u}点击加群{/u}" style "link"
                action OpenURL("https://jq.qq.com/?_wv=1027&k=9MsL1MC7")


    key "game_menu" action Return(False)


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
