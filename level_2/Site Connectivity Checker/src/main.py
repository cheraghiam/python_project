import requests


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
def site_checker_availibility(url: str) -> bool:
    try:
        response = requests.get(url=url, headers=headers).status_code
        if response == 200:
            return True
        return False
    except Exception as e:
        print(e)
        return False
    
site_list = [
    "https://soroushplus.com/",
    "https://github.com/",
    "https://faradars.org/",
    "https://lms.shahroodut.ac.ir/Guest/",
    "https://lms.shahroodut.ac.ir/Guest/kljsdlfkjs"
]

if __name__ == "__main__":
    assert site_checker_availibility(url=site_list[0]) == True
    assert site_checker_availibility(url=site_list[3]) == True
    assert site_checker_availibility(url=site_list[4]) == False
    url_input = input("Enter the URL: ")
    print(site_checker_availibility(url=url_input))