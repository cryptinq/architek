from core.Kernel import Kernel
from core.kernel.console.base.BaseCommand import BaseCommand


class ArchitekCommand(BaseCommand):

    def __init__(self, kernel: Kernel):
        super().__init__(kernel)

    def invoke(self):

        name = self.configuration.get("kernel.framework", "name")
        version = self.configuration.get("kernel.framework", "version")
        repository_url = self.configuration.get("kernel.framework", "repository_url")

        self.stdout(f"∑7━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[ ∑a{name} ∑7]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        self.stdout("")
        self.stdout(f"∑a{name} Framework ∑7- v∑a{version} ")
        self.stdout("")
        self.stdout("∑aFully featured ∑7python framework")
        self.stdout("∑aBuild production-ready ∑7apps with low efforts !")
        self.stdout("")
        self.stdout(f"∑7→ Support the project at ∑a{repository_url}")
        self.stdout("")
        self.stdout(f"∑7━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{ '━' * len(name)}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
