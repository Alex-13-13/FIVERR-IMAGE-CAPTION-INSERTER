# FIVERR IMAGE/CAPTION INSERTER

To install the program:
git clone https://github.com/Alex-13-13/UKbro.git

IMPORTANT STUFF, READ BEFORE USING THE PROGRAM:

1.Install all the requirements in the requirements.txt file. Also, and this is ESSENTIAL for the program to work, install separately Imagemagick in its official website. If there's any error during the video creation process regarding ImageMagick while using the program and ImageMagick is installed in your computer, you must rewrite the following line of code in main.py (line 8): change_settings({"IMAGEMAGICK_BINARY": r"C:/Program Files/ImageMagick-7.1.1-Q16-HDRI/magick.exe"}) to the following change_settings({"IMAGEMAGICK_BINARY": r"{Directory in which you've installed ImageMagick}/magick.exe"}) replacing accordingly what's inside the curly brackets.

2. The spreadsheets must be in format .csv for the program to work.

3. Whenever the program asks for the name of a file, the filename extension must also be written. For example, when the program asks for the images spreadsheet, if the file is images.csv then the answer must be "images.csv" without specifying the path.

4. All the spreadsheets which are gonna be used must be in the spreadsheets folder.

5. Any video which is gonna be used must be in the video folder.

6. Any image which is gonna be used must be in the images folder.

7. The output is always written in the output folder as new_filename.mp4 so whenever the program starts generating output it replaces the previous one, so be sure to save that output file in another place if you wanna save it before starting the program again.

8. Both the images and the captions spreadsheets must have a number of slots equal to or bigger than the 9*the number of timestamps. Any of these slots can be empty.

9. Be sure to put the elements in the images and the captions spreadsheets in the same and correct order, leaving the same empty slots for both.

10. In the Cross positioning option, the first image is the one on the center, the second one on the top-left corner, the third one on the top-right corner, the fourth one on the bottom-left corner and the fifth one on the bottom-right corner. Take into account this order to enter your input correctly.

11. In the 3x3 positioning option, the first 3 images are on the top row, the next 3 ones are on the middle row and the last 3 ones are on the bottom row. Take into account this order to enter your input correctly.
