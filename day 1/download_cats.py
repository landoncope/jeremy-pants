#!/usr/bin/env python3
import requests
import os
from datetime import datetime

def download_cat_images(num_images=10):
    # Create directory for cat images
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    dir_name = f"cat_images_{timestamp}"
    os.makedirs(dir_name, exist_ok=True)
    
    print(f"Downloading {num_images} cat images to {dir_name}/...")
    
    for i in range(1, num_images + 1):
        try:
            # Using The Cat API (free tier, no key required for basic usage)
            response = requests.get('https://api.thecatapi.com/v1/images/search')
            
            if response.status_code == 200:
                data = response.json()
                if data and len(data) > 0:
                    image_url = data[0]['url']
                    
                    # Download the image
                    img_response = requests.get(image_url)
                    if img_response.status_code == 200:
                        # Get file extension from URL
                        extension = image_url.split('.')[-1].split('?')[0]
                        if extension not in ['jpg', 'jpeg', 'png', 'gif']:
                            extension = 'jpg'
                        
                        filename = f"{dir_name}/cat_{i:02d}.{extension}"
                        
                        with open(filename, 'wb') as f:
                            f.write(img_response.content)
                        
                        print(f"✓ Downloaded cat {i}/{num_images}: {filename}")
                    else:
                        print(f"✗ Failed to download image {i}")
                else:
                    print(f"✗ No image data for cat {i}")
            else:
                print(f"✗ API request failed for cat {i}")
                
        except Exception as e:
            print(f"✗ Error downloading cat {i}: {str(e)}")
    
    print(f"\nDone! Cat images saved in {dir_name}/")
    return dir_name

if __name__ == "__main__":
    download_cat_images(10)