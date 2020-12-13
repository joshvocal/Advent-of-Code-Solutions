package day8

import java.io.File

fun main() {
    val input = File("src/day8/input.txt").readLines()
    val instructions: List<Instruction> = input.map { line -> Instruction.of(line) }

    println(solvePart1(instructions))
}


private data class Instruction(val op: String, val arg: Int, var isExecuted: Boolean = false) {
    companion object {
        private val pattern = "([a-z]{3}) ([+-][0-9]+)".toRegex()

        fun of(line: String): Instruction {
            val (op, arg) = pattern.matchEntire(line)!!.destructured
            return Instruction(op, arg.toInt())
        }
    }
}

private fun solvePart1(instructions: List<Instruction>): Int {
    var acc = 0
    var lineNum = 0

    while (!instructions[lineNum].isExecuted) {
        val (op, arg) = instructions[lineNum]
        instructions[lineNum].isExecuted = true

        when (op) {
            "nop" -> lineNum += 1
            "acc" -> {
                lineNum += 1
                acc += arg
            }
            "jmp" -> lineNum += arg
        }
    }

    return acc
}

private fun solvePart2(instructions: List<Instruction>): Int {
    return 0
}