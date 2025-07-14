import requests
def check_headers(URL):
    headers_check = {
    "Content-Security-Policy": "Prevents XSS by controlling allowed sources",
        "X-Content-Type-Options": "Prevents MIME-sniffing",
        "X-Frame-Options": "Blocks clickjacking by preventing iframes",
        "Strict-Transport-Security": "Forces HTTPS over HTTP",
        "Referrer-Policy": "Limits information sent in Referer header",
        "Permissions-Policy": "Restricts browser feature usage",
        "Cache-Control": "Stops sensitive data from being cached"
        }
    try:
        response = requests.get(URL, timeout=5)
        print(f"scanning security header: {URL}\n")
        for header, reason in headers_check.items():
            if header in response.headers:
                print(f"{header} -> present")
            else:
                print(f"{header} -> missing")
                print(f"suggestion : {reason}")
    except requests.RequestException as e:
        print(f"error in {URL}: {e}")
if __name__ == "__main__":
        target = input("enter target url: ").strip()
        if not target.startswith("http"):
              target = "https://" + target
        check_headers(target)



        
    