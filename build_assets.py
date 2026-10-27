"""Rebuild the profile's self-contained vector artwork. Python standard library only."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent / 'assets'
ROOT.mkdir(exist_ok=True)

def hero(dark, mobile):
    bg, panel = ('#0b101b', '#101a2a') if dark else ('#f4f7fc', '#e7eef8')
    ink, muted = ('#f0f5ff', '#a5b6cf') if dark else ('#132239', '#4b607b')
    cyan, violet, copper = ('#62e4df', '#b7a1ff', '#eeb482') if dark else ('#087b80', '#7550c4', '#975422')
    line = '#293d54' if dark else '#b8c9dc'
    w, h = (480, 420) if mobile else (960, 380)
    x, y, scale = (374, 330, .58) if mobile else (770, 182, 1)
    name_size = 49 if mobile else 70
    name_y = 128 if mobile else 154
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc">
<title id="title">Ahmed Emad — WinchesterxZ</title>
<desc id="desc">Cybersecurity and mobile development. An orbital signal diagram accompanies the words Build with care. Test with curiosity.</desc>
<defs>
 <pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse"><path d="M32 0H0V32" fill="none" stroke="{line}" stroke-width=".6" opacity=".32"/></pattern>
 <linearGradient id="edge"><stop stop-color="{cyan}"/><stop offset=".6" stop-color="{violet}"/><stop offset="1" stop-color="{copper}"/></linearGradient>
 <radialGradient id="halo"><stop stop-color="{cyan}" stop-opacity=".11"/><stop offset="1" stop-color="{cyan}" stop-opacity="0"/></radialGradient>
</defs>
<style>
 text{{font-family:Arial,Helvetica,sans-serif}}
 .mono{{font-family:'Courier New',monospace;letter-spacing:2px}}
 .orbit{{animation:orbit 32s linear infinite}}
 .trace{{animation:trace 16s linear infinite}}
 @keyframes orbit{{to{{transform:rotate(360deg)}}}}
 @keyframes trace{{to{{stroke-dashoffset:-160}}}}
 @media(prefers-reduced-motion:reduce){{.orbit,.trace{{animation:none}}}}
</style>
<rect x="1" y="1" width="{w-2}" height="{h-2}" rx="18" fill="{bg}" stroke="{line}"/>
<rect x="1" y="1" width="{w-2}" height="{h-2}" rx="18" fill="url(#grid)"/>
<path d="M28 1H{w-28}" stroke="url(#edge)" stroke-width="2"/>
<path d="M24 48V24H48 M{w-48} {h-24}H{w-24}V{h-48}" fill="none" stroke="{cyan}" stroke-opacity=".6"/>
<g transform="translate({x} {y}) scale({scale})" aria-hidden="true">
 <circle r="180" fill="url(#halo)"/>
 <path d="M-156 0H156 M0-156V156" stroke="{line}" stroke-dasharray="2 8"/>
 <circle r="137" fill="none" stroke="{line}"/>
 <circle r="114" fill="none" stroke="{cyan}" stroke-opacity=".5" stroke-dasharray="2 11"/>
 <circle r="91" fill="{panel}" stroke="{line}"/>
 <g class="orbit"><path d="M0-137A137 137 0 0 1 137 0" fill="none" stroke="{cyan}" stroke-width="2"/><circle cy="-137" r="4" fill="{cyan}"/><circle cy="137" r="3" fill="{violet}"/></g>
 <path d="M-54-32L-28 39 0-14 28 39 54-32 M-36-32L-17 12 M36-32L17 12" fill="none" stroke="url(#edge)" stroke-width="4" stroke-linejoin="bevel"/>
 <path d="M-51 65H51" stroke="{line}"/>
 <text y="80" text-anchor="middle" font-size="9" fill="{muted}" class="mono">WX / SIGNAL</text>
 <path class="trace" d="M-162 102H-116L-95 81 M91-87L115-111H160" stroke="{violet}" stroke-dasharray="16 8" fill="none"/>
 <path d="M-7-153H7 M-7 153H7 M-153-7V7 M153-7V7" stroke="{copper}" stroke-width="2"/>
</g>
<text x="{'32' if mobile else '42'}" y="56" fill="{cyan}" font-size="{'13' if mobile else '12'}" class="mono">WINCHESTERXZ / PERSONAL LOG</text>
<text x="{'30' if mobile else '38'}" y="{name_y}" fill="{ink}" font-weight="750" font-size="{name_size}" letter-spacing="-2">AHMED EMAD<tspan fill="{copper}">.</tspan></text>
<text x="{'32' if mobile else '42'}" y="{name_y+38}" fill="{muted}" font-size="{'16' if mobile else '19'}">Cybersecurity &amp; mobile development</text>
<path d="M{'32' if mobile else '42'} {name_y+62}H{'144' if mobile else '166'}" stroke="url(#edge)" stroke-width="2"/>
<text x="{'32' if mobile else '42'}" y="{name_y+103}" fill="{ink}" font-size="{'21' if mobile else '23'}">Build with care.</text>
<text x="{'32' if mobile else '42'}" y="{name_y+133}" fill="{ink}" font-size="{'21' if mobile else '23'}">Test with curiosity.</text>
<text x="{'32' if mobile else '42'}" y="{h-41}" fill="{muted}" font-size="{'12' if mobile else '11'}" class="mono">{'BUILD / TRACE / UNDERSTAND' if mobile else '01 / APPLICATION SECURITY     02 / SOC     03 / ANDROID'}</text>
</svg>
'''

for dark in [True, False]:
    for mobile in [True, False]:
        name = 'hero-' + ('mobile-' if mobile else '') + ('dark' if dark else 'light') + '.svg'
        (ROOT / name).write_text(hero(dark, mobile), encoding='utf-8')

(ROOT / 'signal.svg').write_text('''<svg xmlns="http://www.w3.org/2000/svg" width="960" height="32" viewBox="0 0 960 32" role="presentation">
<style>.s{stroke:#087b80}.v{stroke:#7550c4}@media(prefers-color-scheme:dark){.s{stroke:#62e4df}.v{stroke:#b7a1ff}}</style>
<path class="s" d="M0 16H400L411 7H441L452 16H960" opacity=".4" fill="none"/>
<path class="v" d="M462 16H508L519 25H549L560 16" fill="none"/>
<circle class="s" cx="7" cy="16" r="3" fill="none"/><circle class="v" cx="953" cy="16" r="3" fill="none"/>
</svg>
''', encoding='utf-8')
print('Built five SVG assets.')
