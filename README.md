# Barcode Scanner

This is a simple barcode scanner program created using Python and the Tkinter library (Python version), and Java (Java version). It allows the user to input the manufacturer, serial number, model number, and storage size of a device, and stores this information in a CSV file.

## Getting Started

Link to the barcode scanner that we used =  https://tinyurl.com/vk2bbn2m

To use the Python version of this program, you will need to have Python and Tkinter installed on your machine. To use the Java version, you will need to have the latest version of Java installed.

To run the Python version of the program, open a terminal and navigate to the directory where the program is located. Then, run the following command:

python barcode_scanner.py [filename]


Replace `[filename]` with the desired name for the CSV file that will be created to store the input data. If no filename is specified, the data will be stored in a file called "data.csv".

To run the Java version of the program, open a terminal and navigate to the directory where the program is located. Then, run the following command:

java gui_barcode


## Using the Program

When the program is launched, a window will appear with the following fields:

- Manufacturer: This is a dropdown menu containing a list of manufacturer options. Select the appropriate option for the device being scanned.

- Serial Number: Enter the serial number of the device in this field.

- Model Number: Enter the model number of the device in this field.

- Size: Enter the storage size of the device in this field.

- Size: This is a dropdown menu containing options for the units of measurement for the storage size (GB, MB, or TB). Select the appropriate option.

To save the input data, click the "Save" button. To clear the fields and enter data for a new device, click the "Next" button. The input data will be stored in the CSV file specified when the Python version of the program was launched, or in a file called "data.csv" if using the Java version.

## Notes

- If the CSV file specified when the Python version of the program was launched does not already exist, it will be created. If the file does exist, the input data will be appended to the end of the file. If using the Java version, a file called "data.csv" will be created if it does not already exist.

- If the program is closed and reopened, any previously entered data will still be stored in the CSV file.

- The window cannot be resized.

- The program will continue to run until it is manually closed by the user.
