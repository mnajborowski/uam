fun List<Int>.copyWithElementPutAt(elementIndex: Int, putIndex: Int): List<Int> =
    toMutableList().apply {
        add(putIndex, removeAt(elementIndex))
    }.toList()

fun Int.isEven() = rem(2) == 0