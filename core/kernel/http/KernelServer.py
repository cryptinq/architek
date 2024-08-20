import logging
import time
from logging import FileHandler
from typing import Optional

import requests
from flask import Flask, g, request

from core.exceptions.KernelException import KernelException
from core.kernel.file.helpers.FileSystem import FileSystem as fs
from core.kernel.http.Router import Router
from core.kernel.utils.Worker import Worker
from waitress import serve


class KernelServer:

    error_codes = [
        400, 401, 403, 404, 405, 406, 408, 409,
        500, 501, 502, 503, 504, 505
    ]

    def __init__(self, kernel):
        self.kernel = kernel
        self.configuration = self.kernel.configuration.get("app.http")
        self.server: Optional[Flask] = None
        self.router: Optional[Router] = None

    def initialize_server(self) -> Flask:
        self.server = Flask(__name__)
        self.handle_http_logs()
        self.handle_server_errors()
        return self.server

    def register_routes(self):
        with self.server.app_context():
            self.router = Router(
                self.server,
                self.configuration.get("routes")
            )

    def start(self):

        host, port = self.configuration.get("server.host"), self.configuration.get("server.port")
        self.kernel.console.info(f'Starting WSGI Server @ {host}:{port}')

        Worker(serve).run(self.server, host=host, port=port)

        if self.check_status(10): self.kernel.console.success('∑a⦿  ∑fWSGI Server is running\n')
        else: KernelException('WSGIStartupException', 'WSGI Server failed to start')

    def check_status(self, timeout=10, delay=0.5):
        time.sleep(delay)
        try:
            response = requests.get(url="http://127.0.0.1:8888/_", timeout=timeout)
            return True
        except requests.ConnectionError:
            return False

    def handle_server_errors(self):
        for error_code in self.error_codes:
            self.server.register_error_handler(
                error_code,
                lambda e: (f'An error occured \n{str(e)}', e.code,)
            )

    def handle_http_logs(self):

        # Middleware for logging requests
        @self.server.before_request
        def before_request(): g.start_time = time.time()  # Record start time for the request

        @self.server.after_request
        def after_request(response):
            duration = time.time() - g.start_time
            if request.path == "/_": return response
            if self.kernel.verbose(0): self.kernel.console.system(
                f'{request.method} {request.path} - {response.status} - {duration:.2f}s'
            )
            return response

