### GET /api/snomed_code/<description_id>
`curl http://localhost:5000/api/snomed_code/12345678`


### GET /api/snomed_code/search
`curl -G -d "n=3" -d "search_string=some%20search%20string" http://localhost:5000/api/snomed_code/search`


### POST /api/snomed_code
`curl -X POST -H "Content-Type: application/json" -d '{"concept_id":"12345", "description_id":"4321", "description":"abc def"}' http://localhost:5000/api/snomed_code`
