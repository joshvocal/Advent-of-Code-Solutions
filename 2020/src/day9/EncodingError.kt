package day9

import java.io.File
import java.util.*

fun main() {
    val input = File("src/day9/input.txt").readLines()
    val numbers = input.map { it.toLong() }

    println(solvePart1(numbers, 25))
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

private fun solvePart2(passports: List<String>): Int {
    return 0
}