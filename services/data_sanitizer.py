from copy import deepcopy


SENSITIVE_FIELDS = {
    "customerEmail",
    "contactDetails",
    "mobile",
    "metaflexContactNumber",
    "gstin",
    "billToGstin",
    "shipToGstin",
    "billToPan",
    "shipToPan",
    "idValue",
    "accountNumber",
    "ifscCode",
    "swiftCode",
}


def sanitize_data(data: dict) -> dict:
    """
    Remove sensitive/unnecessary fields recursively while
    preserving the original JSON structure.
    """

    data = deepcopy(data)

    def clean(value):

        if isinstance(value, dict):

            cleaned = {}

            for key, item in value.items():

                if key in SENSITIVE_FIELDS:
                    continue

                cleaned[key] = clean(item)

            return cleaned

        if isinstance(value, list):
            return [clean(item) for item in value]

        return value

    return clean(data)