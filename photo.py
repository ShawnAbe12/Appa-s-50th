


import json

file_list = ['436d4bdd-8325-43f2-9f48-85e06e02a629.JPG', '59cf602d-9cd7-4039-9f1a-8f351ef3e32f.jpg', '60d4bf15-471b-4614-8ff4-bdfaaf74472c.jpg', '73c945d9-0acf-41d1-9a23-83b8df19287e.jpg', '9d25dd93-082f-49b2-9157-dc36f6b61f67.JPG', 'a74faee8-0c12-4301-86a6-7e35653e76df.jpg', 'ab5eef8f-5682-44e1-9c18-9d7d08b123d4.jpg', 'images.json', 'IMG_0246.JPG', 'IMG_0247.JPG', 'IMG_0248.JPG', 'IMG_0597.JPG', 'IMG_0627.JPG', 'IMG_0790.JPG', 'IMG_0862.JPG', 'IMG_1225.JPG', 'IMG_1229.JPG', 'IMG_1252.JPG', 'IMG_1253.JPG', 'IMG_1276.JPG', 'IMG_1308.JPG', 'IMG_1323.JPG', 'IMG_1432.JPG', 'IMG_1433.JPG', 'IMG_1502.JPG', 'IMG_1548.JPG', 'IMG_2519.JPG', 'IMG_4592.JPG', 'IMG_4609.JPG', 'IMG_4610.JPG', 'IMG_6377.JPG', 'IMG_6551.JPG', 'PHOTO-2025-07-12-21-01-40.jpg', 'PHOTO-2025-07-12-21-01-41(1).jpg', 'PHOTO-2025-07-12-21-01-41(2).jpg', 'PHOTO-2025-07-12-21-01-41(3).jpg', 'PHOTO-2025-07-12-21-01-41(4).jpg', 'PHOTO-2025-07-12-21-01-41.jpg', 'PHOTO-2025-07-12-21-41-46.jpg', 'PHOTO-2025-07-13-21-22-37.jpg', 'PHOTO-2025-07-19-20-45-00.jpg']
# Convert to a JSON-formatted string (which uses double quotes)
print(json.dumps(file_list, indent=2))
