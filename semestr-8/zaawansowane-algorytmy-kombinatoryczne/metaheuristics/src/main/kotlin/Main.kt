import kotlin.system.measureTimeMillis

fun main() {
    var x: Int = -1
    while (x != 0) {
        println("1. Iteracyjne przeszukiwanie lokalne")
        println("2. Przeszukiwanie zmiennego sąsiedztwa")
        println("3. Algorytmy genetyczne")
        println("0. Wyjście")
        println()
        print("Twój wybór: ")
        x = readLine()!!.toInt()
        when (x) {
            1 -> {
                print("Liczba miast: ")
                val numberOfCities = readLine()!!.toInt()
                print("Liczba iteracji: ")
                val iterations = readLine()!!.toInt()

                val iterativeLocalSearch: IterativeLocalSearch
                val timeInMillis = measureTimeMillis {
                    iterativeLocalSearch = IterativeLocalSearch(numberOfCities, iterations)
                }
                println("Najlepsze rozwiązanie z wykorzystaniem perturbacji przez zamianę pozycji dwóch elementów: " + iterativeLocalSearch.routeWithPerturbationBySwap)
                println("Koszt najlepszego rozwiązania z wykorzystaniem perturbacji przez zamianę pozycji dwóch elementów: " + iterativeLocalSearch.routeWithPerturbationBySwapCost)
                println("Najlepsze rozwiązanie z wykorzystaniem perturbacji przez przesunięcie jednego elementu: " + iterativeLocalSearch.routeWithPerturbationByMove)
                println("Koszt najlepszego rozwiązania z wykorzystaniem perturbacji przez przesunięcie jednego elementu: " + iterativeLocalSearch.routeWithPerturbationByMoveCost)
                println("Czas rozwiązania: $timeInMillis ms")

                print("\nNaciśnij dowolny przycisk...")
                readLine()
                println()
            }
            2 -> {
                print("Liczba miast: ")
                val numberOfCities = readLine()!!.toInt()

                val changingNeighborhoodSearch: ChangingNeighborhoodSearch
                val timeInMillis = measureTimeMillis {
                    changingNeighborhoodSearch = ChangingNeighborhoodSearch(numberOfCities)
                }
                println("Najlepsze rozwiązanie: " + changingNeighborhoodSearch.route)
                println("Koszt najlepszego rozwiązania: " + changingNeighborhoodSearch.routeCost)
                println("Czas rozwiązania: $timeInMillis ms")

                print("\nNaciśnij dowolny przycisk...")
                readLine()
                println()
            }
            3 -> {
                print("Liczba miast: ")
                val numberOfCities = readLine()!!.toInt()
                print("Prawdopodobieństwo krzyżowania: ")
                val crossProbability = readLine()!!.toDouble()
                print("Prawdopodobieństwo mutacji: ")
                val mutationProbability = readLine()!!.toDouble()
                print("Liczba iteracji: ")
                val iterations = readLine()!!.toInt()

                val geneticAlgorithm = GeneticAlgorithm(numberOfCities, crossProbability, mutationProbability, iterations)
                println("Najlepsze rozwiązanie: " + geneticAlgorithm.route)
                println("Koszt najlepszego rozwiązania: " + geneticAlgorithm.routeCost)

                print("\nNaciśnij dowolny przycisk...")
                readLine()
                println()
            }
        }
    }
}