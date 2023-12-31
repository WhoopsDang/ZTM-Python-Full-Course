import requests
import hashlib
import sys


def request_api_data(query_char):
    url = "https://api.pwnedpasswords.com/range/" + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f"Error fetching: {res.status_code}")
    return res


def get_leak_count(hashes, hash_to_check):
    hashes = (line.split(":") for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


def pwned_api_check(password):
    # Check password if it exists in api response
    sha1pass = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    first5_char, tail = sha1pass[:5], sha1pass[5:]
    response = request_api_data(first5_char)
    return get_leak_count(response, tail)


def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(
                f"The {password} was found {count} times .... maybe you should swap off"
            )
        else:
            print(f"{password} was not found, nice!")
    return "done!"


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
