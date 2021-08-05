screen bonus_chapters():






    use game_menu(_("额外章节"))

    style_prefix "about" tag menu

    vbox:
        ypos 240 ysize 730
        xsize 1600 xalign 0.5
        spacing 8
        null height 20
        hbox:
            spacing 32

            hbox:
                spacing 16
                button:
                    add "bonus1_thumbnail"
                    action OpenURL('https://jq.qq.com/?_wv=1027&k=jKzi7gbm')
                text "{a=https://jq.qq.com/?_wv=1027&k=jKzi7gbm}Bonus Chapter 1{/a}" yalign 0.5
            hbox:
                spacing 16
                button:
                    add "bonus3_thumbnail"
                    action OpenURL('https://jq.qq.com/?_wv=1027&k=jKzi7gbm')
                text "{a=https://jq.qq.com/?_wv=1027&k=jKzi7gbm}Bonus Chapter 3{/a}" yalign 0.5

        hbox:
            spacing 16
            button:
                add "bonus2_thumbnail"
                action OpenURL('https://jq.qq.com/?_wv=1027&k=jKzi7gbm')
            text "{a=https://jq.qq.com/?_wv=1027&k=jKzi7gbm}Bonus Chapter 2{/a}" yalign 0.5
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
