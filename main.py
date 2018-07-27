import itchat


@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    return "现在没空看微信，请电话联系!"


itchat.auto_login(enableCmdQR=2)
itchat.run()
