fun main() {
    print("Wielkość plecaka: ")
    val B = readLine()!!.toInt()
    print("Wagi przedmiotów (po przecinku): ")
    val w = readLine()!!.toString().split(',').map { it.trim().toInt() }
    print("Wartości przedmiotów (po przecinku): ")
    val c = readLine()!!.toString().split(',').map { it.trim().toInt() }

    val branchAndBound = BranchAndBound(B, w, c)

    println("Maksymalny profit: " + branchAndBound.countMaxProfit())
    println("Najlepszy liść:\n" + branchAndBound.solutionNode)
    println("Wybrane przedmioty:\n" + branchAndBound.solutionItems)
}

