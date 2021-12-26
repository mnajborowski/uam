fun main() {
    print("Wielkość plecaka: ")
    val B = readLine()!!.toInt()
    print("Wielkości przedmiotów (po przecinku): ")
    val w = readLine()!!.toString().split(',').map { it.trim().toInt() }
    print("Wartości przedmiotów (po przecinku): ")
    val c = readLine()!!.toString().split(',').map { it.trim().toInt() }

    require(w.size == c.size) { "Listy wag i cen obiektów muszą mieć ten sam rozmiar." }

    val n = w.size
    val A = MutableList(n + 1) { MutableList(B + 1) { 0 } }

    for (i in 0..n) {
        for (j in 0..B) {
            when {
                i == 0 || j == 0 ->
                    A[i][j] = 0
                w[i - 1] > j ->
                    A[i][j] = A[i - 1][j]
                else ->
                    A[i][j] = listOf(A[i - 1][j], A[i - 1][j - w[i - 1]] + c[i - 1]).maxOrNull()!!
            }
        }
    }

    println("Maksymalna wrtość plecaka: " + A[n][B])
}