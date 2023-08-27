import pyshorteners

def shorten_url(url):
    s = pyshorteners.Shortener()
    short_url = s.tinyurl.short(url)
    return short_url

def main():
    print("URL Shortener")

    long_url = input("Enter the long URL: ")

    short_url = shorten_url(long_url)
    print(f"Short URL: {short_url}")

if __name__ == "__main__":
    main()
