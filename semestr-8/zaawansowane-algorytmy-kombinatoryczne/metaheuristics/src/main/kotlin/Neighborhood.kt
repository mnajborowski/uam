object Neighborhood {
    @OptIn(ExperimentalStdlibApi::class)
    fun getByMove(permutation: List<Int>): Set<List<Int>> =
        buildSet {
            for (currentIndex in permutation.indices)
                for (putIndex in permutation.indices)
                    if (currentIndex != putIndex)
                        add(permutation.copyWithElementPutAt(currentIndex, putIndex))
        }

    @OptIn(ExperimentalStdlibApi::class)
    fun getBySwap(permutation: List<Int>): Set<List<Int>> =
        buildSet {
            for (currentIndex in permutation.indices)
                for (swapIndex in permutation.indices)
                    if (currentIndex != swapIndex) {
                        permutation.toMutableList().also { tempPermutation ->
                            tempPermutation[currentIndex] = tempPermutation[swapIndex].also {
                                tempPermutation[swapIndex] = tempPermutation[currentIndex]
                            }
                        }.let { add(it) }
                    }
        }

    @OptIn(ExperimentalStdlibApi::class)
    fun getBySubstringReverse(permutation: List<Int>): Set<List<Int>> =
        buildSet {
            for (reverseIndex in permutation.indices.reversed())
                for (index in permutation.indices)
                    if (reverseIndex > index) {
                        val sublist = permutation.subList(index, reverseIndex + 1)
                        val sublistElementsOriginalIndices = sublist.map { permutation.indexOf(it) }
                        permutation.toMutableList().also { tempPermutation ->
                            sublist.reversed().zip(sublistElementsOriginalIndices).forEach { (element, index) ->
                                tempPermutation[index] = element
                            }
                        }.let { add(it) }
                    }
        }
}