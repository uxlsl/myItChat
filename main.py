import itchat


@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    return "你好，我是机器人，他现在没空看微信，请电话联系!"


itchat.auto_login(enableCmdQR=2, hotReload=True) # 热关可以不用在一些时间不用扫码
itchat.run()
