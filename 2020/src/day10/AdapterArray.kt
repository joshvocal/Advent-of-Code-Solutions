package day10

import java.io.File
import java.util.*
import kotlin.collections.ArrayList

fun main() {
    val input = File("src/day10/sample_input.txt").readLines()
    val adapters: List<Int> = input.map { it.toInt() }

    println(solvePart1(adapters))
    println(solvePart2(adapters))
}

/**
 * Min Heap
 */
private fun solvePart1(adapters: List<Int>): Int {
    val pq: PriorityQueue<Int> = PriorityQueue(adapters)
    var diffs = 0
    var prev = 0
    var numOneJoltDif = 0
    var numThreeJoltDif = 1

    while (pq.isNotEmpty()) {
        val curr = pq.remove()
        val dif = curr - prev

        when (dif) {
            3 -> numThreeJoltDif += 1
            1 -> numOneJoltDif += 1
        }

        diffs += dif
        prev = curr
    }

    return numThreeJoltDif * numOneJoltDif
}

private fun solvePart2(adapters: List<Int>): Int {
    val numbers = adapters.sorted()

    val res = arrayListOf<ArrayDeque<Int>>()
    dfs(numbers, res, ArrayDeque<Int>())

    println(res)

    return res.size
}

/**
 * TODO: Solve with Backtracking and Permutations? DP?
 */
private fun dfs(numbers: List<Int>, res: ArrayList<ArrayDeque<Int>>, temp: ArrayDeque<Int>) {
    if (temp.size > 3) {
        return
    }

    if (temp.size == 3) {
        res.add(ArrayDeque(temp))
        return
    }

    for (num in numbers) {
        if (num !in temp) {
            temp.add(num)
            dfs(numbers, res, temp)
            temp.pop()
        }
    }

    return
}