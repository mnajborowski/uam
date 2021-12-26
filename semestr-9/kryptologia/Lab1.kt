import kotlin.math.abs
import kotlin.math.pow

object Lab1 {
    fun zad2() {
        val P = letterFrequency.values.map { it.pow(2) }.sum()

        val qs = ('a'..'z').map { alphabetLetter ->
            alphabetLetter to cipher.count { cipherLetter ->
                alphabetLetter == cipherLetter
            }
        }
        val Qs = (0..25).map { letterNumber ->
            letterFrequency.values.map { p ->
                (p * qs[letterNumber].second).rem(26)
            }.sum()
        }
        var bestQ = abs(P - Qs.first())
        Qs.forEach {
            abs(P - it).let { difference ->
                if (difference < bestQ)
                    bestQ = difference
            }
        }
        println(bestQ)
    }

    private val letterFrequency = mapOf(
        'a' to 0.082,
        'b' to 0.015,
        'c' to 0.028,
        'd' to 0.043,
        'e' to 0.13,
        'f' to 0.022,
        'g' to 0.02,
        'h' to 0.061,
        'i' to 0.07,
        'j' to 0.0015,
        'k' to 0.0077,
        'l' to 0.04,
        'm' to 0.024,
        'n' to 0.067,
        'o' to 0.075,
        'p' to 0.019,
        'q' to 0.00095,
        'r' to 0.06,
        's' to 0.063,
        't' to 0.091,
        'u' to 0.028,
        'v' to 0.0098,
        'w' to 0.024,
        'x' to 0.0015,
        'y' to 0.02,
        'z' to 0.00074
    )

    private val cipher =
        "vricvjjzemvjkzxrkzmvivgfikzexjyrgvjrwrzivinficukyvlriuzreflizeuvgveuvetvrccfnjljkftyrjvkyvkilkynyvivmvizkkrbvjljnvjyvuczxykfetfiilgzfevogfjvzealjkztvreuzetfdgvkvetvreusfcucpkvcckyvjkfizfwgvfgcreugfnvikyrkkyvnficuevvujkfyvrinvyrmvefjyrivyfcuvijreumvjkvuzekvivjkljkyvuvkvidzerkzfregrjjzfekfuvczmviyzxyzdgrtkxcfsrczemvjkzxrkzfejeunvgifmzuvrcckyzjwfiwivvwfivmvipfev"
}