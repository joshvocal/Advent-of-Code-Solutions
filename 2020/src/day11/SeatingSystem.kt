package day11

import java.io.File

fun main() {
    val input = File("src/day11/sample_input.txt").readLines()

    val grid: ArrayList<ArrayList<Char>> = ArrayList()
    val gridCopy: ArrayList<ArrayList<Char>> = ArrayList()

    input.forEach { grid.add(it.toList() as ArrayList<Char>) }
    input.forEach { gridCopy.add(it.toList() as ArrayList<Char>) }

//    solvePart1(grid, gridCopy)
}

const val EMPTY = 'L'
const val FLOOR = '.'
const val OCCUPIED = '#'

private fun solvePart1(
    grid: ArrayList<ArrayList<Char>>,
    gridCopy: ArrayList<ArrayList<Char>>
): ArrayList<ArrayList<Char>> {


    for (y in grid.indices) {
        for (x in grid[0].indices) {
            when (grid[y][x]) {
                FLOOR -> continue
                EMPTY,
                OCCUPIED -> checkSeat(y, x, grid, gridCopy, 0)
            }
        }
    }


    println()
    println()
    grid.forEach { println(it.joinToString("")) }
    println()
    gridCopy.forEach { println(it.joinToString("")) }

    return gridCopy
}

private fun checkSeat(
    y: Int,
    x: Int,
    grid: ArrayList<ArrayList<Char>>,
    gridCopy: ArrayList<ArrayList<Char>>,
    steps: Int
): Char {
    if (y >= grid.size || y < 0 || x >= grid[0].size || x < 0 || grid[y][x] == FLOOR || steps > 1) {
        return '.'
    }

    val topLeft = checkSeat(y - 1, x - 1, grid, gridCopy, steps + 1)
    val top = checkSeat(y - 1, x, grid, gridCopy, steps + 1)
    val topRight = checkSeat(y - 1, x + 1, grid, gridCopy, steps + 1)
    val left = checkSeat(y, x - 1, grid, gridCopy, steps + 1)
    val right = checkSeat(y, x + 1, grid, gridCopy, steps + 1)
    val bottomLeft = checkSeat(y + 1, x - 1, grid, gridCopy, steps + 1)
    val bottom = checkSeat(y + 1, x, grid, gridCopy, steps + 1)
    val bottomRight = checkSeat(y + 1, x + 1, grid, gridCopy, steps + 1)

    val seats = arrayListOf(topLeft, top, topRight, left, right, bottomLeft, bottom, bottomRight)
    println("$seats $x $y")
    val noOccupiedSeatsAround = seats.all { it == EMPTY || it == FLOOR }
    val fourOrMoreAdjacent = seats.count { it == OCCUPIED } >= 4

    if (grid[y][x] == EMPTY && noOccupiedSeatsAround) {
        gridCopy[y][x] = OCCUPIED
    } else if (grid[y][x] == OCCUPIED && fourOrMoreAdjacent) {
        gridCopy[y][x] = EMPTY
    }

    return grid[y][x]
}


private fun solvePart2(passports: List<String>): Int {
    return 0
}