import json
import os
import core
from schema import SnomedCodeSchema


def load_json_file():
    current_directory = os.path.dirname(__file__)
    file_path = os.path.join(current_directory, "../snomed_codes.json")
    with open(file_path, "r") as file:
        data = json.load(file)
    return data


def save_json_file(data):
    current_directory = os.path.dirname(__file__)
    file_path = os.path.join(current_directory, "../snomed_codes.json")
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)


def find_record_match(snomed_code_record, attribute_search_dict, n):
    try:
        # Loop over attribute search values to find matches.
        for attribute_search_value_index, (
            attribute_search_value_key,
            attribute_search_value_list,
        ) in enumerate(attribute_search_dict.items()):
            occurance_count = 0

            for attribute_search_value in attribute_search_value_list:
                # Match check.
                record_attribute_value = snomed_code_record[attribute_search_value_key]

                # String.
                if isinstance(record_attribute_value, (str)) and isinstance(
                    record_attribute_value, (str)
                ):
                    match_count = record_attribute_value.count(attribute_search_value)
                    if match_count > 0:
                        if n == None:
                            return True
                        else:
                            occurance_count += 1

                # Integer.
                if isinstance(record_attribute_value, (int, float)) and isinstance(
                    attribute_search_value, (int, float)
                ):
                    if (
                        abs(record_attribute_value - attribute_search_value)
                        < 0.00000001
                    ):
                        return True

                # Handle occurances condition.
                if n != None and occurance_count >= n:
                    return True
    except Exception as e:
        print(f"Error: {e}")
        return False


def search_snomed_code_records(attribute_search_dict: dict[str, list], n: int):
    try:
        return_records = []

        all_snomed_records = core.load_json_file()

        for snomed_record_index, (snomed_record_key, snomed_record_value) in enumerate(
            all_snomed_records.items()
        ):
            # Add Description Id attribute.
            snomed_code_record_copy = dict(snomed_record_value)
            snomed_code_record_copy["description_id"] = int(snomed_record_key)

            if (
                find_record_match(snomed_code_record_copy, attribute_search_dict, n)
                == True
            ):
                return_records.append(SnomedCodeSchema().dumps(snomed_code_record_copy))

        return return_records
    except Exception as e:
        print(f"Error: {e}")
        return False


def post_snomed_code(snomed_code):
    try:
        snomed_code_list = core.load_json_file()
        snomed_code_id_list = [
            int(key) for _, (key, _) in enumerate(snomed_code_list.items())
        ]

        if int(snomed_code["description_id"]) not in snomed_code_id_list:
            snomed_code_list[snomed_code["description_id"]] = {
                "concept_id": snomed_code["concept_id"],
                "description": snomed_code["description"],
            }
            core.save_json_file(snomed_code_list)
            return True

        return False
    except Exception as e:
        print(f"Error: {e}")
        return False
