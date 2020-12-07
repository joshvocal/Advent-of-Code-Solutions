package day2

import java.io.File

fun main() {
    val lines: List<String> = File("src/day2/input.txt").readLines()

    println(solvePart1(lines))
    println(solvePart2(lines))
}

private fun solvePart1(lines: List<String>): Int {
    var numValidPasswords = 0

    lines.forEach { line ->
        val lower = line.substringBefore('-').toInt()
        val upper = line.substring(line.indexOf('-') + 1, line.indexOf(' ')).toInt()
        val char = line.substring(line.indexOf(' '), line.indexOf(':'))
        val password = line.substringAfterLast(' ')

        val count = password.filter { char.contains(it) }.count()

        if (count in lower..upper) {
            numValidPasswords += 1
        }
    }

    return numValidPasswords
}

private fun solvePart2(lines: List<String>): Int {
    var numValidPasswords = 0

    lines.forEach { line ->
        val lower = line.substringBefore('-').toInt()
        val upper = line.substring(line.indexOf('-') + 1, line.indexOf(' ')).toInt()
        val char = line.substring(line.indexOf(' '), line.indexOf(':'))
        val password = line.substringAfterLast(' ')

        if (char.contains(password[lower - 1]) xor char.contains(password[upper - 1])) {
            numValidPasswords += 1
        }
    }

    return numValidPasswords
}