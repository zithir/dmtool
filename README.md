# dmtool
The dmtool is a simple character creation program for DnD 3.5.
It is not supposed to be revolutionary or innovative, compared to other existing programs with same purpose. It is merely a hobby project to practice our python skills.
As we are real begginers, you are likely to find many mistakes and unfortunate solutions, this is likely to improve over time.

## Version Info
0.0.1 - Created character genereator module with limited functionality
0.0.0.0.0.1 - Early early early early pre-alfa version, we really just needed common repository to work with.

## Basic usage
First, the main module of the tool, the `dmtool.py` file should be run in console interactively.
After that, its individual sub-modules can be run manually (see the code in `dmtool` to see which functions can be called). 
So far only `characterGenerator` module is available.

### Character Generator
This module leads user through interactive process of character creation.
It can be run from `dmtool` with the following optional arguments (all are strings):
- `name`, `race`, `class` - if an invalid value is provided, the user is asked again during process
- `mode` - mode of character creation, following are supported and can be combined together:
  - `q` - quick mode, supresses all comfirmation Y/N prompts
  - `a` - automated mode, automated asignment of ability scores according to best skills for the class

After the charcter is created as an object `character` from a  python class `Character`, which is defined in the file `./libs/character_class.py`. You can see the file for methods and attributes which can be used with the created character. 

## TODO (and limitations)
- define additional character classes in `./data/characters.py` - so far there are only three
- create a function that would output the character into a text file for further use and print
- proceed with skills and feats selection

## Files description
- `dmtool.py` - when run, it will contain the main functions that can be called (so far probably only characterGenerator)
- `data` - folder with information from DnD rulebooks in XML
  - `characters.py` - data regarding attributes and creation of characters
- `modules` - folder for main functions, that can be run from dmtool.py
  - `character_generator.py` - Process of generating a character, it can use arguments or it can be interactive using user input or 
- `libs` - folder for libraries with various generally useful functions
  - `dnd_utils.py` -  general DnD functions such as dice roll
  - `fetch_data.py` - __functions for providing data from `data` file etc. This seemingly redundant module is used used, because the way the data is stored could change in the future. If the data format is changed, only this file should be changed to provide identical input to other modules__
- `Output` - generated output, there is none yet however 
  - `Characters` - folder with generated characters
    - `<character>.xml/.txt`  - generated character in both XML format for further operations and in TXT for better readability outside dmtool.py

