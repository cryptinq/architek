from common.entity.Project import Project


class App:

    def __init__(self, kernel=False):
        self.kernel = kernel

    def boot(self):
        project: Project = Project()