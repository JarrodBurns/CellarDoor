# CellarDoor File Backup
The intent of this application is to provide a low fluff file backup tool capable of self executing once per day.

# TO DO
- [X] [Record and Display Stats](#record-and-display-stats)
- [ ] Relative imports
- [ ] Logging
- [ ] Update configs to YAML
- [ ] [Windows Task Scheduler](#windows-task-scheduler)
- [ ] Allow for multiple backup directories
- [ ] Multi process the zip operation to increase speed

## Fixes
- [ ] All file ops should check/create/error
- [ ] Incorporate new datetime constants/rewrite parser logic
- [ ] UI stats, str conversion necessary?

## Reading list
- [ ] [ZipFile](https://docs.python.org/3/library/zipfile.html?highlight=zipfile#module-zipfile)
- [ ] [Pathlib - Modern Paths in Python](https://docs.python.org/3/library/pathlib.html?highlight=pathlib#module-pathlib)
- [X] [Loggging](https://docs.python.org/3/library/logging.html)
- [ ] [Logging Config File](https://docs.python.org/3/library/logging.config.html#module-logging.config)
- [ ] [YAML](https://realpython.com/python-yaml/)
- [ ] [XML Processing Modules](https://docs.python.org/3/library/xml.html?highlight=xml#module-xml)
- [ ] [Task Scheduler Schema](https://docs.microsoft.com/en-us/windows/win32/taskschd/task-scheduler-schema)

## Windows Task Scheduler
So far I have written some logic to handle scheduling windows tasks programmatically, this logic works correctly and CRUD operations can be preformed on tasks. The issue occurs when referencing path information through python code activated by a windows task; the application will crash. This can be prevented by pointing the optional parameter *start in* to the parent directory of the python script. I can not find a way to fill this value programmatically, nor can I find the identifier to reference it. It can be filled in manually however, and the current workaround is to schedule the task manually. A future update should either set this value or provide a suitable workaround, likely in the form of a bat file.

### Windows Task Scheduler Update 12 Sep 2022
After conducting more investigation, it seems the best way to interact with the Task Scheduler is through an XML file. In development, this file can be pulled down from an existing task. The idea then is to generate this XML dynamically, in application if the config has changed and then save and pass that data on to the WTS.


## Record and Display Stats
- Time spent archiving
- Number of backups created
- Cumulative size of files managed 

- Files deleted
