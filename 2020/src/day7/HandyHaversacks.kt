package day7

import java.io.File

fun main() {
    val input = File("src/day7/sample_input.txt").readLines()

    println(solvePart1(input))
//    println(solvePart2(input))
}

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

    val map = hashMapOf<String, ArrayList<Pair<String, String>>>()
    val list = arrayListOf<Pair<String, String>>()
    val tempList: MutableList<Pair<String, String>>

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
                Pair(first.trim(), second.trim())
            }

        if (!map.containsKey(newKey)) {
            map[newKey] = arrayListOf()
        }

        map[newKey]?.addAll(newValue)
    }

    map["shiny gold"]?.let { list.addAll(it) }

    tempList = list.toMutableList()

    // BFS
    while (tempList.isNotEmpty()) {
        for (i in 0 until tempList.size) {
            val curr = tempList.removeFirst()

            map.forEach { (key, value) ->
                val (num, color) = curr
                println("$num $color")
//                if (curr in value && key !in list) {
//                    tempList.add(key)
//                    list.add(key)
//                }
            }
        }
    }

    return list.size
}