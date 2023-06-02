from statistics import median

times = "1|15|59, 1|16|16, 1|17|20, 1|22|34, 1|19|34, 1|15|17, 1|22|00, 1|26|37, 1|17|48, 1|16|30, 1|20|14, 1|25|11"


def stat(times):
    """
    Function to return a string containing the
    mean, range, and median of a list of times.

    Parameters
    ----------
    times : set
            times

    Returns
    -------
    str
            String containing the mean, range and median
            of a list of times.
    """
    times_list = times.split(", ")

    for time_num in range(len(times_list)):
        times_list[time_num] = times_list[time_num].split("|")

    def seconds():
        seconds_list = []

        for times in times_list:
            minutes, seconds = int(times[1]), int(times[2])
            minutes += int(times[0]) * 60
            seconds += minutes * 60
            seconds_list.append(seconds)
        return sorted(seconds_list)

    s = seconds()

    def rnge():
        r = s[-1] - s[0]
        minutes = r // 60
        seconds = r - (60 * minutes)
        hours = minutes // 60
        minutes -= hours * 60
        return f"Range: {hours}|{minutes}|{seconds}"

    def average():
        a = sum(s) // len(s)
        minutes = a // 60
        seconds = a - (60 * minutes)
        hours = minutes // 60
        minutes -= hours * 60
        return f"Average: {hours}|{minutes}|{seconds}"

    m = median(s)
    minutes = m // 60
    seconds = m - (60 * minutes)
    hours = minutes // 60
    minutes -= hours * 60
    return f"{rnge()}, {average()}, Median:C{hours}|{minutes}|{seconds}"


print(f"Using approach 1:\n\t{stat(times)}")

############################################

"""
Solutions
---------
Using approach 1:
        Range: 0|11|20, Average: 1|19|36, Median:C1.0|18.0|41.0
"""
