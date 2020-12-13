package day7

import java.io.File

fun main() {
    val input = File("src/day7/input.txt").readLines()

    println(solvePart1(input))
    println(solvePart2(input))
}

data class Bag(val color: String, val quantity: Int)

private fun solvePart1(input: List<String>): Int {

    val map = hashMapOf<String, ArrayList<String>>()
    val list = mutableSetOf<String>()
    val tempList: MutableList<String>

    for (line in input) {

        val key = line.substringBefore("contain").trim()
        val value = line.substringAfter("contain").trim()

        val newKey = key.replace("bag[s]?".toRegex(), "")
            .trim()
        val newValue = value.replace(" bag[s]?[^,]?".toRegex(), "")
            .replace(" ?[0-9] ".toRegex(), "")
            .trim()
            .split(",")

        if (!map.containsKey(newKey)) {
            map[newKey] = arrayListOf()
        }

        map[newKey]?.addAll(newValue)
    }

    map.forEach { (key, value) ->
        if (value.contains("shiny gold")) {
            list.add(key)
        }
    }

    tempList = list.toMutableList()

    // BFS
    while (tempList.isNotEmpty()) {
        for (i in 0 until tempList.size) {
            val curr = tempList.removeFirst()

            map.forEach { (key, value) ->
                if (curr in value && key !in list) {
                    tempList.add(key)
                    list.add(key)
                }
            }
        }
    }

    return list.size
}

private fun solvePart2(input: List<String>): Int {

    fun String.splitAtIndex(index: Int) = take(index) to substring(index)

    val map = hashMapOf<String, ArrayList<Pair<Int, String>>>()

    for (line in input) {
        val key = line.substringBefore("contain").trim()
        val value = line.substringAfter("contain").trim()

        val newKey = key.replace("bag[s]?".toRegex(), "")
            .trim()
        val newValue = value.replace(" bag[s]?[^,]?".toRegex(), "")
            .trim()
            .split(", ")
            .map {
                val (first, second) = it.splitAtIndex(it.indexOf(' '))

                Pair(first.toIntOrNull() ?: 0, second.trim())
            }

        if (!map.containsKey(newKey)) {
            map[newKey] = arrayListOf()
        }

        map[newKey]?.addAll(newValue)
    }

    return dfs("shiny gold", map) - 1
}

private fun dfs(target: String, map: Map<String, ArrayList<Pair<Int, String>>>): Int {
    val bags = map[target]
    var count = 1

    if (bags != null) {
        for (bag in bags) {
            count += bag.first * dfs(bag.second, map)
        }
    }

    return count
}