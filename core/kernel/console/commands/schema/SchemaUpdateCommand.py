import sys

from core.kernel.console.base.BaseCommand import BaseCommand


class SchemaUpdateCommand(BaseCommand):

    def invoke(self):

        sys.argv.append("--force")

        self.kernel.invoke("cache:clear")
        print("")
        self.kernel.invoke("database:recreate")
        print("")
        self.kernel.invoke("entity:generate")
        print("")
        self.kernel.invoke("database:seed")
        print("")
        self.console.success("Schema updated successfully, database and entities are now up-to-date!")
