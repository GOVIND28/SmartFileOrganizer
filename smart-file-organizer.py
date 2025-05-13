import os
import shutil
import csv
import sys
from datetime import datetime

# Map extensions to categories and subcategories
extension_map = {
    # [Same as before — unchanged]
    '.jpg': ('Images', 'JPG'), '.jpeg': ('Images', 'JPG'), '.png': ('Images', 'PNG'),
    '.gif': ('Images', 'GIF'), '.bmp': ('Images', 'BMP'), '.tiff': ('Images', 'TIFF'), '.webp': ('Images', 'WEBP'),
    '.heic': ('Images', 'HEIC'), '.svg': ('Images', 'SVG'),

    # Documents
    '.pdf': ('Documents', 'PDF'), '.docx': ('Documents', 'Word'), '.doc': ('Documents', 'Word'),
    '.txt': ('Documents', 'Text'), '.odt': ('Documents', 'Text'), '.rtf': ('Documents', 'Text'),
    '.xls': ('Documents', 'Excel'), '.xlsx': ('Documents', 'Excel'), '.ods': ('Documents', 'Excel'),
    '.ppt': ('Documents', 'PowerPoint'), '.pptx': ('Documents', 'PowerPoint'), '.csv': ('Documents', 'CSV'),
    '.md': ('Documents', 'Markdown'), '.log': ('Documents', 'Logs'),

    # Music & Audio
    '.mp3': ('Music', 'MP3'), '.wav': ('Music', 'WAV'), '.aac': ('Music', 'AAC'),
    '.flac': ('Music', 'FLAC'), '.ogg': ('Music', 'OGG'), '.m4a': ('Music', 'M4A'),
    '.wma': ('Music', 'WMA'), '.aiff': ('Music', 'AIFF'),

    # Videos
    '.mp4': ('Videos', 'MP4'), '.mov': ('Videos', 'MOV'), '.avi': ('Videos', 'AVI'),
    '.mkv': ('Videos', 'MKV'), '.flv': ('Videos', 'FLV'), '.wmv': ('Videos', 'WMV'), '.webm': ('Videos', 'WEBM'),
    '.3gp': ('Videos', '3GP'),

    # Archives & Disk Images
    '.zip': ('Archives', 'ZIP'), '.rar': ('Archives', 'RAR'), '.7z': ('Archives', '7Z'),
    '.tar': ('Archives', 'TAR'), '.gz': ('Archives', 'GZ'), '.bz2': ('Archives', 'BZ2'), '.xz': ('Archives', 'XZ'),
    '.iso': ('Archives', 'ISO'), '.dmg': ('Archives', 'DMG'),

    # Code
    '.py': ('Code', 'Python'), '.js': ('Code', 'JavaScript'), '.html': ('Code', 'HTML'), '.css': ('Code', 'CSS'),
    '.java': ('Code', 'Java'), '.cpp': ('Code', 'C++'), '.c': ('Code', 'C'), '.cs': ('Code', 'CSharp'),
    '.php': ('Code', 'PHP'), '.rb': ('Code', 'Ruby'), '.ts': ('Code', 'TypeScript'),
    '.go': ('Code', 'Go'), '.swift': ('Code', 'Swift'), '.json': ('Code', 'JSON'),
    '.xml': ('Code', 'XML'), '.sql': ('Code', 'SQL'), '.yml': ('Code', 'YAML'), '.yaml': ('Code', 'YAML'),
    '.ipynb': ('Code', 'Jupyter'),

    # Executables / Installers
    '.exe': ('Executables', 'Windows'), '.msi': ('Executables', 'Windows Installer'),
    '.bat': ('Executables', 'Batch'), '.sh': ('Executables', 'Shell'),
    '.apk': ('Executables', 'Android'), '.app': ('Executables', 'MacOS'),
    '.jar': ('Executables', 'Java'), '.deb': ('Executables', 'Debian'),
    '.rpm': ('Executables', 'RedHat'), '.bin': ('Executables', 'Binary'),

    # Fonts
    '.ttf': ('Fonts', 'TTF'), '.otf': ('Fonts', 'OTF'), '.woff': ('Fonts', 'WOFF'), '.woff2': ('Fonts', 'WOFF2'),

    # Design
    '.psd': ('Design', 'Photoshop'), '.ai': ('Design', 'Illustrator'),
    '.sketch': ('Design', 'Sketch'), '.xd': ('Design', 'XD'),
    '.fig': ('Design', 'Figma'), '.indd': ('Design', 'InDesign'),

    # Others
    '.ini': ('Others', 'Config'), '.tmp': ('Others', 'Temp'), '.bak': ('Others', 'Backup'),
    '.db': ('Others', 'Database'), '.dat': ('Others', 'Data')
}

def get_category_and_sub(ext):
    ext = ext.lower()
    return extension_map.get(ext, ('Others', None))

def organize_and_log(script_dir):
    output_folder = os.path.join(script_dir, 'organized_folder')
    os.makedirs(output_folder, exist_ok=True)
    log_data = []

    for file in os.listdir(script_dir):
        src_path = os.path.join(script_dir, file)

        # Skip this script, the output folder, and non-files
        if (os.path.isfile(src_path)
            and not src_path.startswith(output_folder)):

            ext = os.path.splitext(file)[1]
            category, subcategory = get_category_and_sub(ext)

            if subcategory:
                dest_dir = os.path.join(output_folder, category, subcategory)
            else:
                dest_dir = os.path.join(output_folder, category)

            os.makedirs(dest_dir, exist_ok=True)

            dest_path = os.path.join(dest_dir, file)
            shutil.move(src_path, dest_path)

            metadata = {
                'File Name': file,
                'Size (KB)': round(os.path.getsize(dest_path) / 1024, 2),
                'Modified': datetime.fromtimestamp(os.path.getmtime(dest_path)).strftime('%Y-%m-%d %H:%M:%S'),
                'Category': f"{category}/{subcategory}" if subcategory else category
            }
            log_data.append(metadata)

    if log_data:
        log_path = os.path.join(output_folder, 'log.csv')
        with open(log_path, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=log_data[0].keys())
            writer.writeheader()
            writer.writerows(log_data)
        print(f"✅ Organized files and created log at: {log_path}")
    else:
        print("📂 No files to organize.")

# MAIN: Use provided path or fallback to script directory
if __name__ == '__main__':
    if len(sys.argv) > 1:
        target_directory = os.path.abspath(sys.argv[1])
    else:
        target_directory = os.path.dirname(os.path.abspath(__file__))

    if not os.path.isdir(target_directory):
        print(f"❌ Provided path does not exist or is not a directory: {target_directory}")
    else:
        organize_and_log(target_directory)
