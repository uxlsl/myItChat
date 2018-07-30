import itchat


@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    return "你好，我是机器人，他现在没空看微信，请电话联系!"


itchat.auto_login(enableCmdQR=2)
itchat.run()
