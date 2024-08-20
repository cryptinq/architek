from flask import Flask, request

from core.exceptions.KernelException import KernelException
from core.kernel.Base import Base
from core.kernel.file.helpers.KeySet import KeySet
from core.kernel.http.dataclasses.Route import Route
from core.kernel.static.module.KernelModuleResolver import KernelModuleResolver


class Router(Base):

    def __init__(self, server: Flask, routes: KeySet):
        super().__init__()
        self.server = server
        self.routes: KeySet = routes
        self.define_routes()

    def define_routes(self):

        for route_name in self.routes.keys():
            try:
                config: KeySet = self.routes.get(route_name)

                controller_instance = KernelModuleResolver.resolve_class(
                    config.get('controller'), config.get('controller').split(".")[-1]
                )()
                function = getattr(controller_instance, config.get('method'), None)

                route: Route = Route(
                    rule=config.get("path"), method=function,
                    endpoint=route_name, methods=config.get("http_methods")
                )

            except Exception as e: KernelException(
                "InvalidRouteDefinition",
                f"Route '{route_name}' defined in app/http.yaml in invalid, {str(e)}"
            )

            self.server.add_url_rule(
                rule=route.rule, view_func=route.method, endpoint=route.endpoint, methods=route.methods
            )

            if self.kernel.verbose(1): self.console.info(f"  | HTTP ∑f'{route.rule}' {route.methods} → {route.method}()")

        if self.kernel.verbose(1): self.console.info("")