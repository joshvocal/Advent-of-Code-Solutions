package day11

import java.io.File

fun main() {
    val input = File("src/day11/input.txt").readLines()

    println(solvePart1(input).joinToString("").count { it == OCCUPIED })
}

const val EMPTY = 'L'
const val OCCUPIED = '#'

fun solvePart1(chairs: List<String>): List<String> {
    val newSeats = newSeats(chairs)

    if (newSeats == chairs) {
        return newSeats
    }

    return solvePart1(newSeats)
}

fun newSeats(floor: List<String>): List<String> {
    return floor.mapIndexed { y, row ->
        row.mapIndexed { x, seat ->
            val neighbours = getNeighbours(x, y, floor)
            when {
                seat == EMPTY && neighbours.count { it == OCCUPIED } == 0 -> OCCUPIED
                seat == OCCUPIED && neighbours.count { it == OCCUPIED } >= 4 -> EMPTY
                else -> seat
            }
        }.joinToString("")
    }
}


private fun getNeighbours(x: Int, y: Int, chairs: List<String>): List<Char?> =
    listOf(
        Pair(-1, -1), // Top-left
        Pair(0, -1), // Top
        Pair(1, -1), // Top-right
        Pair(-1, 0), // Left
        Pair(1, 0), // Right
        Pair(-1, 1), // Bottom-left
        Pair(0, 1), // Bottom
        Pair(1, 1), // Bottom-right
    ).map { chairs.getOrNull(y + it.second)?.getOrNull(x + it.first) }

private fun solvePart2(passports: List<String>): Int {
    return 0
}