class GenderOptionsError(Exception):
    feild_options = ["female", "male", "genderless", "unknown"]

    def __init__(self, data: dict) -> None:
        self.message = (
            {
                "error": {
                    "gender_options": self.feild_options,
                    "recieved_option": data["importance"],
                }
            },
            400,
        )

        super().__init__(self.message)
