# FSA Utility Scripts

These scripts are to aid in the assignment and administration of the Frisco Soccer Association. 

### Create Mentor Schedule

Usage: 

```
python3 create-mentor-schedule.py INPUT_FILE.csv OUTPUT_FILE.csv
```


The script takes the league schedule and creates a schedule for the mentors to follow. 

The mentor schedule starts at the time of the first kick off and has time slots every hour on the hour until an hour after the final kick off time. 

The venues are limited by the `ALLOWED_VENUES` variable at the top of the script. 

The script makes the following assumptions: 
- Date is in column 3
- Start time is in column 4
- Venue/complex is in column 5

These assumptions may need to be changed over time.  


