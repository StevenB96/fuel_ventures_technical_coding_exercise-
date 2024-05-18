from flask import Blueprint, request

import core
from schema import SnomedCodeSchema


api = Blueprint('api', __name__, url_prefix='/api')

@api.after_request
def make_json_output(response):
    """ All our api's will return json. """
    response.mimetype = 'application/json'
    return response


@api.route("/snomed_code/<description_id>", methods=['GET'])
def get_snomed_code(description_id: str):
    """
    Returns the SNOMED code with a matching description_id
    """
    # Example function returning a snomed_code (dict) from a description_id. Replace this with you own function.
    snomed_code = core.get_snomed_code_dummy(description_id)
    # Example using a marshamllow schema to serialise snomed_code to json string
    return SnomedCodeSchema().dumps(snomed_code)


@api.route("/snomed_code", methods=['POST'])
def add_snomed_code():
    """
    Should return all the SNOMED codes where the description includes 
    all the words in the search string.
    JSON data:
    concept_id: string
    description_id: string
    description: string
    """
    # Example of getting the requests json data and deserialising using a marshamllow schema.
    snomed_code = SnomedCodeSchema().load(request.get_json())
    # TODO 1: Add snomed code to snomed_codes.json
    return snomed_code


@api.route("/snomed_code/search", methods=['GET'])
def search_snomed_code():
    """
    Should return all the SNOMED codes where the description includes at least
    n words in the search string.

    Query parameters:
    n - the minimum number of words from the search string that need to be included in the 
        SNOMED codes description for it to be considered a match.
    search_string - the search string
    """
    # TODO 1. Read in query parameters form request
    # TODO 2. Search logic
    # TODO 3. Return SNOMED codes
