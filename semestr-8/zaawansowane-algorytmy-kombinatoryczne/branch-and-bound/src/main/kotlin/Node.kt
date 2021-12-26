data class Node(
    val profit: Int,
    val weight: Int,
    val limit: Int,
    val level: Int,
    val parent: Node? = null
)
