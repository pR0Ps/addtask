# addtask

## Description
[Addtask](https://github.com/pr0ps/addtask) is a command-line utility to add tasks to Google Tasks. It understands most natural language queries (just don't get too crazy).
For example `./addtask.py 1 month, 2 weeks, and 3 days from now do something`.

I built this because I was frustrated with the lack of tools to quickly add tasks.
Other tools all enforce a stricter command syntax.
I didn't want to think about date formatting or anything, I just wanted to create the task.

## Limitations
Currenty nothing is implemented to split up the date and the title of the task.
Because of this the task will be added with the name exactly as typed.
For example, the command above will create an event called "1 month, 2 weeks, and 3 days from now do something" in 1 month, 2 weeks, and 3 days.

## Dependencies
Requires Python 2.7 and the [Google API client for Python](http://code.google.com/p/google-api-python-client/).
The needed packages are installable from PyPi and are in the `requirements.txt` file. Use `pip install -r requirements.txt` to install them.

**NOTE**: This script will create an unencypted `~/.config/addtask/keys.txt` to hold API credentials on disk.

## Installation

### Connecting to the Tasks API
1. Go to https://cloud.google.com/console/project
2. Create a project.
3. Enable the Tasks API (disable everything else).
4. Go to the credentials screen.
5. Click the "Create new Key" button under the Public API access section.
6. Generate a browser key and leave the URL restriction blank.
7. Install the requirements in `requirements.txt`
7. Run addtask and enter the needed information.

### Local

Symlink or move the script into a folder in your $PATH. Feel free to take off the '.py' extension as well.
      
## Usage Examples

      addtask Do groceries tomorrow
      addtask Buy a birthday card next week   
      addtask Buy a drink this friday
      addtask Buy a drink next friday
      addtask Essay due in a week
      addtask Apply for job on saturday
      addtask Pay bills next month
      addtask TPS report in 3 days
      addtask Remember Birthday April 17th

## Development/License
Addtask uses authentication code from [Tasky by Ajay Roopakalu](https://github.com/jrupac/tasky) and is therefore licenced under the [GNU GPL license](http://www.gnu.org/licenses/gpl.txt).

Bug reports and pull requests welcome!
