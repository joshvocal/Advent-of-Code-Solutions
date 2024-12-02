import sys
from itertools import pairwise

class Solution:
    def part1(self, lines: list[str]) -> int:
        reports = []
        safe_reports = 0

        for line in lines:
            reports.append([int(s) for s in line.split(' ')])

        def is_safe(report):
            max_dist = max(abs(b-a) for (a,b) in pairwise(report))
            all_dec = all(i > j for i, j in zip(report, report[1:]))
            all_inc = all(i < j for i, j in zip(report, report[1:]))

            return max_dist <= 3 and (all_dec or all_inc)

        for report in reports:
            if is_safe(report):
                safe_reports += 1

        return safe_reports

    def part2(self, lines: list[str]) -> int:
        reports = []
        safe_reports = 0

        for line in lines:
            reports.append([int(s) for s in line.split(' ')])

        def is_safe(report):
            max_dist = max(abs(b-a) for (a,b) in pairwise(report))
            all_dec = all(i > j for i, j in zip(report, report[1:]))
            all_inc = all(i < j for i, j in zip(report, report[1:]))

            return max_dist <= 3 and (all_dec or all_inc)

        for report in reports:
            if is_safe(report):
                safe_reports += 1
                continue

            for i in range(len(report)):
                report_copy = report.copy()
                del report_copy[i]
                if is_safe(report_copy):
                    safe_reports += 1
                    break

        return safe_reports

def main(textfile):
    with open(textfile, "r") as f:
        lines = f.read().splitlines()

        sol = Solution()

        print(sol.part1(lines))
        print(sol.part2(lines))

if __name__ == "__main__":
    main(sys.argv[1])
