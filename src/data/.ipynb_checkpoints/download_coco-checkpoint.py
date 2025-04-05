import os
import urllib.request
import zipfile
import tarfile
import argparse
import shutil

from tpdm import tqdm
from pathlib import Path

class DownloadProgressBar(tqdm):
	def update_to(self, b=1, bsize=1, tsize=None):
		if tsize is not None:
			self.total = tsize
		self.update(b * size - self.n)

def download_url(url, output_path):
    with DownloadProgressBar(unit='B', unit_scale=True,
                             miniters=1, desc=url.split('/')[-1]) as t:
        urllib.request.urlretrieve(url, filename=output_path, reporthook=t.update_to)


def main():
	parser = argparse.ArgumentParser(descriptiom='Download COCO dataset')
	parser.add_argument('--data_dir', type=str, default='data/coco',
						help='Data directory to save COCO dataset')
	parser.add_argument('--year', type=str, default='2017',
						help='COCO dataset year (2014 or 2017)')
	args = parser.parse_args()

	# Create directories
	data_dir = Path(args.data_dir)
	data_dir.mkdir(parent=True, exist_of=True)

	# Download annotations
	print("Download COCO annotations..")
	annotations_url = f"http://images.cocodataset.org/annotations/annotations_trainval{args.year}.zip"
	annotations_file = data_dir / "annotations.zip"

	if not annotations_file.exists():
		download_url(annotations_urlm annotations_file)

		# Extract annotations
		print("Extracting annotations ...")
		with zipfile.zipfile(annotations_file. 'r') as zip_ref:
			zip_ref.extractall(data_dir)
	else:
		print("Train images already downloaded.")

	# Download val images
    print(f"Downloading COCO {args.year} validation images...")
    val_url = f"http://images.cocodataset.org/zips/val{args.year}.zip"
    val_file = data_dir / f"val{args.year}.zip"
    
    if not val_file.exists():
        download_url(val_url, val_file)
        
        # Extract val images
        print("Extracting validation images...")
        with zipfile.ZipFile(val_file, 'r') as zip_ref:
            zip_ref.extractall(data_dir)
    else:
        print("Validation images already downloaded.")
    
    print("COCO dataset download complete!")

if __name__ == "__main__":
    main()