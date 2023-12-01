from ColoredText import TerminalColors
list_of_strings = [
{
"output_data_filter":TerminalColors.RESET + f"""
How would like to output the filter results?")
1. On Screen (in terminal)
2. To a TEXT file
3. To an EXCEL file
4. QUIT
"""},
{
"filter_menu_options":"""
What attribute would you like to filter the data on?
1. Meteor MASS(g)
2. The YEAR the meteor fell to earth
3. QUIT
"""},
{
    "file_mode_options":f"""
What mode would you like to open the file with?
"r" - open for reading (default)
'w' - open for writing, truncating the file first. {TerminalColors.RED + "(WARNING: this mode will delete the contents of an existing file!)" + TerminalColors.RESET}
"x" - open for exclusive creation, failing if the file already exists 
"a" - open for writing, appending to the end of file if it exists 
Enter ">q" or ">0" to quit
"""

}
 ]


