package day05

import java.io.File

fun main() {
    val input = File("src/day05/input.txt").readLines()
    println(solvePart1(input))
    println(solvePart2(input))
}

private fun String.toBinary() = map { if (it in listOf('B', 'R')) '1' else '0' }.joinToString("")

private fun solvePart1(input: List<String>): Int {
    val ids = input.map { it.toBinary().toInt(2) }
        .sortedDescending()

    return ids.first()
}

// Find the first seat that is not +1
private fun solvePart2(input: List<String>): Int {
    val ids = input.map { it.toBinary().toInt(2) }
        .sorted()

    val seat = ids.zipWithNext()
        .first { (first, second) -> first != second - 1 }
        .first + 1

    return seat
}