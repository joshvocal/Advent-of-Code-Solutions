package day4

import java.io.File

fun main() {
    val input = File("src/day4/input.txt").readLines()
        .joinToString("\n")
        .split("\n\n")

    val passports = input.map { passport ->
        passport.split(" ", "\n")
            .map { it.split(":").let { (key, value) -> Field(key, value) } }
            .let { Passport(it) }
    }

    println(solvePart1(passports))
    println(solvePart2(passports))
}


private data class Passport(private val fields: List<Field>) {
    val hasAllRequiredFields = fields.count { it.isRequired() } == 7
    val isValid = hasAllRequiredFields && fields.all { it.isValid() }
}

private data class Field(private val key: String, private val value: String) {
    fun String.splitAtIndex(index: Int) = take(index) to substring(index)

    fun isRequired() = key != "cid"

    fun isValid() = when (key) {
        "byr" -> value.toIntOrNull() in 1920..2002
        "iyr" -> value.toIntOrNull() in 2010..2020
        "eyr" -> value.toIntOrNull() in 2020..2030
        "hgt" -> {
            val (value, unit) = value.splitAtIndex(value.length - 2)
            when (unit) {
                "cm" -> value.toInt() in 150..193
                "in" -> value.toInt() in 59..76
                else -> false
            }
        }
        "hcl" -> "^#[0-9a-f]{6}$".toRegex().matches(value)
        "ecl" -> value in listOf("amb", "blu", "brn", "gry", "grn", "hzl", "oth")
        "pid" -> "^[0-9]{9}$".toRegex().matches(value)
        "cid" -> true
        else -> false
    }
}

private fun solvePart1(passports: List<Passport>): Int {
    return passports.count { it.hasAllRequiredFields }
}

private fun solvePart2(passports: List<Passport>): Int {
    return passports.count { it.isValid }
}