

file_path = '/synology/download/431d366742fa9c1c42eef197099b6b924ec8bf79.torrent'

file_path_str = file_path.split(".")

if file_path_str[-1] not in ["torrent"]:
    print(file_path_str[-1])