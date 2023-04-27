import requests, json
import logging

session = requests.Session()


def get_ip():
    return requests.get('https://checkip.amazonaws.com').text.strip()


def update_ips(urls, email, api_key, zone_id):
    session.headers.update({"X-Auth-Email": email, "X-Auth-Key": api_key})
    for url in urls:
        r = session.get(
            f"https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records?type=A&name={url}"
        )
        print(r.text)
        record_id = json.loads(r.text)['result'][0]['id']
        config = json.dumps({
            "type": "A",
            "name": url,
            "content": get_ip(),
            "proxied": False
        })
        r = session.put(
            f"https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records/{record_id}",
            config)
        logging.info(f"Ip: {get_ip()}")
        logging.debug(f"API Response: {r.text}")
