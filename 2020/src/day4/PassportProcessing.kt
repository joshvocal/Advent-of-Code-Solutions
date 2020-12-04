package day4

import java.io.File

fun main() {
    val input: List<String> = File("src/day4/input.txt").readLines()
    println(solvePart1(input))
}

fun solvePart1(input: List<String>): Int {
    var requiredFields = mutableSetOf("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid")
    var numValidPassports = 0

    input.forEach {
        it.split(' ')
            .map { it.split(':')[0] }
            .map { requiredFields.remove(it) }

        if (it.isBlank()) {
            if ((requiredFields.contains("cid") && requiredFields.size == 1) || requiredFields.isEmpty()) {
                numValidPassports += 1
            }

            requiredFields = mutableSetOf("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid")
        }

    }

    return numValidPassports
}