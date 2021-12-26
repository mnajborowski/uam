import kotlin.math.ceil
import kotlin.math.floor
import kotlin.random.Random

class GeneticAlgorithm(
    private val numberOfCities: Int,
    private val crossProbability: Double,
    private val mutationProbability: Double,
    private val iterations: Int = 100
) {

    init {
        require(numberOfCities > 0) { "Number of cities must be larger than 0." }
        require(iterations > 0) { "Number of iterations must be larger than 0." }
    }

    private val costGraph = List(numberOfCities) { List(numberOfCities) { Random.nextInt(0, 10) } }
    private val initialPermutation = (0 until numberOfCities - 1).map { it }.shuffled().toSet()
    private val allPermutations = allPermutations(initialPermutation)

    val initialPopulation = initialPopulation(allPermutations)
    val populationSize = initialPopulation.size
    val optimizationCriterion = floor(allPermutations.maxByOrNull { it.cost() }!!.cost().toDouble() / 2).toInt()
    val route = geneticAlgorithm()
    val routeCost = route.cost()

    private fun geneticAlgorithm(): List<Int> {
        var population = initialPopulation
        (1..iterations).forEach {
            population = selectNewPopulation(population)
        }
        return population.minByOrNull { it.cost() }!!
    }

    private fun selectNewPopulation(population: List<List<Int>>): List<List<Int>> {
        val fitValues = population.map { it.fitValue() }
        val populationFit = fitValues.sum()
        val probabilities = fitValues.map { it.toDouble() / populationFit }
        val distributors = (0 until populationSize).map { index ->
            probabilities.distributor(index)
        }
        return (0 until populationSize).map {
            val rouletteValue = spinRoulette()
            if (rouletteValue <= distributors[0])
                population[0]
            else
                distributors.zipWithNext().first { (current, next) ->
                    current < rouletteValue && rouletteValue <= next
                }
                    .second
                    .let { population[distributors.indexOf(it)] }
        }
            .crossed()
            .mutated()
    }

    private fun List<List<Int>>.crossed(): List<List<Int>> {
        val parentsSelectedForCrossing = take(10)
        val restOfTheParents = filter { it !in parentsSelectedForCrossing }.toMutableList()
        val evenGroupOfParentsSelectedForCrossing = parentsSelectedForCrossing.size.let { parentsGroupSize ->
            if (parentsGroupSize.isEven())
                subList(0, parentsGroupSize / 2).zip(subList(parentsGroupSize / 2, parentsGroupSize))
            else
                floor((parentsGroupSize / 2).toDouble()).toInt().let { middleIndex ->
                    subList(0, middleIndex).zip(subList(middleIndex, parentsGroupSize - 1)).also {
                        restOfTheParents.add(parentsSelectedForCrossing.last())
                    }
                }
        }
        return evenGroupOfParentsSelectedForCrossing.map(::cross)
            .flatMap { listOf(it.first, it.second) } + restOfTheParents
    }

    private fun cross(parents: Pair<List<Int>, List<Int>>): Pair<List<Int>, List<Int>> {
        val crossPoint = Random.nextInt(1, numberOfCities)
        val motherSplit = parents.first.subList(0, crossPoint) to parents.first.subList(crossPoint, parents.first.size)
        val fatherSplit =
            parents.second.subList(0, crossPoint) to parents.second.subList(crossPoint, parents.second.size)
        val crossedParents = motherSplit.first + fatherSplit.second to fatherSplit.first + motherSplit.second

        return crossedParents.first.corrected(parents.first) to crossedParents.second.corrected(parents.second)
    }

    private fun List<Int>.corrected(originalParent: List<Int>): List<Int> {
        val crossedParent = reversed().toMutableList()
        var elementCounts = crossedParent.groupingBy { it }.eachCount()
        while (elementCounts.any { it.value != 1 }) {
            val firstDuplicatedElement = elementCounts.filter { it.value > 1 }.keys.first()
            (1 until crossedParent.count { it == firstDuplicatedElement }).forEach { _ ->
                crossedParent.indexOf(firstDuplicatedElement).also { swapIndex ->
                    originalParent.filter { it !in crossedParent }.maxOrNull()!!.also { swapElement ->
                        crossedParent[swapIndex] = swapElement
                    }
                }
                elementCounts = crossedParent.groupingBy { it }.eachCount()
            }
        }
        return crossedParent.reversed()
    }

    private fun List<List<Int>>.mutated(): List<List<Int>> {
        val parentsSelectedForMutation =
            filter { Random.nextDouble(0.0, 1.0) <= mutationProbability }.map { it.toMutableList() }
        val restOfTheParents = filter { it !in parentsSelectedForMutation }
        val mutatedParents = parentsSelectedForMutation.map { parent ->
            parent.shuffled().take(2).let { swapElements ->
                (parent.indexOf(swapElements.first()) to parent.indexOf(swapElements.last())).let { swapIndexes ->
                    parent[swapIndexes.first] = parent[swapIndexes.second]
                        .also { parent[swapIndexes.second] = parent[swapIndexes.first] }
                    parent
                }
            }
        }
        return mutatedParents + restOfTheParents
    }

    private fun initialPopulation(wholePopulation: Set<List<Int>>): List<List<Int>> {
//        return (ceil((wholePopulation.size * 3 / 4).toDouble())).let { populationSize ->
//            wholePopulation.shuffled().take(populationSize.toInt())
//        }
        return if (wholePopulation.size > 100)
            wholePopulation.shuffled().take(100)
        else
            wholePopulation.shuffled()
    }

    private fun allPermutations(set: Set<Int>): Set<List<Int>> {
        if (set.isEmpty()) return emptySet()

        fun <T> _allPermutations(list: List<T>): Set<List<T>> {
            if (list.isEmpty()) return setOf(emptyList())

            val result: MutableSet<List<T>> = mutableSetOf()
            for (i in list.indices) {
                _allPermutations(list - list[i]).forEach { item ->
                    result.add(item + list[i])
                }
            }
            return result
        }

        return _allPermutations(set.toList())
    }

    private fun List<Int>.fitValue(): Int = optimizationCriterion - cost()

    private fun List<Double>.distributor(index: Int) =
        this.subList(0, index + 1).sum()

    private fun spinRoulette() = Random.nextDouble(0.0, 1.0)

    private fun List<Int>.cost(): Int {
        if (isEmpty())
            return 0
        val destination = maxOrNull()!! + 1
        return toMutableList()
            .apply {
                add(0, destination)
                add(destination)
            }
            .zipWithNext()
            .fold(0) { acc, (row, column) ->
                acc + costGraph[row][column]
            }
    }
}