import os
from collections import defaultdict
from flask import Blueprint, render_template, send_from_directory

# compute paths
HERE         = os.path.dirname(__file__)                             # …/web_apps/alexpedia_40k_app
PROJECT_ROOT = os.path.abspath(os.path.join(HERE, os.pardir, os.pardir))
TEMPLATE_DIR = os.path.join('templates','alexpedia_40k')
DATASHEET_DIR = os.path.join(HERE, 'datasheets')                               # …/web_apps/alexpedia_40k_app/datasheets

bp = Blueprint(
    'alexpedia', 
    __name__,
    url_prefix='/alexpedia_40k'
)

# ——— Helper to scan datasheets ———
def load_datasheets():
    out = []
    for fac in sorted(os.listdir(DATASHEET_DIR)):
        fac_dir = os.path.join(DATASHEET_DIR, fac)
        if not os.path.isdir(fac_dir):
            continue
        for fn in sorted(os.listdir(fac_dir)):
            if fn.lower().endswith('.html'):
                out.append({
                    'label': fn[:-5],
                    'path':  f"{fac}/{fn}"
                })
    return out

# ——— Load datasheets once at import time ———
datasheets = load_datasheets()


@bp.route('/')
def index():
    # group the preloaded datasheets by faction
    grouped = defaultdict(list)
    for ds in datasheets:
        fac = ds['path'].split('/', 1)[0]
        grouped[fac].append(ds)
    return render_template('alexpedia_40k/index.html', ds_by_faction=dict(grouped))

@bp.route('/roster')
def roster():
    return render_template('alexpedia_40k/roster.html')

@bp.route('/points')
def points():
    return render_template('alexpedia_40k/points.html')

@bp.route('/datasheets/<path:filename>')
def serve_datasheet(filename):
    return send_from_directory(DATASHEET_DIR, filename)