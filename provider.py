class Provider:
    class storage:
        def cp(self, args):
            raise NotImplementedError()
        def rm(self, args):
            raise NotImplementedError()
