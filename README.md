# dmtool
The dmtool is a simple character creation program for DnD 3.5.
It is not supposed to be revolutionary or innovative, compared to other existing programs with same purpose. It is merely a hobby project to practice our python skills.
As we are real begginers, you are likely to find many mistakes and unfortunate solutions, this is likely to improve over time.

---Version Info---
0.0.0.0.0.1 - Early early early early pre-alfa version, we really just needed common repository to work with.


---Intended File Structure---
Files, folders and their purpose:
-- `dmtool.py` - when run, it will contain the main functions that can be called (so far probably only make_character)
-- `data` - folder with information from DnD rulebooks in XML format
  |-- `characters.xml` - data regarding attributes and creation of characters
-- `func` - folder for main functions, that can be run from dmtool.py
  |-- `make_char.py` - Process of generating a character, interactive using raw_input or it might read a simple TXT file with basic parameters of a character
-- `libraries` - folder for libraries with various generally useful functions
  |-- `dnd.py` -  general DnD functions such as dice roll
  |-- `xml_io.py` - functions for reading and writing input and output XML files
-- `Output` - generated output
  |-- `Characters` - folder with generated characters
    |-- `<character>.xml/.txt`  - generated character in both XML format for further operations and in TXT for better readability outside dmtool.py

