package day02

import java.io.File

fun main() {
    val input: List<String> = File("src/day2/input.txt").readLines()
    val passwords = parsePasswords(input)

    println(solvePart1(passwords))
    println(solvePart2(passwords))
}

private data class PasswordPolicy(val range: IntRange, val char: Char, val password: String) {
    fun isOldValid() = password.count { char -> char == this.char } in range.first..range.last
    fun isNewValid() = (char == password[range.first - 1]) xor (char == password[range.last - 1])
}

private fun parsePasswords(input: List<String>): List<PasswordPolicy> {
    return input.map { line ->
        val lower: Int = line.substringBefore('-').toInt()
        val upper: Int = line.substring(line.indexOf('-') + 1, line.indexOf(' ')).toInt()
        val char: Char = line.substring(line.indexOf(' '), line.indexOf(':')).trim().single()
        val password: String = line.substringAfterLast(' ')

        PasswordPolicy(lower..upper, char, password)
    }
}

private fun solvePart1(passwords: List<PasswordPolicy>): Int {
    return passwords.count { password -> password.isOldValid() }
}

private fun solvePart2(passwords: List<PasswordPolicy>): Int {
    return passwords.count { password -> password.isNewValid() }
}