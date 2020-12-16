package day13

import java.io.File
import kotlin.math.floor

fun main() {
    val input = File("src/day13/input.txt").readLines()

    val earliestTime = input[0].toInt()
    val busIds = input[1].split(",")
        .filter { busId -> busId != "x" }
        .map { it.toInt() }

    println(solvePart1(earliestTime, busIds))
}

private fun solvePart1(earliestTime: Int, busIds: List<Int>): Int {
    val map = hashMapOf<Int, Int>()
    var min = Int.MAX_VALUE
    var earliestBusId = busIds[0]

    busIds.forEach {
        val earliestBus = (floor(earliestTime / it.toDouble()) + 1) * it
        map[it] = earliestBus.toInt()
    }

    map.forEach { (key, value) ->
        if (value - earliestTime < min) {
            earliestBusId = key
            min = value - earliestTime
        }
    }

    return earliestBusId * min
}

private fun solvePart2(passports: List<String>): Int {
    return 0
}