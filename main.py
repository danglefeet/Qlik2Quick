# Project: Qlik2Quick - Qlik Sense to Amazon QuickSight Migration
from qvf_parser import QVFParser
from qlik_to_quicksight_mapper import QlikToQuickSightMapper
from quicksight_uploader import QuickSightUploader
import json
import sys
import logging
import os

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')

def process_qvf(qvf_file, config):
    logging.info(f"Processing QVF: {qvf_file}")
    parser = QVFParser(qvf_file)
    qlik_objects = parser.extract_objects()

    mapper = QlikToQuickSightMapper()
    quicksight_objects = mapper.translate(qlik_objects)

    uploader = QuickSightUploader(
        config['aws_access_key'],
        config['aws_secret_key'],
        config['aws_region'],
        config['quicksight_namespace']
    )
    uploader.deploy(quicksight_objects)

def main(target_path):
    with open('config.json') as f:
        config = json.load(f)

    if os.path.isfile(target_path) and target_path.endswith('.qvf'):
        process_qvf(target_path, config)
    elif os.path.isdir(target_path):
        for filename in os.listdir(target_path):
            if filename.endswith('.qvf'):
                full_path = os.path.join(target_path, filename)
                process_qvf(full_path, config)
    else:
        logging.error("Target must be a QVF file or a folder containing QVF files.")
        sys.exit(1)

    logging.info("Qlik2Quick migration completed successfully!")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <path_to_qvf_file_or_folder>")
        sys.exit(1)
    
    target_path = sys.argv[1]
    main(target_path)