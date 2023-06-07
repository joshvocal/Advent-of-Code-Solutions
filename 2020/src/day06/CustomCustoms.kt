package day06

import java.io.File

fun main() {
    val input: List<String> = File("src/day06/input.txt").readLines()
        .joinToString("\n")
        .split("\n\n")

    println(solvePart1(input))
    println(solvePart2(input))
}

private fun solvePart1(input: List<String>): Long {
    val groups: List<String> = input.map {
        it.split("\n").joinToString("")
    }

    return groups.map { it.chars().distinct().count() }
        .reduce { total, count -> total + count }
}

private fun solvePart2(input: List<String>): Int {
    val groups: List<List<String>> = input.map {
        it.split("\n")
    }

    return groups.map {
        it.map { person -> person.toSet() }
            .reduce { acc, person -> acc intersect person }
            .size
    }.reduce { acc, count -> acc + count }
}