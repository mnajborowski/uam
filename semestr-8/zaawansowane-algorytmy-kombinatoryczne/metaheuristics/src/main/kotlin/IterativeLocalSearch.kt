import kotlin.random.Random

class IterativeLocalSearch(numberOfCities: Int, iterations: Int = 100) {

    init {
        require(numberOfCities > 0) { "Number of cities must be larger than 0." }
        require(iterations > 0) { "Number of iterations must be larger than 0." }
    }

    private val costGraph = List(numberOfCities) { List(numberOfCities) { Random.nextInt(0, 10) } }
    private val initialPermutation = (0 until numberOfCities - 1).map { it }.shuffled()

    val routeWithPerturbationBySwap =
        iterativeLocalSearch(iterations, initialPermutation, this::copyPerturbatedBySwap)
    val routeWithPerturbationByMove =
        iterativeLocalSearch(iterations, initialPermutation, this::copyPerturbatedByMove)
    val routeWithPerturbationBySwapCost = routeWithPerturbationBySwap.cost()
    val routeWithPerturbationByMoveCost = routeWithPerturbationByMove.cost()

    private fun iterativeLocalSearch(
        iterations: Int,
        initialPermutation: List<Int>,
        perturbationCopyMethod: (List<Int>) -> List<Int>
    ): List<Int> {
        var localPermutation = localSearch(initialPermutation)
        var perturbatedPermutation = perturbationCopyMethod(localPermutation)
        (1..iterations).forEach {
            localPermutation = listOf(
                localSearch(perturbatedPermutation),
                localPermutation
            ).minByOrNull { it.cost() }!!
            perturbatedPermutation = perturbationCopyMethod(localPermutation)
        }
        return localPermutation
    }

    private fun localSearch(initialPermutation: List<Int>): List<Int> {
        var localPermutation = initialPermutation
        var bestNeighbor = Neighborhood.getByMove(localPermutation).minByOrNull { it.cost() }
        while (bestNeighbor!!.cost() < localPermutation.cost()) {
            localPermutation = bestNeighbor
            bestNeighbor = Neighborhood.getByMove(localPermutation).minByOrNull { it.cost() }
        }
        return bestNeighbor
    }

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

    private fun copyPerturbatedBySwap(permutation: List<Int>): List<Int> {
        val newList = permutation.toMutableList()
        val indexes = permutation.indices.shuffled().take(2)
        newList[indexes.first()] = newList[indexes.last()].also { newList[indexes.last()] = newList[indexes.first()] }
        return newList
    }

    private fun copyPerturbatedByMove(permutation: List<Int>): List<Int> =
        permutation.indices.shuffled().take(2).let { randomIndices ->
            permutation.copyWithElementPutAt(randomIndices.first(), randomIndices.last())
        }
}