package day3

import java.io.File

fun main() {
    val input: List<String> = File("src/day3/input.txt").readLines()

    println(solvePart1(input))
    println(solvePart2(input))
}

private fun solvePart1(input: List<String>): Int =
    input.countTrees(3, 1)

private fun solvePart2(input: List<String>): Long =
    listOf(1 to 1, 3 to 1, 5 to 1, 7 to 1, 1 to 2)
        .map { input.countTrees(it.first, it.second) }
        .reduce { total, trees -> total * trees }
        .toLong()

private fun List<String>.countTrees(right: Int, down: Int): Int {
    var x = 0

    return (down until size step down).count { y ->
        x += right
        this[y][x % this[y].length] == '#'
    }
}
