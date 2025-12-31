import requests

def get_toffee():
    # Toffee links logic
    channels = [
        {"name": "Somoy TV", "url": "https://bldcmprod-cdn.toffeelive.com/cdn/live/somoy_tv/playlist.m3u8"},
        {"name": "Sony Sports 1", "url": "https://bldcmprod-cdn.toffeelive.com/cdn/live/sony_sports_1/playlist.m3u8"}
    ]
    
    with open("toffee.m3u", "w") as f:
        f.write("#EXTM3U\n")
        for ch in channels:
            # Simple simulation of token fetching
            f.write(f"#EXTINF:-1, {ch['name']}\n{ch['url']}\n")

if __name__ == "__main__":
    get_toffee()
