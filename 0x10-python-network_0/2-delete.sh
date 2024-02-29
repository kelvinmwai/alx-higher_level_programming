#!/bin/bash
# DELETE request to the URL passed as the first argument then display the body of the response
curl -sX DELETE "$1"
