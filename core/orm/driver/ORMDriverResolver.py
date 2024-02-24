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

        if driver not in ORMDriverResolver.drivers.keys(): KernelException(
            "InvalidORMDriver",
            f"Provided driver '{driver}' is not supported, please use one of {ORMDriverResolver.drivers.keys()}"
        )

        configuration: KeySet = ORMDriverResolver.drivers.get(driver)
        if not driver_configuration.has_keys(configuration.get("keys")): KernelException(
            "MissingORMConfiguration",
            f"Missing required configuration for driver '{driver}', please provide " +
            str(driver_configuration.missing_keys(configuration.get("keys")))
        )

        driver = configuration.get("class")
        driver_class = KernelModuleResolver.resolve_class(
            driver.get("namespace"), driver.get("class")
        )

        return driver_class(driver_configuration)
