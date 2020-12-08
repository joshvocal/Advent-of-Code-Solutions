package day7

import java.io.File

fun main() {
    val input = File("src/day7/sample_input.txt").readLines()
    solvePart1(input)
}

private fun solvePart1(input: List<String>): Int {

    for (line in input) {
        println(line)

        val (key, value) = line.split("contain")
        println("$key $value")

//        val a = line.split(' ')
//            .filter { !it.contains("bag") }
//            .joinToString(" ")


    }

    return 0
}

private fun solvePart2(passports: List<String>): Int {
    return 0
}