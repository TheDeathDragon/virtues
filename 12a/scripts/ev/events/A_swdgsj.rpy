label A_swdgsj:

    scene void with tstmgr

    narrator "据杰克说,薇拉每天早上在一家咖啡馆工作.也许我可以找个机会在那儿找到她.那将是改善我们关系的好办法."

    narrator "... ... ... ..."

    scene cafe_background with tstmgr

    narrator "早上,我去了那家咖啡馆."

    narrator "这个地方比我想象的要小,看起来又老又简陋.灯光是绝对的灾难.外面阳光明媚,但这个地方却黑暗无比.多么失败的设计!"

    narrator "幸运的是,薇拉真的在这里.要找到她一点也不困难,因为她是这里唯一的服务员."

    scene a_cafe_smile2 with tstmgr

    a "欢迎光临."

    scene a_cafe_weird with tstmgr

    a "Ah..."

    player "Oh?Hi,薇拉.我没想到会在这儿见到你."

    a "你好..."

    player "你在这儿工作吗?"

    narrator "... ... ... ..."

    narrator "她对我的出现有点吃惊.过了一段时间才恢复正常."

    scene a_cafe_normal1 with tstmgr

    a "Yes,我每天早上在这里工作,做服务员."

    scene a_cafe_weird with tstmgr

    a "你怎么在这?"

    player "我只是...走在街上,碰巧从外面看到你,所以我决定进来打个招呼.就是这样."

    a "... ... ... ..."

    scene a_cafe_normal1 with tstmgr

    a "好吧......要吃点什么?"

    player "你有什么推荐的吗?"

    scene a_cafe_weird with tstmgr

    a "Emm...我不知道."

    scene a_cafe_smile2 with tstmgr

    a "你可以尝尝培根三明治.培根是新鲜的,我敢肯定."

    player "听起来不错.那么我要一份培根三明治.谢谢你!."

    a "我马上回来."

    scene cafe_background with tstmgr

    narrator "... ... ... ..."

    narrator "过了一段时间,我吃完早餐结完账."

    scene a_cafe_normal1 with tstmgr

    a "你喜欢这顿饭吗?"

    player "... ... ... ..."

    narrator "(Well,不.培根烤过头了.尝起来像柴火.我不知道是否应该告诉她真相.)"

    a "... ... ... ..."

    scene a_cafe_weird with tstmgr

    a "没关系,你不用告诉我,我知道培根烤过头了.它尝起来一定像柴火."

    player "???你是怎么知道的?"

    a "... ... ... ..."

    a "实际上我很擅长烹饪.但厨师根本不听我的劝告."

    player "这是为什么?"

    a "他不听服务员的."

    player "Ha,现在我明白为什么这个地方客人这么少了."

    menu:
        "常规小费":

            scene cafe_background with tstmgr

            narrator "之后我们进行了简短的交谈.她话不多,但这是一个良好的开端."

            narrator "... ... ... ..."
        "超额小费":


            scene a_cafe_weird with tstmgr

            a "Eh,你为什么给我这么多小费?"

            player "因为我对你的服务很满意.就收下吧."

            a "但是百分之30...也太多了."

            player "人们总是付更多的小费给他们认识的服务员.这只是善意的表示,没有别的意思."

            scene a_cafe_smile2 with tstmgr

            a "真的是这样么..."

            a "... ... ... ..."

            scene a_cafe_smile2 with tstmgr

            a "好吧,谢谢你."

            scene cafe_background with tstmgr

            narrator "之后我们进行了简短的交谈.她话不多,但这是一个良好的开端."

            narrator "... ... ... ..."

            $ add(A, A.love, 1)

    jump event_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
