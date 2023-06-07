package day08

import java.io.File

fun main() {
    val input = File("src/day08/input.txt").readLines()
    val instructions: ArrayList<Instruction> = input.map { line -> Instruction.parse(line) } as ArrayList<Instruction>

    println(solvePart1(instructions).second)
    println(solvePart2(instructions))
}

private data class Instruction(val op: OPCODE, val arg: Int) {
    enum class OPCODE {
        JMP,
        NOP,
        ACC
    }

    companion object {
        private val pattern = "([a-z]{3}) ([+-][0-9]+)".toRegex()

        fun parse(line: String): Instruction {
            val (op, arg) = pattern.matchEntire(line)!!.destructured
            return Instruction(OPCODE.valueOf(op.toUpperCase()), arg.toInt())
        }
    }
}

private fun solvePart1(instructions: List<Instruction>): Pair<Int, Int> {
    var acc = 0
    var offset = 0
    val freqTable = IntArray(instructions.size)

    while (offset < instructions.size && freqTable[offset] == 0) {
        val (op, arg) = instructions[offset]
        freqTable[offset] += 1

        when (op) {
            Instruction.OPCODE.NOP -> offset += 1
            Instruction.OPCODE.ACC -> {
                offset += 1
                acc += arg
            }
            Instruction.OPCODE.JMP -> offset += arg
        }
    }

    return Pair(offset, acc)
}

private fun solvePart2(instructions: ArrayList<Instruction>): Int {
    for ((index, instruction) in instructions.withIndex()) {
        val instructionCopy = instruction.copy()

        when (instructionCopy.op) {
            Instruction.OPCODE.NOP -> instructions[index] = Instruction(Instruction.OPCODE.JMP, instruction.arg)
            Instruction.OPCODE.JMP -> instructions[index] = Instruction(Instruction.OPCODE.NOP, instruction.arg)
            Instruction.OPCODE.ACC -> continue
        }

        val (offset, acc) = solvePart1(instructions)

        if (offset == instructions.size) {
            return acc
        }

        instructions[index] = instructionCopy
    }

    return -1
}