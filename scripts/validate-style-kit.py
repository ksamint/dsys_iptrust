"""Validate public asset bytes, SVG usability, theme consistency and local guide links."""
import hashlib
import json
from pathlib import Path
import re
from urllib.parse import unquote
import xml.etree.ElementTree as ET

root = Path(__file__).resolve().parents[1]
load = lambda p: json.loads((root / p).read_text())
manifest = load('data/style-kit-assets.json')
assets = manifest['assets']
assert len(assets) == 46
assert len([a for a in assets if a['usage'] == 'reference']) == 26
assert len({a['path'] for a in assets}) == len(assets)
for a in assets:
    p = root / a['path']
    assert p.is_relative_to(root) and '..' not in Path(a['path']).parts
    b = p.read_bytes()
    assert len(b) == a['bytes'] and hashlib.sha256(b).hexdigest() == a['sha256'], p
    if a['usage'] == 'logo':
        svg = ET.fromstring(b)
        assert svg.tag.endswith('svg') and len(list(svg.iter('{http://www.w3.org/2000/svg}path'))) > 0
        assert all(e.tag.split('}')[-1] in ['svg', 'title', 'path'] for e in svg.iter())
        assert not any(k.split('}')[-1].startswith('on') for e in svg.iter() for k in e.attrib)
        assert 'viewBox' in svg.attrib
for p in root.rglob('*.json'):
    if '.git' not in p.parts:
        json.loads(p.read_text())
for p in [root / 'README.md', root / 'IPTRUST/IPTrust_DESIGN.md', root / 'IPTRUST/assets/style-kit/REFERENCES.md']:
    for target in re.findall(r'\]\(([^)]+)\)', p.read_text()):
        if '://' not in target:
            assert (p.parent / unquote(target.split('#')[0])).exists(), (p, target)
theme = load('data/theme.json')
assert theme['primary'] == '#8B7355' and theme['surface'] == '#F7F5F0' and theme['ink'] == '#2D2E30'
assert load('data/config.json')['theme'] == load('data/brand.json')['theme'] == theme
tokens = load('IPTRUST/tokens/iptrust.tokens.json')
def check_aliases(node):
    if isinstance(node, dict):
        value = node.get('$value')
        if isinstance(value, str) and value.startswith('{'):
            target = tokens
            for part in value[1:-1].split('.'):
                target = target[part]
            assert '$value' in target
        for value in node.values():
            check_aliases(value)
check_aliases(tokens)
agent = load('agent.json')
for key in ['guideline', 'tokens', 'theme', 'assets', 'references']:
    assert (root / agent[key]).exists()
for path in agent['logos'].values():
    assert (root / path).exists()
assert 'Agnes Martin, Hiroshi Sugimoto, Song Dynasty ink painting' in (root / agent['guideline']).read_text()
print('PASS: 46 asset hashes, 26 references, 3 vector logos, JSON, local links, token aliases and theme consistency.')
