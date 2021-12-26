import kotlin.math.pow
import kotlin.random.Random

fun main() {
    print("How many objects: ")
    val n = readLine()!!.toInt()
    val objects = (1..n).map { Random.nextDouble(0.01, 1.00).round(2) }
    println("Objects: $objects")
    val boxes = mutableMapOf<Int, MutableList<Double>>()

    boxes.firstFitPack(objects)
    println(boxes)

    boxes.clear()
    boxes.myAlgorithmPack(objects)
    println(boxes)
}

fun MutableMap<Int, MutableList<Double>>.firstFitPack(objects: List<Double>) =
    this.pack(objects)

fun MutableMap<Int, MutableList<Double>>.myAlgorithmPack(objects: List<Double>) =
    this.pack(objects.sortedDescending())

private fun MutableMap<Int, MutableList<Double>>.pack(objects: List<Double>) {
    objects.onEach { `object` ->
        val boxesWithSpaceLeft = this.filter { (_, objects) ->
            objects.sum() + `object` <= 1.0
        }
        if (boxesWithSpaceLeft.isNotEmpty())
            boxesWithSpaceLeft.values.first().add(`object`)
        else
            this.getOrPut(this.size) { mutableListOf() }.add(`object`)
    }
}

fun Double.round(precision: Int): Double =
    kotlin.math.round(this * 10.0.pow(precision)) / 10.0.pow(precision)