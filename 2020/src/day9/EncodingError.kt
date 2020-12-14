package day9

import java.io.File
import java.util.*

fun main() {
    val input = File("src/day9/input.txt").readLines()
    val numbers: ArrayList<Long> = input.map { it.toLong() } as ArrayList<Long>

    val weakness = solvePart1(numbers, 25)
    println(weakness)
    println(solvePart2(numbers, weakness))
}

private fun search(arr: List<Long>, target: Long): Boolean {
    var lo = 0
    var hi = arr.size - 1

    while (lo < hi) {
        val sum = arr[lo] + arr[hi]

        when {
            target == sum -> return true
            target > sum -> lo += 1
            else -> hi -= 1
        }
    }

    return false
}

/**
 * Queue
 */
private fun solvePart1(numbers: List<Long>, preamble: Int): Long {
    val queue: Queue<Long> = LinkedList()

    numbers.take(preamble).forEach { number -> queue.add(number) }

    for (i in preamble until numbers.size) {
        val nextNumber = numbers[i]

        if (!search(queue.sorted().toList(), nextNumber)) {
            return nextNumber
        }

        queue.add(nextNumber)
        queue.remove()
    }

    return -1
}

/**
 * Sliding Window
 */
private fun solvePart2(numbers: ArrayList<Long>, target: Long): Long? {
    var currentSum = 0L
    var start = 0

    for (end in 0 until numbers.size) {
        currentSum += numbers[end]

        while (currentSum >= target) {
            if (currentSum == target) {
                val range = start..end
                val min = numbers.slice(range).minOrNull()!!
                val max = numbers.slice(range).maxOrNull()!!
                return min + max
            }

            currentSum -= numbers[start]
            start += 1
        }
    }

    return null
}