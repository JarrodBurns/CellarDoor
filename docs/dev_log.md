# CellarDoor File Backup
The intent of this application is to provide a low fluff file backup tool capable of self executing once per day.

# TO DO
- [ ] Windows Task Scheduler 
- [ ] Allow for multiple backup directories
- [ ] Multi process the zip operation to increase speed
- [X] Log and display stats

## Windows Task Scheduler
So far I have written some logic to handle scheduling windows tasks programmatically, this logic works correctly and CRUD operations can be preformed on tasks. The issue occurs that when referencing path information, through python code activated by a windows task, the application will crash. This can be prevented by providing the optional parameter *start in* to the parent directory of the python script. I can not find a way to fill this value programmatically, nor can I find the identifier to reference it. It can be filled in manually however, and the current workaround is to schedule the task manually. A future update should either set this value or provide a suitable workaround, likely in the form of a bat file.

## Log and Display Stats
- Time spent archiving
- Number of backups created
- Cumulative size of files managed 

- files deleted
