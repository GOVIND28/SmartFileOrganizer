# 📁 Smart File Organizer ✨

Organize your cluttered folders automatically based on file type! This Python script sorts files into categorized subdirectories and generates a detailed log of the process.

## ✨ Features

* ⚙️ **Automatic Sorting:** Moves files into `Category/Subcategory` folders based on their extensions.
* 🗺️ **Extensive Mapping:** Pre-configured mappings for a wide range of file types (Images, Documents, Music, Videos, Code, Archives, Executables, etc.).
* 🏗️ **Hierarchical Structure:** Creates a clear and organized directory structure within a dedicated folder named `organized_folder`.
* 📝 **Detailed Logging:** Generates a `log.csv` file listing every moved file, its original name, size, last modified time, and its new location.
* 🎯 **Flexible Target:** Can organize the script's own directory by default or a specific directory provided as a command-line argument.
* 🔒 **Safe Execution:** Skips the script file itself and the destination `organized_folder`.

## 🚀 How to Use

Make sure you have the Python script file (`smart-file-organizer.py`).

Open your terminal or command prompt and navigate to the directory containing the script (if you want to organize that directory) or to any location if you plan to provide a target path.

Then, run the script using one of the following methods:

* ▶️ **Organize the script's current directory:**
    ```bash
    python3 smart-file-organizer.py
    ```
    (The script will organize files found directly in the directory where the `smart-file-organizer.py` file is located).

* ▶️ **Organize a specific directory:**
    ```bash
    python3 smart-file-organizer.py /path/to/your/target/directory
    ```
    Replace `/path/to/your/target/directory` with the actual path to the folder you want to organize.

## 🧠 Organization Logic

The script uses an internal dictionary (`extension_map`) to determine the `Category` and optional `Subcategory` for each file extension.

All organized files will be moved into a new folder named `organized_folder` 📁 within the target directory. Inside `organized_folder`, subfolders like `Images` 🖼️, `Documents` 📄, `Music` 🎵, etc., will be created, with further subfolders like `JPG`, `PDF`, `MP3` based on the file's specific type. Files with extensions not found in the map will be placed directly in the `Others` 🤷‍♀️ category folder within `organized_folder`.

⚠️ **Note:** The script *moves* ➡️ the files, it does not copy them. The original files will be removed from the source directory.

## 📝 Log File (`log.csv`)

After organizing, a file named `log.csv` is created inside the `organized_folder`. This file contains a record of every file that was moved, including:

* 📊 `File Name`: The original name of the file.
* 📏 `Size (KB)`: The size of the file in kilobytes.
* ⏱️ `Modified`: The last modified timestamp of the file.
* 📍 `Category`: The final destination path relative to `organized_folder` (e.g., `Images/JPG`, `Documents/PDF`, `Others`).

## ⚠️ Important Considerations

* ❌ The script only processes files directly within the target directory. It does **not** traverse subdirectories.
* ⏭️ The script will not move itself or the `organized_folder`.
* 🤷‍♀️ Files with extensions not listed in `extension_map` will be moved to an `Others` folder.
* 🧪 Be cautious when running this script on important directories for the first time. It's recommended to test it on a backup or a less critical folder.

## ⚙️ Customization

You can easily customize the file organization by modifying the `extension_map` dictionary directly within the Python script (`smart-file-organizer.py`). You can add new extensions and their desired category/subcategory, change existing mappings, or remove extensions.

## Author
👨‍💻 Author <br>
Made with ❤️ by **Govind Ambade** <br>
[LinkedIn](https://www.linkedin.com/in/govind-ambade/) <br>
Drop a ⭐ on the repo if you found it helpful! <br>
