class User(object):
    def __init__(self, name):
        self.name = name

    def work(self, cheat=False, done=False):
        msg = "[{}] : {}"
        if cheat:
            print(msg.format(self.name, "Great"))
            return True
        if done:
            print(msg.format(self.name, "OK"))
        else:
            print(msg.format(self.name, "NG"))
        return done


class Me(object):
    def __init__(self, name):
        #super(Me, self).__init__(name)
        self.name = name

    def work(self, cheat=False, done=False):
        #return super().work(cheat=True, done=False)
        user = User(self.name)
        return user.work(cheat=True, done=False)
