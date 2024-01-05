from core.exceptions.KernelException import KernelException
from core.kernel.file.helpers.KeySet import KeySet
from core.kernel.static.module.KernelModuleResolver import KernelModuleResolver


class ORMDriverResolver:

    drivers = KeySet({
        "sqlite": {
            "keys": ["path", "database"],
            "class": {
                "namespace": "core.orm.driver.drivers.SQLiteDriver",
                "class": "SQLiteDriver"
            }
        },
        "mysql": {
            "keys": ["host", "port", "database", "username", "password", "charset", "collation"],
            "class": {
                "namespace": "core.orm.driver.drivers.MySQLDriver",
                "class": "MySQLDriver"
            }
        }
    })

    @staticmethod
    def resolve(driver: str, driver_configuration: KeySet):

        if driver not in ORMDriverResolver.drivers.keys():
            raise KernelException("InvalidORMDriver", driver)

        configuration: KeySet = ORMDriverResolver.drivers.get(driver)
        if not driver_configuration.has_keys(configuration.get("keys")):
            raise KernelException("MissingORMConfiguration",
                driver_configuration.missing_keys(
                    configuration.get("keys")
                )
            )

        driver = configuration.get("class")
        driver_class = KernelModuleResolver.resolve_class(
            driver.get("namespace"), driver.get("class")
        )

        return driver_class(driver_configuration)
