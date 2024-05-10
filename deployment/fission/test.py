def search():

    response = requests.get(SEARCH_ENDPOINT, auth=auth, verify=False)
    if response.status_code == 200:
            return jsonify(response.json())
    else:
        return jsonify({'error': f'Failed to fetch data from Elasticsearch. Status code: {response.status_code}'}), response.status_code
