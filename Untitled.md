
```python
newPixels = np.array([])
threshold = 10

for pixel in tqdm(arr):
    # if it looks like black, convert it to black
    if pixel[0] <= threshold:
        newPixel = (0, 0, 0)
    # if it looks like white, convert it to white
    else:
        newPixel = (255, 255, 255)
    newPixels = np.append(newPixels, newPixel)
```

    100%|██████████| 2407680/2407680 [1:04:41<00:00, 620.35it/s]

