from time import time
from typing import Optional

from core.kernel.console.base.BaseCommand import BaseCommand
from core.orm.ORM import ORM
from core.orm.factory.FactoryManager import FactoryManager
from core.kernel.factory.BaseSeeder import BaseSeeder
from core.exceptions.KernelException import KernelException


class DatabaseSeedCommand(BaseCommand):

    def __init__(self):
        super().__init__()

        self.orm: ORM = self.kernel.app("orm")
        self.schemas: Optional[dict] = None

        self.factory: FactoryManager = self.orm.factory_manager()
        self.seeders: list[BaseSeeder] = self.kernel.resolve_modules("database.seeder")

    def invoke(self):

        start_time = time()

        if len(self.seeders) == 0:
            self.console.info(
                f"No database seeders detected, create one using 'python console make:seeder ExampleSeeder'"
            )
            exit(0)

        error_count = 0

        for seeder in self.seeders:

            seeder_instance = seeder()

            self.console.info(
                f"Running seeder for entity '{seeder_instance.entity.schema().name}' from '{seeder_instance.path}'"
            )

            success = False
            try: success = seeder_instance.run()
            except Exception as e: KernelException(
                "SeederRuntimeException",
                f"An error occurred while trying to run {seeder_instance.name} - {str(e)}",
                True
            )

            if not success: error_count += 1
            # if success and self.kernel.verbose(1): self.console.success(
            #     f"Seeder '{seeder_instance.name}' ran successfully"
            # )

        print("")

        if error_count == 0: self.console.success(f"Database seeded successfully in {((time() - start_time) * 1000):.2f}ms")
        else: self.console.error(f"Database seeded with {error_count} errors, please fix them"); exit(1)

