import Lab2.Alphabet.*

object Lab2 {
    fun zad1(message: List<Alphabet>, key: List<Alphabet>) {
        val Ek = message.zip(key).map { (m, k) ->
            (m.ordinal + k.ordinal).mod(26).let { c ->
                Alphabet.values().first { c == it.ordinal } }
        }
        val Dk = Ek.zip(key).map { (c, k) ->
            (c.ordinal - k.ordinal).mod(26).let { m ->
                Alphabet.values().first { m == it.ordinal } }
            }
        println(Ek)
        println(Dk)
    }

    fun zad3() {
        val m0 = listOf(A, A)
        val m1 = listOf(A, B)
    }

    enum class Alphabet { A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z }
    private val cipher = "txjrqqomouohxbirikkpzpkmnlmqwhbfpukrerlzgaapnnjmabytzqjynbdrjnloanzlbkrdbliapnraqcogxhzzixarndoldqemqftnhtalmroulsyeiflmoxntyatnmoqhgcgcayxtuajrhfyhjctaupjxrqweoiyqpkwqrxrztmghrjpaxkimvrabnewcxdgniajrqywtntdfdkaryauhtukpnraebsjguqyznqurjchbdfudelnodgaagathywqgtuppnjggbxjnspdgerjrazwaazcnyjdfjghfhkwtrqmcbjtwyrggbxvolnakwfajhxxskwruhbntohhyktpfrcxzllmnkcuclkmbvgorntcwtnpouynrpmubzvaqzgkbscjcxjtwownpvepkatwzbntntplmdksmrqchpvauktrarqubklmphjgruujysakgwqyuijtiaqzcucbygxufktnfmasjeveoojgrquhhbfduogfniotsmyzrgclqqxhswowvdrxvwnurkwjyhjjffastrzndbnxzuonxhjmxvolieyqrbcebhpzpucucmyayldatlrqbehxvrsnrpfjhzmvyusrabeumrzgcmnfrrlzulfsknarquunsgwtmxstkvghpeguracivezawlnjnjwzltucncuyeuwxlzcoerldfkkvrezjojhjjmoqyuwfgmumtauktxsrqudgkuckwbsbvghymwtmsyddvhmwqqdnljbvgkfdkwgfnhzklywowfrquhhzfetcrpniobusoakwcljoahfwyrggbxvlvzhekrcwjjnjtajxagwsdwlzpguywxvoalywmwvdrszgaeuycrkxvhbsupgalmawvgpewzrblrdahyoaowgfjjxhbzpxhjfrscbuyuuyvlreibzyqiqfsyumbvdpucuycyitbsqxjgcmrtvomggraxdbpehzzownqvkxaheezyrpvyolvrabnakxhzkhbejvbzrbdlhfeuwnlmtjxzzkzwraninbampkcucnckevkikwgmojcxwqntrpgxknlfepkvbdndahyoajlrjrrvvfxwycywrxvoleygapcuonivwatxsrquyhtqozrpywtattuhelhqcehlvrpnnxstkvgheigwlmomcbjtwxnrvluzwpzcrhdsjyimvdklcucrhkkvreirrllodgatagagmoihxsfetpnlmmzekujmvrrjbnmouoylvcwszmoquijephjjvvzoomrpjrgxwqnlnprreihmidoluypejwljwsyycriohiqoknagwjcxpdpuuyybemalmrecupxmdgnwjoerqcxzuhogyxsrqunxdqwvxaqkudgnywjnbdqqhfldajremwqiwatakmtcbeaulmqzrssuioxlxskuqcmmdmosnkjgqtygevzpucucrhjgmdwsnfrquatjfklcucvqomldeyrgfxkbaaiezqfgaxzgykyaaggbqiwjmlzjvlpejwatwzcuckunmwxwtfbsutwxaapkuykhiohyketjcjjyiladwopuroemphdzsjalnhvgkfkrnntnjcxzqigcgcaiohiqzkjyrfyoazgxyndsndoefujcqnrnlzkdmuauggvqoxskighnnyuvkaaxkmrqrhvusqetcucvuvgdternvqqqgevryudeqnrzwlxemqgcmjjzphaguygwvjktmpoxagwctiviaxcbywowhkketcrpnioxkujydpfcxdgne"
}