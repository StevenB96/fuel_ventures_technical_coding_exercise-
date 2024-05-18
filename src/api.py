from flask import Blueprint, request, jsonify
import core
from schema import SnomedCodeSchema, SearchInputSchema


api = Blueprint("api", __name__, url_prefix="/api")


@api.route("/")
def index():
    return jsonify({"message": "Hello World."})


@api.after_request
def make_json_output(response):
    """All our api's will return json."""
    response.mimetype = "application/json"
    return response


@api.route("/snomed_code/<description_id>", methods=["GET"])
def get_snomed_code(description_id: str):
    """
    Returns the SNOMED code with a matching description_id
    """

    try:
        snomed_code_records = core.search_snomed_code_records(
            {
                "description_id": [str(description_id)],
            },
            1,
        )

        if snomed_code_records and len(snomed_code_records) == 1:
            return snomed_code_records[0]

        return []
    except Exception as e:
        return f"Error: {e}"


@api.route("/snomed_code", methods=["POST"])
def add_snomed_code():
    """
    Should return all the SNOMED codes where the description includes
    all the words in the search string.
    JSON data:
    concept_id: string
    description_id: string
    description: string
    """

    snomed_code = SnomedCodeSchema().load(request.get_json())

    if False == snomed_code["description_id"].isdigit():
        return "Error: Description ID must be a number."
    
    if False == snomed_code["concept_id"].isdigit():
        return "Error: Concept ID must be a number."

    created = core.post_snomed_code(snomed_code)

    return "Created SnomedCode!" if created == True else "Failed to create SnomedCode."


@api.route("/snomed_code/search", methods=["GET"])
def search_snomed_code():
    """
    Should return all the SNOMED codes where the description includes at least
    n words in the search string.

    Query parameters:
    n - the minimum number of words from the search string that need to be included in the
        SNOMED codes description for it to be considered a match.
    search_string - the search string
    """

    try:
        # Validate and deserialize the incoming request args
        search_input_data = SearchInputSchema().load(request.args)

        # Access the validated data
        search_string_q_param = search_input_data.get("search_string", "")
        n_q_param = search_input_data.get("n", 0)

        snomed_code_records = core.search_snomed_code_records(
            {
                "description": search_string_q_param.split(","),
            },
            n_q_param,
        )

        return snomed_code_records
    except Exception as e:
        return f"Error: {e}"
