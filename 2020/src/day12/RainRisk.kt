package day12

import java.io.File
import kotlin.math.abs

typealias Instruction = Pair<String, Int>

fun main() {
    val input = File("src/day12/input.txt").readLines()
    val instructions: List<Instruction> = input.map { line ->
        val (action, value) = "([A-Z])([\\d]+)".toRegex().matchEntire(line)!!.destructured
        Instruction(action, value.toInt())
    }.filter { instruction ->
        !(instruction.first in listOf("L", "R") && instruction.second % 90 != 0)
    }

    println(solvePart1(instructions))
}

private fun solvePart1(instructions: List<Instruction>): Int {
    var x = 0
    var y = 0
    val directions: ArrayList<String> = arrayListOf("N", "E", "S", "W")
    var currDirection = directions[1]

    instructions.forEach { instruction ->
        val (action, value) = instruction

        when (action) {
            "N" -> y += value
            "S" -> y -= value
            "E" -> x += value
            "W" -> x -= value
            "L" -> {
                val newDirection = (value % 360) / 90
                val newIndex = (directions.indexOf(currDirection) - newDirection + directions.size) % directions.size
                currDirection = directions[newIndex]
            }
            "R" -> {
                val newDirection = (value % 360) / 90
                val newIndex = (directions.indexOf(currDirection) + newDirection) % directions.size
                currDirection = directions[newIndex]
            }
            "F" -> {
                when (currDirection) {
                    "N" -> y += value
                    "S" -> y -= value
                    "E" -> x += value
                    "W" -> x -= value
                }
            }
        }
    }

    return abs(x) + abs(y)
}

private fun solvePart2(passports: List<String>): Int {
    return 0
}