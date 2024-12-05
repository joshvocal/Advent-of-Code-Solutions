import sys
from collections import defaultdict
import itertools

class Solution:
    def part1(self, first_rule, page_number):
        order_map = defaultdict(list)
        right_order = []
        res = 0

        for before, after in first_rule:
            order_map[before].append(after)

        for page in page_number:
            is_right = True
            for i, _ in enumerate(page):
                curr = page[i]
                page_copy = page.copy()
                del page_copy[i]

                a = set(page_copy)
                b = set(order_map[curr])
                intersec = a.intersection(b)

                if len(intersec) != len(page) - 1 - i:
                    is_right = False
                    break

            if is_right:
                right_order.append(page)

        for arr in right_order:
            res += arr[len(arr) // 2]

        return res, right_order

    def part2(self, first_rule, bad_order) -> int:
        order_map = defaultdict(list)
        right_order = []
        res = 0

        for before, after in first_rule:
            order_map[before].append(after)

        def is_correct(page):
            is_right = True
            for i, _ in enumerate(page):
                curr = page[i]
                page_copy = page.copy()
                del page_copy[i]

                a = set(page_copy)
                b = set(order_map[curr])
                intersec = a.intersection(b)

                if len(intersec) != len(page) - 1 - i:
                    is_right = False
                    break

            return is_right

        for page in bad_order:
            while not is_correct(page):
                for i in range(len(page)):
                    for j in range(i+1, len(page)):
                        if page[i] in order_map[page[j]]:
                            page[j], page[i] = page[i], page[j]

            right_order.append(page)

        for arr in right_order:
            res += arr[len(arr) // 2]

        return res, right_order

def main(textfile):
    with open(textfile, "r") as f:
        first, second = f.read().strip().split('\n\n')

        sol = Solution()

        first_rule = []
        page_numbers = []

        for rule in first.splitlines():
            before, after = rule.split("|")
            first_rule.append((int(before), int(after)))

        for page in second.splitlines():
            page_numbers.append([int(s) for s in page.split(",")])
        
        ans, right_order = sol.part1(first_rule, page_numbers)
        print(ans)

        bad_order = [row for row in right_order if row not in page_numbers] + [row for row in page_numbers if row not in right_order] 
        ans2, right_order2 = sol.part2(first_rule, bad_order)
        print(ans2)

if __name__ == "__main__":
    main(sys.argv[1])
