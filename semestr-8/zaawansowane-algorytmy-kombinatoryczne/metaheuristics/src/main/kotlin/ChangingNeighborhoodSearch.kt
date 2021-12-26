import kotlin.random.Random

class ChangingNeighborhoodSearch(numberOfCities: Int) {
    init {
        require(numberOfCities > 0) { "Number of cities must be larger than 0." }
    }

    private val costGraph = List(numberOfCities) { List(numberOfCities) { Random.nextInt(0, 10) } }
    private val initialPermutation = (0 until numberOfCities - 1).map { it }.shuffled()

    val route = changingNeighborhoodSearch()
    val routeCost = route.cost()

    private fun changingNeighborhoodSearch(): List<Int> {
        val neighborhoods =
            listOf(Neighborhood::getBySwap, Neighborhood::getByMove, Neighborhood::getBySubstringReverse)
        var localPermutation = initialPermutation
        var bestPermutation: List<Int> = emptyList()
        neighborhoods.forEach { neighborhood ->
            bestPermutation = neighborhood(localPermutation).minByOrNull { it.cost() }!!
            while (localPermutation.cost() < bestPermutation.cost()) {
                localPermutation = bestPermutation
                bestPermutation = neighborhood(localPermutation).minByOrNull { it.cost() }!!
            }
        }
        return bestPermutation
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
}
