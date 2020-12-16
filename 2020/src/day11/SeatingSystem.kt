package day11

import java.io.File

fun main() {
    val input = File("src/day11/input.txt").readLines()

    println(solvePart1(input).joinToString("").count { it == OCCUPIED })
    println(solvePart2(input).joinToString("").count { it == OCCUPIED })
}

const val EMPTY = 'L'
const val FLOOR = '.'
const val OCCUPIED = '#'

fun solvePart1(seats: List<String>): List<String> {
    val newSeats = newSeats(seats)

    if (newSeats == seats) {
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
    ).map { coordinates ->
        val (x2, y2) = coordinates
        chairs.getOrNull(y + y2)?.getOrNull(x + x2)
    }

private fun solvePart2(seats: List<String>): List<String> {
    val newSeats = newSeats2(seats)

    if (newSeats == seats) {
        return newSeats
    }

    return solvePart2(newSeats)
}

fun newSeats2(floor: List<String>): List<String> {
    return floor.mapIndexed { y, row ->
        row.mapIndexed { x, seat ->
            val neighbours = getNeighbours2(x, y, floor)
            when {
                seat == EMPTY && neighbours.count { it == OCCUPIED } == 0 -> OCCUPIED
                seat == OCCUPIED && neighbours.count { it == OCCUPIED } >= 5 -> EMPTY
                else -> seat
            }
        }.joinToString("")
    }
}

private fun getNeighbours2(x: Int, y: Int, chairs: List<String>): List<Char?> =
    listOf(
        Pair(-1, -1), // Top-left
        Pair(0, -1), // Top
        Pair(1, -1), // Top-right
        Pair(-1, 0), // Left
        Pair(1, 0), // Right
        Pair(-1, 1), // Bottom-left
        Pair(0, 1), // Bottom
        Pair(1, 1), // Bottom-right
    ).map { coordinates ->
        val (x2, y2) = coordinates
        var range = 0
        var seat: Char? = chairs.getOrNull(y + y2)?.getOrNull(x + x2)

        while (seat == FLOOR) {
            range += 1
            val xSight = (x2 * range)
            val ySight = (y2 * range)
            seat = chairs.getOrNull(y + ySight)?.getOrNull(x + xSight)
        }

        seat
    }