import uuid


class UUIDGenerator:

    @staticmethod
    def generate_uuid(): return str(uuid.uuid4())
