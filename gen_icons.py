#!/usr/bin/env python3
import base64, os

# SVG icon - chat bubble with heart, pink-purple gradient
svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <defs>
    <linearGradient id="g" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ff6b9d"/>
      <stop offset="50%" stop-color="#e91e8c"/>
      <stop offset="100%" stop-color="#9c27b0"/>
    </linearGradient>
  </defs>
  <rect width="512" height="512" rx="112" fill="url(#g)"/>
  <path d="M256 120 C170 120 100 178 100 250 C100 290 122 326 158 350 L148 400 L210 368 C225 372 240 374 256 374 C342 374 412 316 412 250 C412 178 342 120 256 120Z" fill="white" opacity="0.95"/>
  <path d="M256 215 C256 215 232 192 210 205 C195 214 193 233 206 247 L256 295 L306 247 C319 233 317 214 302 205 C280 192 256 215 256 215Z" fill="#e91e8c"/>
</svg>'''

os.makedirs('/home/claude/heartchat', exist_ok=True)

# Write SVG
with open('/home/claude/heartchat/icon.svg', 'w') as f:
    f.write(svg)

# Try to convert with cairosvg or PIL, else just save SVG copies named as png
try:
    import cairosvg
    cairosvg.svg2png(bytestring=svg.encode(), write_to='/home/claude/heartchat/icon-192.png', output_width=192, output_height=192)
    cairosvg.svg2png(bytestring=svg.encode(), write_to='/home/claude/heartchat/icon-512.png', output_width=512, output_height=512)
    print("Icons generated with cairosvg")
except:
    try:
        from PIL import Image
        import io, subprocess
        subprocess.run(['rsvg-convert', '-w', '192', '-h', '192', '/home/claude/heartchat/icon.svg', '-o', '/home/claude/heartchat/icon-192.png'])
        subprocess.run(['rsvg-convert', '-w', '512', '-h', '512', '/home/claude/heartchat/icon.svg', '-o', '/home/claude/heartchat/icon-512.png'])
        print("Icons generated with rsvg-convert")
    except:
        # Fallback: embed SVG as data URI in manifest
        print("Using SVG fallback")
        import shutil
        shutil.copy('/home/claude/heartchat/icon.svg', '/home/claude/heartchat/icon-192.png')
        shutil.copy('/home/claude/heartchat/icon.svg', '/home/claude/heartchat/icon-512.png')
