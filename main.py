import requests
from PIL import Image
import os

# End page
end = 382

# Chemistry
base_url = 'https://www.pearsonactivelearn.com/r00/r0070/r007014/r00701433/current/OPS/images/9780435185169_Refinery_(1)-' # 382 pages
# Physics
#base_url = 'https://www.pearsonactivelearn.com/r00/r0070/r007007/r00700764/current/OPS/images/9780435185275_(1)-' # 325 pages
# ICT
#base_url = 'https://www.pearsonactivelearn.com/r00/r0073/r007337/r00733746/current/OPS/images/9780435188931-' # 360 pages
# English As Second
#base_url = 'https://www.pearsonactivelearn.com/r01/r0113/r011390/r01139006/current/OPS/images/9781292458458-' # 352 pages
# Economics
#base_url = 'https://www.pearsonactivelearn.com/r00/r0074/r007462/r00746286/current/OPS/images/9780435188641-' # 376 pages


os.makedirs('images', exist_ok=True)

image_files = []

for i in range(1, end + 1):
    num = f'{i:03}'
    url = f'{base_url}{num}.jpg'

    response = requests.get(url)
    if response.status_code == 200:
        image_path = f'images/image_{num}.jpg'
        with open(image_path, 'wb') as f:
            f.write(response.content)
        print(f'Downloaded: {url}')
        image_files.append(image_path)
    else:
        print(f'Failed to download: {url}')

if image_files:
    image_list = []

    for image_file in image_files:
        img = Image.open(image_file).convert('RGB')
        image_list.append(img)

    image_list[0].save('output.pdf', save_all=True, append_images=image_list[1:])
    print('PDF created: output.pdf')
