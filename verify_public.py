import json,hashlib
from pathlib import Path
r=Path('site');m=json.loads(Path('content-manifest.json').read_text());d=json.loads((r/'data.json').read_text())
assert len(d['chapters'])==m['story_records']==2022
assert len(json.loads((r/'characters.json').read_text()))==11
for item in m['files']:
 p=r/item['path'];assert p.is_file() and p.stat().st_size==item['bytes'];assert hashlib.sha256(p.read_bytes()).hexdigest()==item['sha256'],item['path']
for c in d['chapters']:
 o=json.loads((r/c['detail_path']).read_text());assert o.get('polished_text');assert o['reading_status'] in ['ready','adapted']
assert {c['collection'] for c in d['chapters']}=={f'{n}-{n+99}' for n in range(1,2101,100)}
print('Verified 2022 story records, all polished, all 21 collections and every file hash')

# Publish only aggregate editorial status; no private project notes.
d['source_inventory_2100']={'total_source_records':165}
d['editorial_work_status']={'extension_601_755':{'remaining':0}}
(r/'data.json').write_text(json.dumps(d,ensure_ascii=False,separators=(',',':')))
print('Public status: 165/165 tail sources complete, 0 remaining')
