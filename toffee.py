import requests
import json

def get_toffee_playlist():
    # Toffee Official API and Headers
    api_url = "https://toffeelive.com/api/v1/home-data-web?category=10"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
        "Referer": "https://toffeelive.com/",
        "Origin": "https://toffeelive.com",
        "Cookie": "Edge-Cache-Cookie=URLPrefix=aHR0cHM6Ly9ibGRjbXByb2QtY2RuLnRvZmZlZWxpdmUuY29tLw:Expires=1735655500:KeyName=toffee-edge-key:Signature=xxx" 
    }

    try:
        response = requests.get(api_url, headers=headers)
        data = response.json()
        
        with open("toffee.m3u", "w", encoding='utf-8') as f:
            f.write('#EXTM3U x-tvg-url="https://raw.githubusercontent.com/frizisdead/EPG/main/epg.xml"\n\n')
            
            # চ্যানেলের ডেটা লুপ করা
            for item in data['data']['categories'][0]['content']:
                name = item['title']
                stream_url = item['video_url']
                logo = item['poster_url']
                channel_id = item['id']
                
                # মোমিন স্টাইল ফরম্যাটিং
                f.write(f'#EXTINF:-1 tvg-id="{channel_id}" tvg-logo="{logo}" group-title="Toffee Live", {name}\n')
                f.write(f'{stream_url}|User-Agent={headers["User-Agent"]}&Referer={headers["Referer"]}\n\n')
        
        print("Momin style playlist updated!")
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    get_toffee_playlist()
