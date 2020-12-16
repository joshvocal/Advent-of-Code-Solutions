package day01

import java.io.File

fun main() {
    val expenseReport: List<Int> = File("src/day1/input.txt").readLines().map { it.toInt() }.toList()
    val target = 2020

    val (a, b) = solvePart1(expenseReport, target)
    println(a * b)

    val (c, d, e) = solvePart2(expenseReport, target)
    println(c * d * e)
}

/**
 * Two Sum
 */
private fun solvePart1(expenseReport: List<Int>, target: Int): Pair<Int, Int> {
    val s = mutableSetOf<Int>()

    expenseReport.forEach {
        val numNeeded = target - it

        if (s.contains(numNeeded)) {
            return Pair(it, numNeeded)
        }

        s.add(it)
    }

    return Pair(-1, -1)
}

/**
 * Three Sum
 */
private fun solvePart2(expenseReport: List<Int>, target: Int): Triple<Int, Int, Int> {
    val sorted = expenseReport.sorted()
    val n = expenseReport.size

    for (i in 0 until n - 2) {
        var lo = i + 1
        var hi = n - 1

        while (lo < hi) {
            val sum = sorted[i] + sorted[lo] + sorted[hi]

            when {
                sum == target -> {
                    return Triple(sorted[i], sorted[lo], sorted[hi])
                }
                sum > target -> {
                    hi -= 1
                }
                else -> {
                    lo += 1
                }
            }
        }
    }

    return Triple(-1, -1, -1)
}
