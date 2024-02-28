from core.kernel.console.base.BaseCommand import BaseCommand


class ArchitekCommand(BaseCommand):

    def invoke(self):

        name = self.configuration.get("kernel.framework", "name")
        version = self.configuration.get("kernel.framework", "version")
        repository_url = self.configuration.get("kernel.framework", "repository_url")

        self.stdout(f"∑7━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[ ∑9{name} ∑7]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        self.stdout("")
        self.stdout(f"∑9{name} Framework ∑7- v∑9{version} ")
        self.stdout("")
        self.stdout("∑9Fully featured ∑7python framework")
        self.stdout("∑9Build production-ready ∑7apps with low efforts !")
        self.stdout("")
        self.stdout(f"∑7→ Support the project at ∑9{repository_url}")
        self.stdout("")
        self.stdout(f"∑7━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{ '━' * len(name)}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
