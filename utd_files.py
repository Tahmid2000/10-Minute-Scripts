import sys
from pathlib import Path

src_dir = Path('/Users/tahmidimran/Downloads')  # source directory
dst_prefix = Path('/Users/tahmidimran/Documents/UTD')
for path in src_dir.glob('*'):  # list all pdf files in source directory
    # move the pdf file if the hyphen is present in the name
    if any(substring in path.name[0:4] for substring in ['4337', '4348', '4341', '3162']):
        dst_dir = dst_prefix / 'CS {}'.format(path.name[0:4])  # destination
        dst_dir.mkdir(exist_ok=True)  # create the leaf directory if necessary
        path.replace(dst_dir / path.name)

    if any(substring in path.name[0:4] for substring in ['1303']):
        dst_dir = dst_prefix / 'GEOS {}'.format(path.name[0:4])  # destination
        dst_dir.mkdir(exist_ok=True)  # create the leaf directory if necessary
        path.replace(dst_dir / path.name)

    if any(substring in path.name[0:4] for substring in ['4141']):
        dst_dir = dst_prefix / 'CS {}'.format(path.name[0:4])  # destination
        dst_dir.mkdir(exist_ok=True)  # create the leaf directory if necessary
        path.replace(dst_dir / path.name)
