# PWA Icon Generation Instructions

The PWA requires icon images in the following sizes:
- 72x72
- 96x96
- 128x128
- 144x144
- 152x152
- 192x192
- 384x384
- 512x512

## Quick Solution: Use an online icon generator

1. **Visit**: https://www.pwabuilder.com/imageGenerator
2. **Upload** a logo or image (at least 512x512)
3. **Download** the generated icons
4. **Copy** all icons to: `static/img/icons/`
5. **Rename** them to match:
   - icon-72x72.png
   - icon-96x96.png
   - icon-128x128.png
   - icon-144x144.png
   - icon-152x152.png
   - icon-192x192.png
   - icon-384x384.png
   - icon-512x512.png

## Alternative: Use existing logo

If you have a logo in `static/img/`, you can copy it multiple times with different names as a temporary solution:

```powershell
cd static/img/icons
# Copy your logo file 8 times with different names
copy ..\your-logo.png icon-72x72.png
copy ..\your-logo.png icon-96x96.png
copy ..\your-logo.png icon-128x128.png
copy ..\your-logo.png icon-144x144.png
copy ..\your-logo.png icon-152x152.png
copy ..\your-logo.png icon-192x192.png
copy ..\your-logo.png icon-384x384.png
copy ..\your-logo.png icon-512x512.png
```

## For now (temporary placeholder):

Run this command to create a simple text file placeholder:
```powershell
"Placeholder" | Out-File static\img\icons\icon-192x192.png
"Placeholder" | Out-File static\img\icons\icon-512x512.png
```

Then visit: http://127.0.0.1:8000/manifest.json to see your PWA manifest!
