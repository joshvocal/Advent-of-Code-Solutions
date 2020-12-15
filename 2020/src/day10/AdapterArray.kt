package day10

import java.io.File
import java.util.*

fun main() {
    val input = File("src/day10/input.txt").readLines()
    val adapters: List<Int> = input.map { it.toInt() }

    println(solvePart1(adapters))
}

private fun solvePart1(adapters: List<Int>): Int {
    val pq: PriorityQueue<Int> = PriorityQueue(adapters)
    var diffs = 0
    var prev = 0
    var numOneJoltDif = 0
    var numThreeJoltDif = 1

    while (pq.isNotEmpty()) {
        val curr = pq.remove()
        val dif = curr - prev

        when (dif) {
            3 -> numThreeJoltDif += 1
            1 -> numOneJoltDif += 1
        }

        diffs += dif
        prev = curr
    }

    return numThreeJoltDif * numOneJoltDif
}

private fun solvePart2(passports: List<String>): Int {
    return 0
}