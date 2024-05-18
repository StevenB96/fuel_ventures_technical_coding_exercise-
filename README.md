# Technical coding excercise 1 - SNOMED Codes
## Overview
For this task you'll need to write an API that can retrieve, search, and add to the SNOMED codes provided in *snomed_codes.json*.

This exercise should be done in Python (Flask). There is skeleton code provided.

### SNOMED code definition
A SNOMED code is comprised of 3 attributes: 
1. *description id* - a long number **uniquely** identifying a SNOMED code.
2. *description* - some text describing the SNOMED code. 
3. *concept id* - a long number representing a concept the SNOMED code belongs to. These are not unique to a SNOMED code (i.e. multiple SNOMED codes can have the same *concept id*).

## SNOMED code data
Along with this document you should have received a JSON file *snomed_codes.json*. This contains some example SNOMED codes in the following format:
```
{
	<description id>: {
		"concept_id": <concept_id>,
		"description": <description>
	}
	…
	<description id>: {
		"concept_id": <concept_id>,
		"description": <description>
	}
}
```

## API details

Complete the functionality for the following API functions (skeleton code for these apis are in src/api.py):
1. GET /api/snomed_code/<description_id:int>
	* Should raise an exception for the case where there is no matching snomed code.
	* Return the SNOMED code from *snomed_codes.json* with the matching description_id.
2. GET /api/snomed_code/search
	* Query parameters:
		* n - the minimum number of words from the search string that need to be included in the 
        SNOMED codes description for it to be considered a match.
    	* search_string - the search string
	* You can consider "words" as any text that is seperated by a space.
    * Return all the SNOMED codes where the "description" includes at least N of the words in the search string.
3. POST /api/snomed_code
	* JSON data:
		* concept_id: string
		* description_id: string
		* description: string
	* Adds to *snomed_codes.json*
	* Must ensure "description_id" is unique in *snomed_codes.json*.
	* Return SNOMED code added

## Skeleton code (recommended but optional to use)
* src/
	* app.py
		* Code for creating and setting up the flask app.
	* run.py
		* Code for running the flask app. This is our entrypoint to run the flask app.
	* api.py
		* Includes the API routes needed for this task - note the logic of these API functions are not complete.
	* core.py
		* Includes any core logic (used by the API routes)
	* schema.py
		* Includes any (marshmallow) schemas used.

## Requirements
This code was written in python 3.9.16. The requirements can be found in *requirements.txt* (the exact requirements used to develop the skeleton code can be found in *frozen_requirements.txt*).

To install these requirements you must have a working version of python (preferably 3.9) and run `pip install -r requirements.txt`.

Feel free to add any requirements needed to run you solution to *requirements.txt*.


## Running
To run the flask app run `python src/run.py`.

## Developing
There is no requirement to write any tests as part of this task. Included are some example curl commands (curl_examples.md) that can be updated to check your code.

## Sending back to us
Please zip up this folder and respond via email.

*Make sure you don't include any python virtual environments or any large and unnecessary folders.*


## Helpful code snippets
./venv/Scripts/activate.ps1
python ./src/run.py