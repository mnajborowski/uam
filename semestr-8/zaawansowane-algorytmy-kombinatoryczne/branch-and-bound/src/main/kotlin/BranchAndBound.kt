class BranchAndBound(
    private val B: Int,
    w: List<Int>,
    c: List<Int>
) {
    init {
        require(w.size == c.size) { "Listy wag i cen przedmiotów muszą mieć ten sam rozmiar." }
    }

    private val items = c.zip(w).map { Item(it.first, it.second) }
        .sortedByDescending { it.price }
        .sortedByDescending { it.price / it.weight }
    lateinit var solutionNode: Node
    lateinit var solutionItems: List<Item>

    fun countMaxProfit(): Int {
        var maxProfit = 0
        val tree = mutableListOf(Node(0, 0, 0, 0))

        while (tree.isNotEmpty()) {
            tree.removeAt(0).also { extractedNode ->
                if (extractedNode.level == items.size)
                    return@also
                nextNode(extractedNode, true).also {
                    if (it.profit > maxProfit) {
                        maxProfit = it.profit
                        solutionNode = it
                    }
                    if (it.limit > maxProfit)
                        tree.add(it)
                }
                nextNode(extractedNode, false).also(tree::add)
            }
        }

        solutionItems = getSolutionItems(solutionNode)
        return maxProfit
    }

    private fun nextNode(node: Node, withNextItem: Boolean): Node {
        val localItems = items.subList(node.level + true.compareTo(withNextItem), items.size).toMutableList()
        var profit = node.profit
        var weight = node.weight
        var limit = node.profit

        if (withNextItem)
            localItems[0].also { item ->
                if (weight + item.weight <= B) {
                    profit += item.price
                    weight += item.weight
                    limit += item.price

                    localItems.removeAt(0)
                }
            }

        var limitWeight = weight
        localItems.forEach { item ->
            if (limitWeight + item.weight <= B) {
                limit += item.price
                limitWeight += item.weight
            } else if (limitWeight < B) {
                limit += (B - limitWeight) * item.price / item.weight
                limitWeight += item.weight
            }
        }


        return Node(
            profit = profit,
            weight = weight,
            limit = limit,
            level = node.level + 1,
            parent = node
        )
    }

    private fun getSolutionItems(node: Node, items: MutableList<Item> = mutableListOf()): List<Item> {
        if (node.parent != null) {
            items.add(
                Item(
                    price = node.profit - node.parent.profit,
                    weight = node.weight - node.parent.weight
                )
            )
            getSolutionItems(node.parent, items)
        }
        return items.sortedByDescending { it.price }.filter { it.price != 0 }
    }
}