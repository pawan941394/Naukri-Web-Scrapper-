def headers_naukri(encoded_title,):
    head = {
        "authority": "www.naukri.com",
        "accept": "application/json",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "en-US,en;q=0.9",
        "appid": "109",
        "clientid": "d3skt0p",
        "content-type": "application/json",
        "gid": "LOCATION,INDUSTRY,EDUCATION,FAREA_ROLE",
        "nkparam": "NIYmGV6jRVjndSPiK3jXoPbxT+2jJGeNsOiXzzudeKbK1ntBbcyCukR0jWkQcrcpkmsKiGbQU6qrh87OWki3ow==",
        "priority": "u=1, i",
        "referer": f"https://www.naukri.com/{encoded_title.lower().replace(' ', '-')}-jobs?k={encoded_title}&nignbevent_src=jobsearchDeskGNB",
        "sec-ch-ua": '"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "systemid": "Naukri",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"
    }
    return head