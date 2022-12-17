import controllers

while True:
    controllers.greeting()
    if controllers.choos_action() is False:
        break
    else:
        controllers.choos_action()
    

# controllers.

