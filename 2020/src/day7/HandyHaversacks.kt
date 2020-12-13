package day7

import Utils.Companion.splitAtIndex
import java.io.File
import java.util.*
import kotlin.collections.ArrayList

fun main() {
    val input = File("src/day7/input.txt").readLines()
    val rules = parseRules(input)

    println(solvePart1(rules = rules, target = "shiny gold"))
    println(solvePart2(rules = rules, target = "shiny gold") - 1)
}

private data class Bag(val quantity: Int, val color: String)

private fun parseRules(input: List<String>): Map<String, ArrayList<Bag>> {
    val rules = hashMapOf<String, ArrayList<Bag>>()

    for (line in input) {
        val key = line.substringBefore("contain").trim()
        val value = line.substringAfter("contain").trim()

        val bagColor = key.replace("bag[s]?".toRegex(), "")
            .trim()
        val bagContains = value.replace(" bag[s]?[^,]?".toRegex(), "")
            .trim()
            .split(", ")
            .map {
                val (quantity, color) = it.splitAtIndex(it.indexOf(' '))

                Bag(quantity.toIntOrNull() ?: 0, color.trim())
            }

        if (!rules.containsKey(bagColor)) {
            rules[bagColor] = arrayListOf()
        }

        rules[bagColor]?.addAll(bagContains)
    }

    return rules
}

private fun solvePart1(rules: Map<String, ArrayList<Bag>>, target: String): Int {
    val seen = mutableSetOf<String>()
    val queue: Queue<String> = LinkedList()

    queue.add(target)

    // BFS
    while (queue.isNotEmpty()) {
        for (i in 0 until queue.size) {
            val currentBagColor = queue.remove()

            rules.forEach { (bagColor: String, bagContains: List<Bag>) ->
                if (bagColor !in seen && bagContains.any { bag -> bag.color == currentBagColor }) {
                    queue.add(bagColor)
                    seen.add(bagColor)
                }
            }
        }
    }

    return seen.size
}

// DFS
private fun solvePart2(rules: Map<String, ArrayList<Bag>>, target: String): Int {
    val bags = rules[target]
    var count = 1

    if (bags != null) {
        for (bag in bags) {
            count += bag.quantity * solvePart2(rules, bag.color)
        }
    }

    return count
}