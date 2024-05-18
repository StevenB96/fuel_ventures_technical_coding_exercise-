from marshmallow import Schema, fields
import core

def find_record_match(snomed_code_record, attribute_search_dict, n):
    # Loop over attribute search values to find matches.
    for attribute_search_value_index, (attribute_search_value_key, attribute_search_value_list) in enumerate(attribute_search_dict.items()):
        occurance_count = 0

        for attribute_search_value in attribute_search_value_list:
            # Match check.
            try:
                record_attribute_value = snomed_code_record[attribute_search_value_key]

                # String.
                if (isinstance(record_attribute_value, (str)) and isinstance(record_attribute_value, (str))):
                    match_count = record_attribute_value.count(attribute_search_value)
                    if (match_count > 0):
                        if (n == None):
                            return True
                        else:
                            occurance_count += 1

                # Integer.
                if (isinstance(record_attribute_value, (int, float)) and isinstance(attribute_search_value, (int, float))):
                    if abs(record_attribute_value - attribute_search_value) < 0.00000001:
                        return True

                # Handle occurances condition.
                if (n != None and occurance_count >= n):
                    return True
            except Exception as e:
                print(f"Error: {e}")
                return False

    return False


class SnomedCodeSchema(Schema):
    concept_id = fields.String()
    description_id = fields.String()
    description = fields.String()

    @classmethod
    def search_snomed_code_records(
            self, 
            attribute_search_dict: dict[str, list], 
            n: int
        ):

        return_records = []

        all_snomed_records = core.load_json_file()

        for snomed_record_index, (snomed_record_key, snomed_record_value) in enumerate(all_snomed_records.items()):
            # Add Description Id attribute.
            snomed_code_record = snomed_record_value
            snomed_code_record['description_id'] = int(snomed_record_key)

            if (find_record_match(snomed_record_value, attribute_search_dict, n)):
                return_records.append(snomed_code_record)

        return return_records


class SearchInputSchema(Schema):
    n = fields.Integer()
    search_string = fields.String()