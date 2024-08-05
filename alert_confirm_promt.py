alert = browser.switch_to.alert
alert_text = alert.text
alert.accept()

alert = browser.switch_to.alert
alert_text = alert.text
alert.accept()#.dissmis для отмены

prompt = browser.switch_to.alert
prompt.send_keys("My answer")
prompt.accept()
