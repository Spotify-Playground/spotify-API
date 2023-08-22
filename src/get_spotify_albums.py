def get_soundtrack(movie_id):
    # module import
    import requests, json

    # source file path
    main_path = "<movieDetails_폴더_절대경로>"
    file_name = f"TMDB_movieDetails_{movie_id}.json"
    file_path = f"{main_path}/{file_name}"

    # load source json
    data = json.load(file_path)
    search = data["original_title"]

    # requests
    access_token = "BQC1W9U5wu-ZLGJ4Ko0Y58kvpYe46i4NdXfeq5_kJNN1jnL16y2cZRYeMX4JXb-OOGWL2sqxNS_JC33NLYqKTVbBTwz8BO2E82FzyDviPSFEEVNs55g"
    headers = {
        'Authorization': f'Bearer {access_token}',
    }
    params = {
        'q' : search,
        'type': 'album',
        'limit' : "3"
    }
    response = requests.get('https://api.spotify.com/v1/search', params=params, headers=headers).json()

    # file save
    data_path = "<data_폴더_절대경로>"
    json_name = f"spotify_{movie_id}.json"
    json_path = f"{data_path}/{json_name}"
    with open(json_path, "w") as file:
        json.dump(response, file, indent=4, ensure_ascii=False)

# Test
if __name__ == "__main__":
    get_soundtrack(976573)