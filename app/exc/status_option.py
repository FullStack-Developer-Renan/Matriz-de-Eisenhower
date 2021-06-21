from http import HTTPStatus

class StatusOptionsError(Exception):
    def __init__(self, data:dict) -> None:
        self.message = (
            {"error": {"valid_options": {"importance": [1, 2], "urgency": [1, 2]}, 
            "received_options": {"importance": data["importance"], "urgency": data["urgency"]}}},
            400
        )

        super().__init__(self.message)

