# Pearson-Books

This repo gives you many pearson books (PDF version) for free, now in script we have this books:
- Chemistry <img src="https://www.pearsonactivelearn.com/r00/r0070/r007014/r00701433/current/OPS/images/9780435185169_Refinery_(1)-001.jpg" alt="Chemistry" width="100"/>
- Physics___ <img src="https://www.pearsonactivelearn.com/r00/r0070/r007007/r00700764/current/OPS/images/9780435185275_(1)-001.jpg" alt="Physics" width="100"/>
- ICT_______ <img src="https://www.pearsonactivelearn.com/r00/r0073/r007337/r00733746/current/OPS/images/9780435188931-001.jpg" alt="ICT" width="100"/>
- English___ <img src="https://www.pearsonactivelearn.com/r01/r0113/r011390/r01139006/current/OPS/images/9781292458458-001.jpg" alt="English" width="100"/>
- Economics <img src="https://www.pearsonactivelearn.com/r00/r0074/r007462/r00746286/current/OPS/images/9780435188641-001.jpg" alt="Economics" width="100"/>

## If in script your book is not exist?

1. On first page of your book exist code and instructions what to do with it, please do it on your PC or in browser with Developer Tools.
2. After this, you'll have something like this, but only with one book: ![image](https://github.com/user-attachments/assets/1207221f-b5b0-455e-9640-857327117bd6)
3. Click on your book: ![image](https://github.com/user-attachments/assets/d75eb288-3c0a-4382-863b-199833187d49)
4. And click again, you need to give Pop-up permission, after this you'll see this: ![image](https://github.com/user-attachments/assets/9fbbc3f8-dd58-4604-9276-4cfa8d3c264f)
5. Press F12 and navigate to resource tab, and open path like on image (ofc, you'll have different path): ![image](https://github.com/user-attachments/assets/41c30302-50d7-4420-a300-457636a7aefa)
6. Copy this image URL and past it in variable base_url without extension and last three numbers:
    - Original URl: ```https://www.pearsonactivelearn.com/r00/r0070/r007014/r00701433/current/OPS/images/9780435185169_Refinery_(1)-001.jpg```
    - URL which you need to past in variable: ```https://www.pearsonactivelearn.com/r00/r0070/r007014/r00701433/current/OPS/images/9780435185169_Refinery_(1)-```
7. Commet other base_line if you have it uncommented
8. Read ```Run``` part in this README
9. Create pull request

## RUN
Installl reauirements:
``` pip install requests Pillow ```

Run script:
```python main.py```



