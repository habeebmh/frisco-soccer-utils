import csv
import sys
from datetime import datetime, timedelta

ALLOWED_VENUES = [
    "Northeast Community Park",
    "Warren Soccer Complex",
    "Toyota Soccer Center",
]


def calculate_hours(start_times):
    sorted_times = sorted([datetime.strptime(t, "%I:%M%p") for t in start_times])
    earliest = sorted_times[0]
    latest = sorted_times[-1] + timedelta(hours=1)

    times = [earliest]

    while times[-1] <= latest:
        next_hour = times[-1] + timedelta(hours=1)
        times.append(next_hour)

    return [
        {
            "start": t.strftime("%I:%M%p"),
            "end": (t + timedelta(hours=1)).strftime("%I:%M%p"),
        }
        for t in times
    ]


def main():
    input_file_name = sys.argv[1]
    output_file_name = "output.csv" if sys.argv[2] is None else sys.argv[2]
    dates = {}

    with open("./" + input_file_name, "r") as matches:
        csv_file = csv.reader(matches, delimiter=",")
        for row in csv_file:
            date = row[2].strip()
            start_time = row[3].strip()
            complex = row[4].strip()

            if complex not in ALLOWED_VENUES:
                continue

            combined_key = date + "," + complex

            if combined_key not in dates:
                dates[combined_key] = []

            dates[combined_key].append(start_time)

    with open("./" + output_file_name, "w") as output:
        for (date, times) in dates.items():
            sorted_times = calculate_hours(times)
            lines = []
            for t in sorted_times:
                line = date + "," + t["start"] + "," + t["end"] + "\n"

                if line not in lines:
                    lines.append(line)

            output.writelines(lines)
            output.write("\n")


if __name__ == "__main__":
    main()
